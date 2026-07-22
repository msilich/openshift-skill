<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Machine Config Daemon, part of the Machine Config Operator, runs on every node in the cluster to manage configuration changes and updates on each of the nodes.

# Understanding Machine Config Daemon metrics

You can access the metrics provided by the Machine Config Daemon by using the Prometheus Cluster Monitoring stack.

The following table describes this set of metrics. Some entries contain commands for getting specific logs. However, the most comprehensive set of logs is available using the `oc adm must-gather` command.

> [!NOTE]
> Metrics marked with `*` in the **Name** and **Description** columns represent serious errors that might cause performance problems. Such problems might prevent updates and upgrades from proceeding.

<table>
<caption>MCO metrics</caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Format</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>mcd_host_os_and_version</code></p></td>
<td style="text-align: left;"><p><code>[]string{"os", "version"}</code></p></td>
<td style="text-align: left;"><p>Shows the OS that MCD is running on, such as RHCOS or RHEL. In case of RHCOS, the version is provided.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mcd_drain_err*</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Logs errors received during failed drain. *</p></td>
<td style="text-align: left;"><p>While drains might need multiple tries to succeed, terminal failed drains prevent updates from proceeding. The <code>drain_time</code> metric, which shows how much time the drain took, might help with troubleshooting.</p>
<p>For further investigation, see the logs by running:</p>
<p><code>$ oc logs -f -n openshift-machine-config-operator machine-config-daemon-&lt;hash&gt; -c machine-config-daemon</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mcd_pivot_err*</code></p></td>
<td style="text-align: left;"><p><code>[]string{"err", "node", "pivot_target"}</code></p></td>
<td style="text-align: left;"><p>Logs errors encountered during pivot. *</p></td>
<td style="text-align: left;"><p>Pivot errors might prevent OS upgrades from proceeding.</p>
<p>For further investigation, run this command to see the logs from the <code>machine-config-daemon</code> container:</p>
<p><code>$ oc logs -f -n openshift-machine-config-operator machine-config-daemon-&lt;hash&gt; -c machine-config-daemon</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mcd_state</code></p></td>
<td style="text-align: left;"><p><code>[]string{"state", "reason"}</code></p></td>
<td style="text-align: left;"><p>State of Machine Config Daemon for the indicated node. Possible states are "Done", "Working", and "Degraded". In case of "Degraded", the reason is included.</p></td>
<td style="text-align: left;"><p>For further investigation, see the logs by running:</p>
<p><code>$ oc logs -f -n openshift-machine-config-operator machine-config-daemon-&lt;hash&gt; -c machine-config-daemon</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mcd_kubelet_state*</code></p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Logs kubelet health failures. *</p></td>
<td style="text-align: left;"><p>This is expected to be empty, with failure count of 0. If failure count exceeds 2, the error indicating threshold is exceeded. This indicates a possible issue with the health of the kubelet.</p>
<p>For further investigation, run this command to access the node and see all its logs:</p>
<p><code>$ oc debug node/&lt;node&gt; — chroot /host journalctl -u kubelet</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mcd_reboot_err*</code></p></td>
<td style="text-align: left;"><p><code>[]string{"message", "err", "node"}</code></p></td>
<td style="text-align: left;"><p>Logs the failed reboots and the corresponding errors. *</p></td>
<td style="text-align: left;"><p>This is expected to be empty, which indicates a successful reboot.</p>
<p>For further investigation, see the logs by running:</p>
<p><code>$ oc logs -f -n openshift-machine-config-operator machine-config-daemon-&lt;hash&gt; -c machine-config-daemon</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mcd_update_state</code></p></td>
<td style="text-align: left;"><p><code>[]string{"config", "err"}</code></p></td>
<td style="text-align: left;"><p>Logs success or failure of configuration updates and the corresponding errors.</p></td>
<td style="text-align: left;"><p>The expected value is <code>rendered-master/rendered-worker-XXXX</code>. If the update fails, an error is present.</p>
<p>For further investigation, see the logs by running:</p>
<p><code>$ oc logs -f -n openshift-machine-config-operator machine-config-daemon-&lt;hash&gt; -c machine-config-daemon</code></p></td>
</tr>
</tbody>
</table>

<div>

<div class="title">

Additional resources

</div>

- [About OpenShift Container Platform monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/about_monitoring/about-ocp-monitoring)

- [Gathering data about your cluster](../support/gathering-cluster-data.md#gathering-cluster-data)

</div>
