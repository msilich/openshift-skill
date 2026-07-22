<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use the vSphere Problem Detector Operator to check a cluster that you deployed on VMware vSphere for common installation and configuration issues that relate to storage.

# About the vSphere Problem Detector Operator

The vSphere Problem Detector Operator checks a cluster that you deployed on VMware vSphere for common installation and configuration issues that relate to storage.

After the Cluster Storage Operator starts and determines that a cluster runs on VMware vSphere, the Cluster Storage Operator launches the vSphere Problem Detector Operator. When the vSphere Problem Detector Operator starts, the Operator immediately runs the checks. The vSphere Problem Detector Operator communicates with the vSphere vCenter Server to find the virtual machines in the cluster, the default datastore, and other information about the vSphere vCenter Server configuration. The Operator uses the credentials from the Cloud Credential Operator to connect to vSphere.

The Operator runs the checks according to the following schedule:

- The checks run every hour.

- If any check fails, the Operator runs the checks again in intervals of 1 minute, 2 minutes, 4, 8, and so on. The Operator doubles the interval up to a maximum interval of 8 hours.

- When all checks pass, the schedule returns to an hour interval.

After a failure, the Operator increases its check frequency to quickly report success when the failure condition gets resolved. You can run the Operator manually for immediate troubleshooting information.

# Running the vSphere Problem Detector Operator checks

You can override the schedule for running the vSphere Problem Detector Operator checks and run the checks immediately.

The vSphere Problem Detector Operator automatically runs the checks every hour. After the Operator starts, the Operator runs the checks immediately. After the Cluster Storage Operator starts and determines that a cluster runs on VMware vSphere, the Cluster Storage Operator starts the vSphere Problem Detector Operator. To run the checks immediately, you can scale the vSphere Problem Detector Operator to `0` and back to `1` so that the Cluster Storage Operator restarts the vSphere Problem Detector Operator.

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

