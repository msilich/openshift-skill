<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To monitor and troubleshoot `AdminNetworkPolicy` and `BaselineAdminNetworkPolicy` resources in OpenShift Container Platform, you can use OVN-Kubernetes metrics that report resource counts, rules, and northbound database objects.

# Metrics for AdminNetworkPolicy

You can use OVN-Kubernetes metrics to monitor `AdminNetworkPolicy` and `BaselineAdminNetworkPolicy` resources. These metrics report policy and rule counts by direction and action, and northbound database objects that the policies create.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>ovnkube_controller_admin_network_policies</code></p></td>
<td style="text-align: left;"><p>Not applicable</p></td>
<td style="text-align: left;"><p>The total number of <code>AdminNetworkPolicy</code> resources in the cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ovnkube_controller_baseline_admin_network_policies</code></p></td>
<td style="text-align: left;"><p>Not applicable</p></td>
<td style="text-align: left;"><p>The total number of <code>BaselineAdminNetworkPolicy</code> resources in the cluster. The value should be 0 or 1.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ovnkube_controller_admin_network_policies_rules</code></p></td>
<td style="text-align: left;"><ul>
<li><p><code>direction</code>: specifies either <code>Ingress</code> or <code>Egress</code>.</p></li>
<li><p><code>action</code>: specifies either <code>Pass</code>, <code>Allow</code>, or <code>Deny</code>.</p></li>
</ul></td>
<td style="text-align: left;"><p>The total number of rules across all ANP policies in the cluster grouped by <code>direction</code> and <code>action</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ovnkube_controller_baseline_admin_network_policies_rules</code></p></td>
<td style="text-align: left;"><ul>
<li><p><code>direction</code>: specifies either <code>Ingress</code> or <code>Egress</code>.</p></li>
<li><p><code>action</code>: specifies either <code>Allow</code> or <code>Deny</code>.</p></li>
</ul></td>
<td style="text-align: left;"><p>The total number of rules across all BANP policies in the cluster grouped by <code>direction</code> and <code>action</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ovnkube_controller_admin_network_policies_db_objects</code></p></td>
<td style="text-align: left;"><p><code>table_name</code>: specifies either <code>ACL</code> or <code>Address_Set</code></p></td>
<td style="text-align: left;"><p>The total number of OVN Northbound database (nbdb) objects that are created by all the ANP in the cluster grouped by the <code>table_name</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ovnkube_controller_baseline_admin_network_policies_db_objects</code></p></td>
<td style="text-align: left;"><p><code>table_name</code>: specifies either <code>ACL</code> or <code>Address_Set</code></p></td>
<td style="text-align: left;"><p>The total number of OVN Northbound database (nbdb) objects that are created by all the BANP in the cluster grouped by the <code>table_name</code>.</p></td>
</tr>
</tbody>
</table>