- Scale the Operator to `0`:

  ``` terminal
  $ oc scale deployment/vsphere-problem-detector-operator --replicas=0 \
      -n openshift-cluster-storage-operator
  ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the pods have restarted by running the following command:

  ``` terminal
  $ oc -n openshift-cluster-storage-operator get pod -l name=vsphere-problem-detector-operator -w
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                                                 READY   STATUS    RESTARTS   AGE
  vsphere-problem-detector-operator-77486bd645-9ntpb   1/1     Running   0          11s
  ```

  </div>

  The `AGE` field must indicate that the pod restarted.

</div>

<div>

<div class="title">

Next steps

</div>

- Viewing the events from the vSphere Problem Detector Operator

- Viewing the logs from the vSphere Problem Detector Operator

</div>

# Viewing the events from the vSphere Problem Detector Operator

After the vSphere Problem Detector Operator runs and performs the configuration checks, the Operator creates events that you can view from the command-line interface (CLI) or from the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- The vSphere Problem Detector Operator ran checks on your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

- To view the events by using the CLI, run the following command:

  ``` terminal
  $ oc get event -n openshift-cluster-storage-operator \
      --sort-by={.metadata.creationTimestamp}
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  16m     Normal    Started             pod/vsphere-problem-detector-operator-xxxxx         Started container vsphere-problem-detector
  16m     Normal    Created             pod/vsphere-problem-detector-operator-xxxxx         Created container vsphere-problem-detector
  16m     Normal    LeaderElection      configmap/vsphere-problem-detector-lock    vsphere-problem-detector-operator-xxxxx became leader
  ```

  </div>

- To view the events by using the OpenShift Container Platform web console, navigate to **Home** → **Events** and select `openshift-cluster-storage-operator` from the **Project** menu.

</div>

# Viewing the logs from the vSphere Problem Detector Operator

After the vSphere Problem Detector Operator runs and performs the configuration checks, the Operator creates log records that you can view from the command-line interface (CLI) or from the OpenShift Container Platform web console. Log lines that indicate `passed` means that you do not need to perform any actions.

The ideal output for a log line indicates `passed` or `0 problems`. If a log line indicates `failure` or 1 or more problems, see the information in the "Configuration checks run by the vSphere Problem Detector Operator" document.

<div>

<div class="title">

Prerequisites

</div>

- The vSphere Problem Detector Operator ran checks on your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

- To view the logs by using the CLI, run the following command. A log line that shows `passed` in the output means that you must analyze the log output and resolve the issue.

  ``` terminal
  $ oc logs deployment/vsphere-problem-detector-operator \
      -n openshift-cluster-storage-operator
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  I0108 08:32:28.445696       1 operator.go:209] ClusterInfo passed
  I0108 08:32:28.451029       1 datastore.go:57] CheckStorageClasses checked 1 storage classes, 0 problems found
  I0108 08:32:28.451047       1 operator.go:209] CheckStorageClasses passed
  I0108 08:32:28.452160       1 operator.go:209] CheckDefaultDatastore passed
  I0108 08:32:28.480648       1 operator.go:271] CheckNodeDiskUUID:<host_name> passed
  I0108 08:32:28.480685       1 operator.go:271] CheckNodeProviderID:<host_name> passed
  ```

  </div>

- To view the Operator logs with the OpenShift Container Platform web console, perform the following steps:

  1.  Navigate to **Workloads** → **Pods**.

  2.  Select `openshift-cluster-storage-operator` from the **Projects** menu.

  3.  Click the link for the `vsphere-problem-detector-operator` pod.

  4.  Click the **Logs** tab on the **Pod details** page to view the logs.

</div>

# Configuration checks run by the vSphere Problem Detector Operator

The following tables identify the configuration checks that the vSphere Problem Detector Operator runs. Some checks verify the configuration of the cluster. Other checks verify the configuration of each node in the cluster.

<table>
<caption>Cluster configuration checks</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>CheckDefaultDatastore</code></p></td>
<td style="text-align: left;"><p>Verifies that the default datastore name in the VMware vSphere configuration is short enough for use with dynamic provisioning.</p>
<p>If this check fails, you can expect the following:</p>
<ul>
<li><p><code>systemd</code> logs errors to the journal such as <code>Failed to set up mount unit: Invalid argument</code>.</p></li>
<li><p><code>systemd</code> does not unmount volumes if the virtual machine shuts down or reboots without draining all the pods from the node.</p></li>
</ul>
<p>If this check fails, reconfigure vSphere with a shorter name for the default datastore.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>CheckFolderPermissions</code></p></td>
<td style="text-align: left;"><p>Verifies the permission to list volumes in the default datastore. You must enable the permission to create volumes. The Operator verifies the permission by listing the <code>/</code> and <code>/kubevols</code> directories. When the Operator performs the check, the root directory must exist. The <code>/kubevols</code> directory might not exist at the time of the check. The creation of the <code>/kubevols</code> directory occurs when the datastore supports dynamic provisioning.</p>
<p>If this check fails, review the required permissions for the vCenter account that you specified during the OpenShift Container Platform installation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>CheckStorageClasses</code></p></td>
<td style="text-align: left;"><p>Verifies the following:</p>
<ul>
<li><p>The fully qualified path to each persistent volume that the storage class provisions does not go lower than 255 characters.</p></li>
<li><p>The storage class can use only one storage policy and the policy must be defined.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>CheckTaskPermissions</code></p></td>
<td style="text-align: left;"><p>Verifies the permission to list recent tasks and datastores.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ClusterInfo</code></p></td>
<td style="text-align: left;"><p>Collects the cluster version and UUID from vSphere vCenter.</p></td>
</tr>
</tbody>
</table>

<table>
<caption>Node configuration checks</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>CheckNodeDiskUUID</code></p></td>
<td style="text-align: left;"><p>Verifies that all the vSphere virtual machines include the <code>disk.enableUUID=TRUE</code> configuration.</p>
<p>If this check fails, see the <a href="https://access.redhat.com/solutions/4606201">How to check <code>disk.EnableUUID</code> parameter from VM in vSphere</a> Red Hat Knowledgebase solution.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>CheckNodeProviderID</code></p></td>
<td style="text-align: left;"><p>Verifies that all nodes have the <code>ProviderID</code> configuration from vSphere vCenter. This check fails when the output from the following command does not include a provider ID for each node.</p>
<pre class="terminal"><code>$ oc get nodes -o custom-columns=NAME:.metadata.name,PROVIDER_ID:.spec.providerID,UUID:.status.nodeInfo.systemUUID</code></pre>
<p>If this check fails, reference the vSphere product documentation on how to set the provider ID for each node in the cluster.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>CollectNodeESXiVersion</code></p></td>
<td style="text-align: left;"><p>Reports the version of the ESXi hosts that run nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>CollectNodeHWVersion</code></p></td>
<td style="text-align: left;"><p>Reports the virtual machine hardware version for a node.</p></td>
</tr>
</tbody>
</table>

# About the storage class configuration check

The datastore name and cluster ID relate to the names for persistent volumes that use VMware vSphere storage. After the creation of a persistent volume, `systemd` creates a mount unit for the persistent volume.

The `systemd` process has a 255 character limit for the length of the fully qualified path to the virtual machine disk (VMDK) file. This path follows the naming conventions for `systemd` and vSphere. The naming conventions use the following example pattern:

``` text
/var/lib/kubelet/plugins/kubernetes.io/vsphere-volume/mounts/[<datastore>] 00000000-0000-0000-0000-000000000000/<cluster_id>-dynamic-pvc-00000000-0000-0000-0000-000000000000.vmdk
```

- The naming conventions require 205 characters of the 255 character limit.

- The deployment determines the datastore name and the cluster ID.

- The datastore name and cluster ID substitute into the example pattern. The fully qualified path gets processed with the `systemd-escape` command to escape special characters. For example, after the escape operation, a hyphen character uses four characters, such as `\x2d`.

- After the `systemd-escape` CLI processes the VMDK file path, the length of the path must not be lower than 255 characters. This criteria ensures that the `systemd` process can access the fully qualified VMDK file path.

# Metrics for the vSphere Problem Detector Operator

The vSphere Problem Detector Operator exposes the following metrics for use by the OpenShift Container Platform monitoring stack.

| Name | Description |
|----|----|
| `vsphere_cluster_check_total` | Cumulative number of cluster-level checks that the vSphere Problem Detector Operator performed. This count includes both successes and failures. |
| `vsphere_cluster_check_errors` | Number of failed cluster-level checks that the vSphere Problem Detector Operator performed. For example, a value of `1` indicates that one cluster-level check failed. |
| `vsphere_esxi_version_total` | Counts the number of ESXi hosts with a specific version. Note that if a host runs more than one node, the vSphere Problem Detector Operator counts the host only once. |
| `vsphere_node_check_total` | Cumulative number of node-level checks that the vSphere Problem Detector Operator performed. This count includes both successes and failures. |
| `vsphere_node_check_errors` | Counts the number of failed node-level checks that the vSphere Problem Detector Operator performed. For example, a value of `1` indicates that one node-level check failed. |
| `vsphere_node_hw_version_total` | Number of vSphere nodes with a specific hardware version. |
| `vsphere_vcenter_info` | Information about the vSphere vCenter Server. |

Metrics exposed by the vSphere Problem Detector Operator

# Additional resources

- [About OpenShift Container Platform monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/about_monitoring/about-ocp-monitoring)
