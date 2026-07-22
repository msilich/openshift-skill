<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

When opening a support case, it is helpful to provide debugging information about your cluster to Red Hat Support.

It is recommended to provide:

- [Data gathered using the `oc adm must-gather` command](gathering-cluster-data.md#support_gathering_data_gathering-cluster-data)

- The [unique cluster ID](gathering-cluster-data.md#support-get-cluster-id_gathering-cluster-data)

# About the must-gather tool

The `oc adm must-gather` CLI command collects the information from your cluster that is most likely needed for debugging issues, including:

- Resource definitions

- Service logs

By default, the `oc adm must-gather` command uses the default plugin image and writes into `./must-gather.local`.

Alternatively, you can collect specific information by running the command with the appropriate arguments as described in the following sections:

- To collect data related to one or more specific features, use the `--image` argument with an image, as listed in a following section.

  For example:

  ``` terminal
  $ oc adm must-gather \
    --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v4.20.21
  ```

  - To collect the audit logs, use the `-- /usr/bin/gather_audit_logs` argument, as described in a following section.

    For example:

    ``` terminal
    $ oc adm must-gather -- /usr/bin/gather_audit_logs
    ```

    <div class="note">

    <div class="title">

    </div>

    - Audit logs are not collected as part of the default set of information to reduce the size of the files.

    - On a Windows operating system, install the `cwRsync` client and add to the `PATH` variable for use with the `oc rsync` command.

    </div>

When you run `oc adm must-gather`, a new pod with a random name is created in a new project on the cluster. The data is collected on that pod and saved in a new directory that starts with `must-gather.local` in the current working directory.

For example:

``` terminal
NAMESPACE                      NAME                 READY   STATUS      RESTARTS      AGE
...
openshift-must-gather-5drcj    must-gather-bklx4    2/2     Running     0             72s
openshift-must-gather-5drcj    must-gather-s8sdh    2/2     Running     0             72s
...
```

Optionally, you can run the `oc adm must-gather` command in a specific namespace by using the `--run-namespace` option.

For example:

``` terminal
$ oc adm must-gather --run-namespace <namespace> \
  --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v4.20.21
```

## Gathering data about your cluster for Red Hat Support

You can gather debugging information about your cluster by using the `oc adm must-gather` CLI command.

If you are gathering information to debug a self-managed hosted cluster, see "Gathering information to troubleshoot hosted control planes".

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- The OpenShift Container Platform CLI (`oc`) is installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the directory where you want to store the `must-gather` data.

    > [!NOTE]
    > If your cluster is in a disconnected environment, you must take additional steps. If your mirror registry has a trusted CA, you must first add the trusted CA to the cluster. For all clusters in disconnected environments, you must import the default `must-gather` image as an image stream.
    >
    > ``` terminal
    > $ oc import-image is/must-gather -n openshift
    > ```

2.  Run the `oc adm must-gather` command:

    ``` terminal
    $ oc adm must-gather
    ```

    > [!IMPORTANT]
    > If you are in a disconnected environment, use the `--image` flag as part of must-gather and point to the payload image.

    > [!NOTE]
    > Because this command picks a random control plane node by default, the pod might be scheduled to a control plane node that is in the `NotReady` and `SchedulingDisabled` state.

    1.  If this command fails, for example, if you cannot schedule a pod on your cluster, then use the `oc adm inspect` command to gather information for particular resources.

        > [!NOTE]
        > Contact Red Hat Support for the recommended resources to gather.

3.  Create a compressed file from the `must-gather` directory that was just created in your working directory. Make sure you provide the date and cluster ID for the unique must-gather data. For more information about how to find the cluster ID, see [How to find the cluster-id or name on OpenShift cluster](https://access.redhat.com/solutions/5280291). For example, on a computer that uses a Linux operating system, run the following command:

    ``` terminal
    $ tar cvaf must-gather-`date +"%m-%d-%Y-%H-%M-%S"`-<cluster_id>.tar.gz <must_gather_local_dir>
    ```

    - Replace `<must_gather_local_dir>` with the actual directory name.

4.  Attach the compressed file to your support case on the [the **Customer Support** page](https://access.redhat.com/support/cases/#/case/list) of the Red Hat Customer Portal.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Gathering information to troubleshoot hosted control planes](../hosted_control_planes/hcp-troubleshooting.md#hosted-control-planes-troubleshooting_hcp-troubleshooting)

</div>

## Must-gather flags

The flags listed in the following table are available to use with the `oc adm must-gather` command.

| Flag | Example command | Description |
|----|----|----|
| `--all-images` | `oc adm must-gather --all-images=false` | Collect `must-gather` data using the default image for all Operators on the cluster that are annotated with `operators.openshift.io/must-gather-image`. |
| `--dest-dir` | `oc adm must-gather --dest-dir='<directory_name>'` | Set a specific directory on the local machine where the gathered data is written. |
| `--host-network` | `oc adm must-gather --host-network=false` | Run `must-gather` pods as `hostNetwork: true`. Relevant if a specific command and image needs to capture host-level data. |
| `--image` | `oc adm must-gather --image=[<plugin_image>]` | Specify a `must-gather` plugin image to run. If not specified, OpenShift Container Platform’s default `must-gather` image is used. |
| `--image-stream` | `oc adm must-gather --image-stream=[<image_stream>]` | Specify an\`\<image_stream\>\` using a namespace or name:tag value containing a `must-gather` plugin image to run. |
| `--node-name` | `oc adm must-gather --node-name='<node>'` | Set a specific node to use. If not specified, by default a random master is used. |
| `--node-selector` | `oc adm must-gather --node-selector='<node_selector_name>'` | Set a specific node selector to use. Only relevant when specifying a command and image which needs to capture data on a set of cluster nodes simultaneously. |
| `--run-namespace` | `oc adm must-gather --run-namespace='<namespace>'` | An existing privileged namespace where `must-gather` pods should run. If not specified, a temporary namespace is generated. |
| `--since` | `oc adm must-gather --since=<time>` | Only return logs newer than the specified duration. Defaults to all logs. Plugins are encouraged but not required to support this. Only one `since-time` or `since` may be used. |
| `--since-time` | `oc adm must-gather --since-time='<date_and_time>'` | Only return logs after a specific date and time, expressed in ([RFC3339](https://www.rfc-editor.org/rfc/rfc3339)) format. Defaults to all logs. Plugins are encouraged but not required to support this. Only one `since-time` or `since` may be used. |
| `--source-dir` | `oc adm must-gather --source-dir='/<directory_name>/'` | Set the specific directory on the pod where you copy the gathered data from. |
| `--timeout` | `oc adm must-gather --timeout='<time>'` | The length of time to gather data before timing out, expressed as seconds, minutes, or hours, for example, 3s, 5m, or 2h. Time specified must be higher than zero. Defaults to 10 minutes if not specified. |
| `--volume-percentage` | `oc adm must-gather --volume-percentage=<percent>` | Specify maximum percentage of pod’s allocated volume that can be used for `must-gather`. If this limit is exceeded, `must-gather` stops gathering, but still copies gathered data. Defaults to 30% if not specified. |

OpenShift Container Platform flags for `oc adm must-gather`

## Gathering data about specific features

You can gather debugging information about specific features by using the `oc adm must-gather` CLI command with the `--image` or `--image-stream` argument. The `must-gather` tool supports multiple images, so you can gather data about more than one feature by running a single command.

<table>
<caption>Supported must-gather images</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Image</th>
<th style="text-align: left;">Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v4.20.21</code></p></td>
<td style="text-align: left;"><p>Data collection for OpenShift Virtualization.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/openshift-serverless-1/svls-must-gather-rhel8</code></p></td>
<td style="text-align: left;"><p>Data collection for OpenShift Serverless.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/openshift-service-mesh/istio-must-gather-rhel8:&lt;installed_version_service_mesh&gt;</code></p></td>
<td style="text-align: left;"><p>Data collection for Red Hat OpenShift Service Mesh.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/multicluster-engine/must-gather-rhel8</code></p></td>
<td style="text-align: left;"><p>Data collection for hosted control planes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/rhmtc/openshift-migration-must-gather-rhel8:v&lt;installed_version_migration_toolkit&gt;</code></p></td>
<td style="text-align: left;"><p>Data collection for the Migration Toolkit for Containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/odf4/odf-must-gather-rhel9:v&lt;installed_version_ODF&gt;</code></p></td>
<td style="text-align: left;"><p>Data collection for Red Hat OpenShift Data Foundation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/openshift-logging/cluster-logging-rhel9-operator:v&lt;installed_version_logging&gt;</code></p></td>
<td style="text-align: left;"><p>Data collection for logging.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>quay.io/netobserv/must-gather</code></p></td>
<td style="text-align: left;"><p>Data collection for the Network Observability Operator.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/openshift4/ose-local-storage-mustgather-rhel9:v&lt;installed_version_LSO&gt;</code></p></td>
<td style="text-align: left;"><p>Data collection for Local Storage Operator.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/openshift-sandboxed-containers/osc-must-gather-rhel8:v&lt;installed_version_sandboxed_containers&gt;</code></p></td>
<td style="text-align: left;"><p>Data collection for OpenShift sandboxed containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/workload-availability/node-healthcheck-must-gather-rhel8:v&lt;installed_version_NHC&gt;</code></p></td>
<td style="text-align: left;"><p>Data collection for the Red Hat Workload Availability Operators, including the Self Node Remediation (SNR) Operator, the Fence Agents Remediation (FAR) Operator, the Machine Deletion Remediation (MDR) Operator, the Node Health Check (NHC) Operator, and the Node Maintenance Operator (NMO).</p>
<p>Use this image if your NHC Operator version is <strong>earlier than 0.9.0</strong>.</p>
<p>For more information, see the "Gathering data" section for the specific Operator in <a href="https://docs.redhat.com/en/documentation/workload_availability_for_red_hat_openshift/latest/html/remediation_fencing_and_maintenance/index">Remediation, fencing, and maintenance</a> (Workload Availability for Red Hat OpenShift documentation).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/workload-availability/node-healthcheck-must-gather-rhel9:v&lt;installed_version_NHC&gt;</code></p></td>
<td style="text-align: left;"><p>Data collection for the Red Hat Workload Availability Operators, including the Self Node Remediation (SNR) Operator, the Fence Agents Remediation (FAR) Operator, the Machine Deletion Remediation (MDR) Operator, the Node Health Check (NHC) Operator, and the Node Maintenance Operator (NMO).</p>
<p>Use this image if your NHC Operator version is <strong>0.9.0. or later</strong>.</p>
<p>For more information, see the "Gathering data" section for the specific Operator in <a href="https://docs.redhat.com/en/documentation/workload_availability_for_red_hat_openshift/latest/html/remediation_fencing_and_maintenance/index">Remediation, fencing, and maintenance</a> (Workload Availability for Red Hat OpenShift documentation).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/numaresources/numaresources-must-gather-rhel9:v&lt;installed-version-nro&gt;</code></p></td>
<td style="text-align: left;"><p>Data collection for the NUMA Resources Operator (NRO).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/openshift4/ptp-must-gather-rhel8:v&lt;installed-version-ptp&gt;</code></p></td>
<td style="text-align: left;"><p>Data collection for the PTP Operator.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/openshift-gitops-1/must-gather-rhel8:v&lt;installed_version_GitOps&gt;</code></p></td>
<td style="text-align: left;"><p>Data collection for Red Hat OpenShift GitOps.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/openshift4/ose-secrets-store-csi-mustgather-rhel9:v&lt;installed_version_secret_store&gt;</code></p></td>
<td style="text-align: left;"><p>Data collection for the Secrets Store CSI Driver Operator.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/lvms4/lvms-must-gather-rhel9:v&lt;installed_version_LVMS&gt;</code></p></td>
<td style="text-align: left;"><p>Data collection for the LVM Operator.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>registry.redhat.io/compliance/openshift-compliance-must-gather-rhel8:&lt;digest-version&gt;</code></p></td>
<td style="text-align: left;"><p>Data collection for the Compliance Operator.</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> To determine the latest version for an OpenShift Container Platform component’s image, see the [OpenShift Operator Life Cycles](https://access.redhat.com/support/policy/updates/openshift_operators) web page on the Red Hat Customer Portal.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- The OpenShift Container Platform CLI (`oc`) is installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the directory where you want to store the `must-gather` data.

2.  Run the `oc adm must-gather` command with one or more `--image` or `--image-stream` arguments.

    <div class="note">

    <div class="title">

    </div>

    - To collect the default `must-gather` data in addition to specific feature data, add the `--image-stream=openshift/must-gather` argument.

    - For information on gathering data about the Custom Metrics Autoscaler, see the Additional resources section that follows.

    </div>

    For example, the following command gathers both the default cluster data and information specific to OpenShift Virtualization:

    ``` terminal
    $ oc adm must-gather \
      --image-stream=openshift/must-gather \
      --image=registry.redhat.io/container-native-virtualization/cnv-must-gather-rhel9:v4.20.21
    ```

    - The default OpenShift Container Platform `must-gather` image

    - The must-gather image for OpenShift Virtualization

      You can use the `must-gather` tool with additional arguments to gather data that is specifically related to OpenShift Logging and the Red Hat OpenShift Logging Operator in your cluster. For OpenShift Logging, run the following command:

      ``` terminal
      $ oc adm must-gather --image=$(oc -n openshift-logging get deployment.apps/cluster-logging-operator \
        -o jsonpath='{.spec.template.spec.containers[?(@.name == "cluster-logging-operator")].image}')
      ```

      <div class="example">

      <div class="title">

      Example `must-gather` output for OpenShift Logging

      </div>

      ``` terminal
      ├── cluster-logging
      │  ├── clo
      │  │  ├── cluster-logging-operator-74dd5994f-6ttgt
      │  │  ├── clusterlogforwarder_cr
      │  │  ├── cr
      │  │  ├── csv
      │  │  ├── deployment
      │  │  └── logforwarding_cr
      │  ├── collector
      │  │  ├── fluentd-2tr64
      │  ├── eo
      │  │  ├── csv
      │  │  ├── deployment
      │  │  └── elasticsearch-operator-7dc7d97b9d-jb4r4
      │  ├── es
      │  │  ├── cluster-elasticsearch
      │  │  │  ├── aliases
      │  │  │  ├── health
      │  │  │  ├── indices
      │  │  │  ├── latest_documents.json
      │  │  │  ├── nodes
      │  │  │  ├── nodes_stats.json
      │  │  │  └── thread_pool
      │  │  ├── cr
      │  │  ├── elasticsearch-cdm-lp8l38m0-1-794d6dd989-4jxms
      │  │  └── logs
      │  │     ├── elasticsearch-cdm-lp8l38m0-1-794d6dd989-4jxms
      │  ├── install
      │  │  ├── co_logs
      │  │  ├── install_plan
      │  │  ├── olmo_logs
      │  │  └── subscription
      │  └── kibana
      │     ├── cr
      │     ├── kibana-9d69668d4-2rkvz
      ├── cluster-scoped-resources
      │  └── core
      │     ├── nodes
      │     │  ├── ip-10-0-146-180.eu-west-1.compute.internal.yaml
      │     └── persistentvolumes
      │        ├── pvc-0a8d65d9-54aa-4c44-9ecc-33d9381e41c1.yaml
      ├── event-filter.html
      ├── gather-debug.log
      └── namespaces
         ├── openshift-logging
         │  ├── apps
         │  │  ├── daemonsets.yaml
         │  │  ├── deployments.yaml
         │  │  ├── replicasets.yaml
         │  │  └── statefulsets.yaml
         │  ├── batch
         │  │  ├── cronjobs.yaml
         │  │  └── jobs.yaml
         │  ├── core
         │  │  ├── configmaps.yaml
         │  │  ├── endpoints.yaml
         │  │  ├── events
         │  │  │  ├── elasticsearch-im-app-1596020400-gm6nl.1626341a296c16a1.yaml
         │  │  │  ├── elasticsearch-im-audit-1596020400-9l9n4.1626341a2af81bbd.yaml
         │  │  │  ├── elasticsearch-im-infra-1596020400-v98tk.1626341a2d821069.yaml
         │  │  │  ├── elasticsearch-im-app-1596020400-cc5vc.1626341a3019b238.yaml
         │  │  │  ├── elasticsearch-im-audit-1596020400-s8d5s.1626341a31f7b315.yaml
         │  │  │  ├── elasticsearch-im-infra-1596020400-7mgv8.1626341a35ea59ed.yaml
         │  │  ├── events.yaml
         │  │  ├── persistentvolumeclaims.yaml
         │  │  ├── pods.yaml
         │  │  ├── replicationcontrollers.yaml
         │  │  ├── secrets.yaml
         │  │  └── services.yaml
         │  ├── openshift-logging.yaml
         │  ├── pods
         │  │  ├── cluster-logging-operator-74dd5994f-6ttgt
         │  │  │  ├── cluster-logging-operator
         │  │  │  │  └── cluster-logging-operator
         │  │  │  │     └── logs
         │  │  │  │        ├── current.log
         │  │  │  │        ├── previous.insecure.log
         │  │  │  │        └── previous.log
         │  │  │  └── cluster-logging-operator-74dd5994f-6ttgt.yaml
         │  │  ├── cluster-logging-operator-registry-6df49d7d4-mxxff
         │  │  │  ├── cluster-logging-operator-registry
         │  │  │  │  └── cluster-logging-operator-registry
         │  │  │  │     └── logs
         │  │  │  │        ├── current.log
         │  │  │  │        ├── previous.insecure.log
         │  │  │  │        └── previous.log
         │  │  │  ├── cluster-logging-operator-registry-6df49d7d4-mxxff.yaml
         │  │  │  └── mutate-csv-and-generate-sqlite-db
         │  │  │     └── mutate-csv-and-generate-sqlite-db
         │  │  │        └── logs
         │  │  │           ├── current.log
         │  │  │           ├── previous.insecure.log
         │  │  │           └── previous.log
         │  │  ├── elasticsearch-cdm-lp8l38m0-1-794d6dd989-4jxms
         │  │  ├── elasticsearch-im-app-1596030300-bpgcx
         │  │  │  ├── elasticsearch-im-app-1596030300-bpgcx.yaml
         │  │  │  └── indexmanagement
         │  │  │     └── indexmanagement
         │  │  │        └── logs
         │  │  │           ├── current.log
         │  │  │           ├── previous.insecure.log
         │  │  │           └── previous.log
         │  │  ├── fluentd-2tr64
         │  │  │  ├── fluentd
         │  │  │  │  └── fluentd
         │  │  │  │     └── logs
         │  │  │  │        ├── current.log
         │  │  │  │        ├── previous.insecure.log
         │  │  │  │        └── previous.log
         │  │  │  ├── fluentd-2tr64.yaml
         │  │  │  └── fluentd-init
         │  │  │     └── fluentd-init
         │  │  │        └── logs
         │  │  │           ├── current.log
         │  │  │           ├── previous.insecure.log
         │  │  │           └── previous.log
         │  │  ├── kibana-9d69668d4-2rkvz
         │  │  │  ├── kibana
         │  │  │  │  └── kibana
         │  │  │  │     └── logs
         │  │  │  │        ├── current.log
         │  │  │  │        ├── previous.insecure.log
         │  │  │  │        └── previous.log
         │  │  │  ├── kibana-9d69668d4-2rkvz.yaml
         │  │  │  └── kibana-proxy
         │  │  │     └── kibana-proxy
         │  │  │        └── logs
         │  │  │           ├── current.log
         │  │  │           ├── previous.insecure.log
         │  │  │           └── previous.log
         │  └── route.openshift.io
         │     └── routes.yaml
         └── openshift-operators-redhat
            ├── ...
      ```

      </div>

3.  Run the `oc adm must-gather` command with one or more `--image` or `--image-stream` arguments. For example, the following command gathers both the default cluster data and information specific to KubeVirt:

    ``` terminal
    $ oc adm must-gather \
     --image-stream=openshift/must-gather \
     --image=quay.io/kubevirt/must-gather
    ```

    - The default OpenShift Container Platform `must-gather` image

    - The must-gather image for KubeVirt

4.  Create a compressed file from the `must-gather` directory that was just created in your working directory. Make sure you provide the date and cluster ID for the unique must-gather data. For more information about how to find the cluster ID, see [How to find the cluster-id or name on OpenShift cluster](https://access.redhat.com/solutions/5280291). For example, on a computer that uses a Linux operating system, run the following command:

    ``` terminal
    $ tar cvaf must-gather-`date +"%m-%d-%Y-%H-%M-%S"`-<cluster_id>.tar.gz <must_gather_local_dir>
    ```

    - Replace `<must_gather_local_dir>` with the actual directory name.

5.  Attach the compressed file to your support case on the [the **Customer Support** page](https://access.redhat.com/support/cases/#/case/list) of the Red Hat Customer Portal.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Gathering debugging data](../nodes/cma/nodes-cma-autoscaling-custom.md#nodes-cma-autoscaling-custom-gather) for the Custom Metrics Autoscaler.

- [Red Hat OpenShift Container Platform Life Cycle Policy](https://access.redhat.com/support/policy/updates/openshift)

</div>

## Gathering network logs

You can gather network logs on all nodes in a cluster.

<div>

<div class="title">

Procedure

</div>

1.  Run the `oc adm must-gather` command with `-- gather_network_logs`:

    ``` terminal
    $ oc adm must-gather -- gather_network_logs
    ```

    > [!NOTE]
    > By default, the `must-gather` tool collects the OVN `nbdb` and `sbdb` databases from all of the nodes in the cluster. Adding the `-- gather_network_logs` option to include additional logs that contain OVN-Kubernetes transactions for OVN `nbdb` database.

2.  Create a compressed file from the `must-gather` directory that was just created in your working directory. Make sure you provide the date and cluster ID for the unique must-gather data. For more information about how to find the cluster ID, see [How to find the cluster-id or name on OpenShift cluster](https://access.redhat.com/solutions/5280291). For example, on a computer that uses a Linux operating system, run the following command:

    ``` terminal
    $ tar cvaf must-gather-`date +"%m-%d-%Y-%H-%M-%S"`-<cluster_id>.tar.gz <must_gather_local_dir>
    ```

    - Replace `<must_gather_local_dir>` with the actual directory name.

3.  Attach the compressed file to your support case on the [the **Customer Support** page](https://access.redhat.com/support/cases/#/case/list) of the Red Hat Customer Portal.

</div>

## Changing the must-gather storage limit

When using the `oc adm must-gather` command to collect data the default maximum storage for the information is 30% of the storage capacity of the container. After the 30% limit is reached the container is killed and the gathering process stops. Information already gathered is downloaded to your local storage. To run the must-gather command again, you need either a container with more storage capacity or to adjust the maximum volume percentage.

If the container reaches the storage limit, an error message similar to the following example is generated.

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
Disk usage exceeds the volume percentage of 30% for mounted directory. Exiting...
```

</div>

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- The OpenShift CLI (`oc`) is installed.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the `oc adm must-gather` command with the `volume-percentage` flag. The new value cannot exceed 100.

  ``` terminal
  $ oc adm must-gather --volume-percentage <storage_percentage>
  ```

</div>

# About Support Log Gather

Support Log Gather Operator builds on the functionality of the traditional `must-gather` tool to automate the collection of debugging data. It streamlines troubleshooting by packaging the collected information into a single `.tar` file and automatically uploading it to the specified Red Hat Support case.

> [!IMPORTANT]
> Support Log Gather is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

The key features of Support Log Gather include the following:

- **No administrator privileges required**: Enables you to collect and upload logs without needing elevated permissions, making it easier for non-administrators to gather data securely.

- **Simplified log collection**: Collects debugging data from the cluster, such as resource definitions and service logs.

- **Configurable data upload**: Provides configuration options to either automatically upload the `.tar` file to a support case, or store it locally for manual upload.

## Installing Support Log Gather by using the web console

You can use the web console to install the Support Log Gather.

> [!IMPORTANT]
> Support Log Gather is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have access to the OpenShift Container Platform web console.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Navigate to **Ecosystem** → **Software Catalog**.

3.  In the filter box, enter **Support Log Gather**.

4.  Select **Support Log Gather**.

5.  From **Version** list, select the Support Log Gather version, and click **Install**.

6.  On the **Install Operator** page, configure the installation settings:

    1.  Choose the **Installed Namespace** for the Operator.

        The default Operator namespace is `must-gather-operator`. The `must-gather-operator` namespace is created automatically if it does not exist.

    2.  Select an **Update approval** strategy:

        - Select **Automatic** to have the Operator Lifecycle Manager (OLM) update the Operator automatically when a newer version is available.

        - Select **Manual** if Operator updates must be approved by a user with appropriate credentials.

    3.  Click **Install**.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the Operator is installed successfully:

    1.  Navigate to **Ecosystem** → **Software Catalog**.

    2.  Verify that **Support Log Gather** is listed with a **Status** of **Succeeded** in the `must-gather-operator` namespace.

2.  Verify that Support Log Gather pods are running:

    1.  Navigate to **Workloads** → **Pods**

    2.  Verify that the status of the Support Log Gather pods is **Running**.

        You can use the Support Log Gather only after the pods are up and running.

</div>

## Installing Support Log Gather by using the CLI

To enable automated log collection for support cases, you can install Support Log Gather from the command-line interface (CLI).

> [!IMPORTANT]
> Support Log Gather is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a new project named `must-gather-operator` by running the following command:

    ``` terminal
    $ oc new-project must-gather-operator
    ```

2.  Create an `OperatorGroup` object:

    1.  Create a YAML file, for example, `operatorGroup.yaml`, that defines the `OperatorGroup` object:

        ``` yaml
        apiVersion: operators.coreos.com/v1
        kind: OperatorGroup
        metadata:
          name: must-gather-operator
          namespace: must-gather-operator
        spec: {}
        ```

    2.  Create the `OperatorGroup` object by running the following command:

        ``` terminal
        $ oc create -f operatorGroup.yaml
        ```

3.  Create a `Subscription` object:

    1.  Create a YAML file, for example, `subscription.yaml`, that defines the `Subscription` object:

        ``` yaml
        apiVersion: operators.coreos.com/v1alpha1
        kind: Subscription
        metadata:
          name: support-log-gather-operator
          namespace: must-gather-operator
        spec:
          channel: tech-preview
          name: support-log-gather-operator
          source: redhat-operators
          sourceNamespace: openshift-marketplace
          installPlanApproval: Automatic
        ```

    2.  Create the `Subscription` object by running the following command:

        ``` terminal
        $ oc create -f subscription.yaml
        ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify the status of the pods in the Operator namespace by running the following command.

    ``` terminal
    $ oc get pods
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                                              READY   STATUS      RESTARTS   AGE
    must-gather-operator-657fc74d64-2gg2w                             1/1     Running     0          13m
    ```

    </div>

    The status of all the pods must be `Running`.

2.  Verify that the subscription is created by running the following command:

    ``` terminal
    $ oc get subscription -n must-gather-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                          PACKAGE                       SOURCE            CHANNEL
    support-log-gather-operator   support-log-gather-operator   redhat-operators  tech-preview
    ```

    </div>

3.  Verify that the Operator is installed by running the following command:

    ``` terminal
    $ oc get csv -n must-gather-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                  DISPLAY                VERSION   REPLACES   PHASE
    support-log-gather-operator.v4.20.0   support log gather     4.20.0               Succeeded
    ```

    </div>

</div>

## Configuring a Support Log Gather instance

You must create a `MustGather` custom resource (CR) from the command-line interface (CLI) to automate the collection of diagnostic data from your cluster. This process also automatically uploads the data to a Red Hat Support case.

> [!IMPORTANT]
> Support Log Gather is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`) tool.

- You have installed Support Log Gather in your cluster.

- You have a Red Hat Support case ID.

- You have created a Kubernetes secret containing your Red Hat Customer Portal credentials. The secret must contain a username field and a password field.

- You have created a service account.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file for the `MustGather` CR, such as `support-log-gather.yaml`, that contains the following basic configuration::

    <div class="formalpara">

    <div class="title">

    Example `support-log-gather.yaml`

    </div>

    ``` yaml
    apiVersion: operator.openshift.io/v1alpha1
    kind: MustGather
    metadata:
      name: example-mg
      namespace: must-gather-operator
    spec:
      serviceAccountName: must-gather-operator
      audit: true
      proxyConfig:
        httpProxy: "http://proxy.example.com:8080"
        httpsProxy: "https://proxy.example.com:8443"
        noProxy: ".example.com,localhost"
      mustGatherTimeout: "1h30m9s"
      uploadTarget:
        type: SFTP
        sftp:
          caseID: "04230315"
          caseManagementAccountSecretRef:
            name: mustgather-creds
          host: "sftp.access.redhat.com"
      retainResourcesOnCompletion: true
      storage:
        type: PersistentVolume
        persistentVolume:
          claim:
            name: mustgather-pvc
          subPath: must-gather-bundles/case-04230315
    ```

    </div>

    For more information on the configuration parameters, see "Configuration parameters for MustGather custom resource".

2.  Create the `MustGather` object by running the following command:

    ``` terminal
    $ oc create -f support-log-gather.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the `MustGather` CR was created by running the following command:

    ``` terminal
    $ oc get mustgather
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME          AGE
    example-mg    7s
    ```

    </div>

2.  Verify the status of the pods in the Operator namespace by running the following command.

    ``` terminal
    $ oc get pods
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                                              READY   STATUS      RESTARTS   AGE
    must-gather-operator-657fc74d64-2gg2w                             1/1     Running     0          13m
    example-mg-gk8m8                                                  2/2     Running     0          13s
    ```

    </div>

    A new pod with a name based on the `MustGather` CR must be created. The status of all the pods must be `Running`.

3.  To monitor the progress of the file upload, view the logs of the upload container in the job pod by running the following command:

    ``` terminal
    oc logs -f pod/example-mg-gk8m8 -c upload
    ```

    When successful, the process must create an archive and upload it to the Red Hat Secure File Transfer Protocol (SFTP) server for the specified case.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Understanding and creating service accounts](../authentication/understanding-and-creating-service-accounts.md#understanding-and-creating-service-accounts)

</div>

## Configuration parameters for MustGather custom resource

You can manage your `MustGather` custom resource (CR) by creating a YAML file that specifies the parameters for data collection and the upload process. The following table provides an overview of the parameters that you can configure in the `MustGather` CR.

| Parameter name | Description | Type |
|----|----|----|
| `spec.audit` | Optional: Specifies whether to collect audit logs. The valid values are `true` and `false`. The default value is `false`. | `boolean` |
| `spec.mustGatherTimeout` | Optional: Specifies the time limit for the `must-gather` command to complete. | The value must be a floating-point number with a time unit. The valid units are `s` (seconds), `m` (minutes), or `h` (hours). By default, no time is limit set. |
| `spec.proxyConfig` | Optional: Defines the proxy configuration to be used. The default value is set to the cluster-level proxy configuration. | `Object` |
| `spec.proxyConfig.httpProxy` | Specifies the URL of the proxy for HTTP requests. | URL |
| `spec.proxyConfig.httpsProxy` | Specifies the URL of the proxy for HTTPS requests. |  |
| `spec.proxyConfig.noProxy` | Specifies a comma-separated list of domains for which the proxy must not be used. | List of URLs |
| `spec.retainResourcesOnCompletion` | Optional: Specifies whether to retain the `must-gather` job and its related resources after the completion of data collection. The valid values are `true` and `false`. The default value is `false`. | `boolean` |
| `spec.serviceAccountName` | Optional: Specifies the name of the service account. The default value is `default`. | `string` |
| `spec.storage` | Optional: Defines the storage configuration for the `must-gather` bundle. | `Object` |
| `spec.storage.persistentVolume` | Defines the details of the persistent volume. | `Object` |
| `spec.storage.persistentVolume.claim` | Defines the details of the persistent volume claim (PVC). | `Object` |
| `spec.storage.persistentVolume.claim.name` | Specifies the name of the PVC to be used for storage. | `string` |
| `spec.storage.persistentVolume.subPath` | Optional: Specifies the path within the PVC to store the bundle. | `string` |
| `spec.storage.type` | Defines the type of storage. The only supported value is `PersistentVolume`. | `string` |
| `spec.uploadTarget` | Optional: Defines the upload location for the `must-gather` bundle. | `Object` |
| `spec.uploadTarget.host` | Optional: Specifies the destination server for the bundle upload. By default, the bundle is uploaded to `sftp.access.redhat.com`. | By default, the bundle is uploaded to `sftp.access.redhat.com`. |
| `spec.uploadTarget.sftp.caseID` | Specifies the Red Hat Support case ID for which the diagnostic data is collected. | `string` |
| `spec.uploadTarget.sftp.caseManagementAccountSecretRef` | Defines the credentials required for authenticating and uploading the files to the Red Hat Customer Portal support case. The value must contain a `username` and `password` field. | `Object` |
| `spec.uploadTarget.sftp.caseManagementAccountSecretRef.name` | Specifies the name of the Kubernetes secret that contains the credentials. | `string` |
| `spec.uploadTarget.sftp.internalUser` | Optional: Specifies whether the user provided in the `caseManagementAccountSecretRef` is a Red Hat internal user. The valid values are `true` and `false`. The default value is `false`. | `boolean` |
| `spec.uploadTarget.type` | Specifies the type of upload location for the `must-gather` bundle. The only supported value is `SFTP`. | `string` |

> [!NOTE]
> If you do not specify `spec.uploadTarget` or `spec.storage`, the pod saves the data to an ephemeral volume and the data is permanently deleted when the pod terminates.

## Uninstalling Support Log Gather

You can uninstall the Support Log Gather by using the web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have access to the OpenShift Container Platform web console.

- The Support Log Gather is installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Uninstall the Support Log Gather Operator.

    1.  Navigate to **Ecosystem** → **Installed Operators**.

    2.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to the **Support Log Gather** entry and click **Uninstall Operator**.

    3.  In the confirmation dialog, click **Uninstall**.

</div>

## Removing Support Log Gather resources

Once you have uninstalled the Support Log Gather, you can remove the associated resources from your cluster.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have access to the OpenShift Container Platform web console.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Delete the component deployments in the must-gather-operator namespace.:

    1.  Click the **Project** drop-down menu to view the list of all available projects, and select the **must-gather-operator** project.

    2.  Navigate to **Workloads** → **Deployments**.

    3.  Select the deployment that you want to delete.

    4.  Click the **Actions** drop-down menu, and select **Delete Deployment**.

    5.  In the confirmation dialog box, click **Delete** to delete the deployment.

    6.  Alternatively, delete deployments of the components present in the `must-gather-operator` namespace by using the command-line interface (CLI).

        ``` terminal
        $ oc delete deployment -n must-gather-operator -l operators.coreos.com/support-log-gather-operator.must-gather-operator
        ```

3.  Optional: Remove the custom resource definitions (CRDs) that were installed by the Support Log Gather:

    1.  Navigate to **Administration** → **CustomResourceDefinitions**.

    2.  Enter `MustGather` in the **Name** field to filter the CRDs.

    3.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to each of the following CRDs, and select **Delete Custom Resource Definition**:

        - `MustGather`

4.  Optional: Remove the `must-gather-operator` namespace.

    1.  Navigate to **Administration** → **Namespaces**.

    2.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to the **must-gather-operator** and select **Delete Namespace**.

    3.  In the confirmation dialog box, enter `must-gather-operator` and click **Delete**.

</div>

# Obtaining your cluster ID

When providing information to Red Hat Support, it is helpful to provide the unique identifier for your cluster. You can have your cluster ID autofilled by using the OpenShift Container Platform web console. You can also manually obtain your cluster ID by using the web console or the OpenShift CLI (`oc`).

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have access to the web console or the OpenShift CLI (`oc`) installed.

</div>

<div>

<div class="title">

Procedure

</div>

- To open a support case and have your cluster ID autofilled using the web console:

  1.  From the toolbar, navigate to **(?) Help** and select **Share Feedback** from the list.

  2.  Click **Open a support case** from the **Tell us about your experience** window.

- To manually obtain your cluster ID using the web console:

  1.  Navigate to **Home** → **Overview**.

  2.  The value is available in the **Cluster ID** field of the **Details** section.

- To obtain your cluster ID using the OpenShift CLI (`oc`), run the following command:

  ``` terminal
  $ oc get clusterversion -o jsonpath='{.items[].spec.clusterID}{"\n"}'
  ```

</div>

# About sosreport

`sosreport` is a tool that collects configuration details, system information, and diagnostic data from Red Hat Enterprise Linux (RHEL) and Red Hat Enterprise Linux CoreOS (RHCOS) systems. `sosreport` provides a standardized way to collect diagnostic information relating to a node, which can then be provided to Red Hat Support for issue diagnosis.

In some support interactions, Red Hat Support may ask you to collect a `sosreport` archive for a specific OpenShift Container Platform node. For example, it might sometimes be necessary to review system logs or other node-specific data that is not included within the output of `oc adm must-gather`.

# Generating a sosreport archive for an OpenShift Container Platform cluster node

The recommended way to generate a `sosreport` for an OpenShift Container Platform 4.17 cluster node is through a debug pod.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have SSH access to your hosts.

- You have installed the OpenShift CLI (`oc`).

- You have a Red Hat standard or premium Subscription.

- You have a Red Hat Customer Portal account.

- You have an existing Red Hat Support case ID.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Obtain a list of cluster nodes:

    ``` terminal
    $ oc get nodes
    ```

2.  Enter into a debug session on the target node. This step instantiates a debug pod called `<node_name>-debug`:

    ``` terminal
    $ oc debug node/my-cluster-node
    ```

    To enter into a debug session on the target node that is tainted with the `NoExecute` effect, add a toleration to a dummy namespace, and start the debug pod in the dummy namespace:

    ``` terminal
    $ oc new-project dummy
    ```

    ``` terminal
    $ oc patch namespace dummy --type=merge -p '{"metadata": {"annotations": { "scheduler.alpha.kubernetes.io/defaultTolerations": "[{\"operator\": \"Exists\"}]"}}}'
    ```

    ``` terminal
    $ oc debug node/my-cluster-node
    ```

3.  Set `/host` as the root directory within the debug shell. The debug pod mounts the host’s root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host’s executable paths:

    ``` terminal
    # chroot /host
    ```

    > [!NOTE]
    > OpenShift Container Platform 4.17 cluster nodes running Red Hat Enterprise Linux CoreOS (RHCOS) are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to access nodes using `ssh core@<node>.<cluster_name>.<base_domain>` instead.

4.  Start a `toolbox` container, which includes the required binaries and plugins to run `sosreport`:

    ``` terminal
    # toolbox
    ```

    > [!NOTE]
    > If an existing `toolbox` pod is already running, the `toolbox` command outputs `'toolbox-' already exists. Trying to start…​`. Remove the running toolbox container with `podman rm toolbox-` and spawn a new toolbox container, to avoid issues with `sosreport` plugins.

5.  Collect a `sosreport` archive.

    1.  Run the `sos report` command to collect necessary troubleshooting data on `crio` and `podman`:

        ``` terminal
        # sos report -k crio.all=on -k crio.logs=on  -k podman.all=on -k podman.logs=on
        ```

        - `-k` enables you to define `sosreport` plugin parameters outside of the defaults.

    2.  Optional: To include information on OVN-Kubernetes networking configurations from a node in your report, run the following command:

        ``` terminal
        # sos report --all-logs
        ```

    3.  Press **Enter** when prompted, to continue.

    4.  Provide the Red Hat Support case ID. `sosreport` adds the ID to the archive’s file name.

    5.  The `sosreport` output provides the archive’s location and checksum. The following sample output references support case ID `01234567`:

        ``` terminal
        Your sosreport has been generated and saved in:
          /host/var/tmp/sosreport-my-cluster-node-01234567-2020-05-28-eyjknxt.tar.xz

        The checksum is: 382ffc167510fd71b4f12a4f40b97a4e
        ```

        - The `sosreport` archive’s file path is outside of the `chroot` environment because the toolbox container mounts the host’s root directory at `/host`.

6.  Provide the `sosreport` archive to Red Hat Support for analysis, using one of the following methods.

    - Upload the file to an existing Red Hat support case.

      1.  Concatenate the `sosreport` archive by running the `oc debug node/<node_name>` command and redirect the output to a file. This command assumes you have exited the previous `oc debug` session:

          ``` terminal
          $ oc debug node/my-cluster-node -- bash -c 'cat /host/var/tmp/sosreport-my-cluster-node-01234567-2020-05-28-eyjknxt.tar.xz' > /tmp/sosreport-my-cluster-node-01234567-2020-05-28-eyjknxt.tar.xz
          ```

          - The debug container mounts the host’s root directory at `/host`. Reference the absolute path from the debug container’s root directory, including `/host`, when specifying target files for concatenation.

            > [!NOTE]
            > OpenShift Container Platform 4.17 cluster nodes running Red Hat Enterprise Linux CoreOS (RHCOS) are immutable and rely on Operators to apply cluster changes. Transferring a `sosreport` archive from a cluster node by using `scp` is not recommended. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to copy a `sosreport` archive from a node by running `scp core@<node>.<cluster_name>.<base_domain>:<file_path> <local_path>`.

      2.  Navigate to an existing support case within [the **Customer Support** page](https://access.redhat.com/support/cases/#/case/list) of the Red Hat Customer Portal.

      3.  Select **Attach files** and follow the prompts to upload the file.

</div>

# Querying bootstrap node journal logs

If you experience bootstrap-related issues, you can gather `bootkube.service` `journald` unit logs and container logs from the bootstrap node.

<div>

<div class="title">

Prerequisites

</div>

- You have SSH access to your bootstrap node.

- You have the fully qualified domain name of the bootstrap node.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Query `bootkube.service` `journald` unit logs from a bootstrap node during OpenShift Container Platform installation. Replace `<bootstrap_fqdn>` with the bootstrap node’s fully qualified domain name:

    ``` terminal
    $ ssh core@<bootstrap_fqdn> journalctl -b -f -u bootkube.service
    ```

    > [!NOTE]
    > The `bootkube.service` log on the bootstrap node outputs etcd `connection refused` errors, indicating that the bootstrap server is unable to connect to etcd on control plane nodes. After etcd has started on each control plane node and the nodes have joined the cluster, the errors should stop.

2.  Collect logs from the bootstrap node containers using `podman` on the bootstrap node. Replace `<bootstrap_fqdn>` with the bootstrap node’s fully qualified domain name:

    ``` terminal
    $ ssh core@<bootstrap_fqdn> 'for pod in $(sudo podman ps -a -q); do sudo podman logs $pod; done'
    ```

</div>

# Querying cluster node journal logs

You can gather `journald` unit logs and other logs within `/var/log` on individual cluster nodes.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

- Your API service is still functional.

- You have SSH access to your hosts.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Query `kubelet` `journald` unit logs from OpenShift Container Platform cluster nodes. The following example queries control plane nodes only:

    ``` terminal
    $ oc adm node-logs --role=master -u kubelet
    ```

    - `kubelet`: Replace as appropriate to query other unit logs.

2.  Collect logs from specific subdirectories under `/var/log/` on cluster nodes.

    1.  Retrieve a list of logs contained within a `/var/log/` subdirectory. The following example lists files in `/var/log/openshift-apiserver/` on all control plane nodes:

        ``` terminal
        $ oc adm node-logs --role=master --path=openshift-apiserver
        ```

    2.  Inspect a specific log within a `/var/log/` subdirectory. The following example outputs `/var/log/openshift-apiserver/audit.log` contents from all control plane nodes:

        ``` terminal
        $ oc adm node-logs --role=master --path=openshift-apiserver/audit.log
        ```

    3.  If the API is not functional, review the logs on each node using SSH instead. The following example tails `/var/log/openshift-apiserver/audit.log`:

        ``` terminal
        $ ssh core@<master-node>.<cluster_name>.<base_domain> sudo tail -f /var/log/openshift-apiserver/audit.log
        ```

        > [!NOTE]
        > OpenShift Container Platform 4.17 cluster nodes running Red Hat Enterprise Linux CoreOS (RHCOS) are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. Before attempting to collect diagnostic data over SSH, review whether the data collected by running `oc adm must gather` and other `oc` commands is sufficient instead. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to access nodes using `ssh core@<node>.<cluster_name>.<base_domain>`.

</div>

# Network trace methods

Collecting network traces, in the form of packet capture records, can assist Red Hat Support with troubleshooting network issues.

OpenShift Container Platform supports two ways of performing a network trace. Review the following table and choose the method that meets your needs.

<table>
<caption>Supported methods of collecting a network trace</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Method</th>
<th style="text-align: left;">Benefits and capabilities</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Collecting a host network trace</p></td>
<td style="text-align: left;"><p>You perform a packet capture for a duration that you specify on one or more nodes at the same time. The packet capture files are transferred from nodes to the client machine when the specified duration is met.</p>
<p>You can troubleshoot why a specific action triggers network communication issues. Run the packet capture, perform the action that triggers the issue, and use the logs to diagnose the issue.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Collecting a network trace from an OpenShift Container Platform node or container</p></td>
<td style="text-align: left;"><p>You perform a packet capture on one node or one container. You run the <code>tcpdump</code> command interactively, so you can control the duration of the packet capture.</p>
<p>You can start the packet capture manually, trigger the network communication issue, and then stop the packet capture manually.</p>
<p>This method uses the <code>cat</code> command and shell redirection to copy the packet capture data from the node or container to the client machine.</p></td>
</tr>
</tbody>
</table>

# Collecting a host network trace

Sometimes, troubleshooting a network-related issue is simplified by tracing network communication and capturing packets on multiple nodes at the same time.

You can use a combination of the `oc adm must-gather` command and the `registry.redhat.io/openshift4/network-tools-rhel8` container image to gather packet captures from nodes. Analyzing packet captures can help you troubleshoot network communication issues.

The `oc adm must-gather` command is used to run the `tcpdump` command in pods on specific nodes. The `tcpdump` command records the packet captures in the pods. When the `tcpdump` command exits, the `oc adm must-gather` command transfers the files with the packet captures from the pods to your client machine.

> [!TIP]
> The sample command in the following procedure demonstrates performing a packet capture with the `tcpdump` command. However, you can run any command in the container image that is specified in the `--image` argument to gather troubleshooting information from multiple nodes at the same time.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run a packet capture from the host network on some nodes by running the following command:

    ``` terminal
    $ oc adm must-gather \
        --dest-dir /tmp/captures \
        --source-dir '/tmp/tcpdump/' \
        --image registry.redhat.io/openshift4/network-tools-rhel8:latest \
        --node-selector 'node-role.kubernetes.io/worker' \
        --host-network=true \
        --timeout 30s \
        -- \
        tcpdump -i any \
        -w /tmp/tcpdump/%Y-%m-%dT%H:%M:%S.pcap -W 1 -G 300
    ```

    - The `--dest-dir` argument specifies that `oc adm must-gather` stores the packet captures in directories that are relative to `/tmp/captures` on the client machine. You can specify any writable directory.

    - When `tcpdump` is run in the debug pod that `oc adm must-gather` starts, the `--source-dir` argument specifies that the packet captures are temporarily stored in the `/tmp/tcpdump` directory on the pod.

    - The `--image` argument specifies a container image that includes the `tcpdump` command.

    - The `--node-selector` argument and example value specifies to perform the packet captures on the worker nodes. As an alternative, you can specify the `--node-name` argument instead to run the packet capture on a single node. If you omit both the `--node-selector` and the `--node-name` argument, the packet captures are performed on all nodes.

    - The `--host-network=true` argument is required so that the packet captures are performed on the network interfaces of the node.

    - The `--timeout` argument and value specify to run the debug pod for 30 seconds. If you do not specify the `--timeout` argument and a duration, the debug pod runs for 10 minutes.

    - The `-i any` argument for the `tcpdump` command specifies to capture packets on all network interfaces. As an alternative, you can specify a network interface name.

2.  Perform the action, such as accessing a web application, that triggers the network communication issue while the network trace captures packets.

3.  Review the packet capture files that `oc adm must-gather` transferred from the pods to your client machine:

    ``` text
    tmp/captures
    ├── event-filter.html
    ├── ip-10-0-192-217-ec2-internal
    │   └── registry-redhat-io-openshift4-network-tools-rhel8-sha256-bca...
    │       └── 2022-01-13T19:31:31.pcap
    ├── ip-10-0-201-178-ec2-internal
    │   └── registry-redhat-io-openshift4-network-tools-rhel8-sha256-bca...
    │       └── 2022-01-13T19:31:30.pcap
    ├── ip-...
    └── timestamp
    ```

    - The packet captures are stored in directories that identify the hostname, container, and file name. If you did not specify the `--node-selector` argument, then the directory level for the hostname is not present.

</div>

# Collecting a network trace from an OpenShift Container Platform node or container

When investigating potential network-related OpenShift Container Platform issues, Red Hat Support might request a network packet trace from a specific OpenShift Container Platform cluster node or from a specific container. The recommended method to capture a network trace in OpenShift Container Platform is through a debug pod.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

- You have an existing Red Hat Support case ID.

- You have a Red Hat standard or premium Subscription.

- You have a Red Hat Customer Portal account.

- You have SSH access to your hosts.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Obtain a list of cluster nodes:

    ``` terminal
    $ oc get nodes
    ```

2.  Enter into a debug session on the target node. This step instantiates a debug pod called `<node_name>-debug`:

    ``` terminal
    $ oc debug node/my-cluster-node
    ```

3.  Set `/host` as the root directory within the debug shell. The debug pod mounts the host’s root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host’s executable paths:

    ``` terminal
    # chroot /host
    ```

    > [!NOTE]
    > OpenShift Container Platform 4.17 cluster nodes running Red Hat Enterprise Linux CoreOS (RHCOS) are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to access nodes using `ssh core@<node>.<cluster_name>.<base_domain>` instead.

4.  From within the `chroot` environment console, obtain the node’s interface names:

    ``` terminal
    # ip ad
    ```

5.  Start a `toolbox` container, which includes the required binaries and plugins to run `sosreport`:

    ``` terminal
    # toolbox
    ```

    > [!NOTE]
    > If an existing `toolbox` pod is already running, the `toolbox` command outputs `'toolbox-' already exists. Trying to start…​`. To avoid `tcpdump` issues, remove the running toolbox container with `podman rm toolbox-` and spawn a new toolbox container.

6.  Initiate a `tcpdump` session on the cluster node and redirect output to a capture file. This example uses `ens5` as the interface name:

    ``` terminal
    $ tcpdump -nn -s 0 -i ens5 -w /host/var/tmp/my-cluster-node_$(date +%d_%m_%Y-%H_%M_%S-%Z).pcap
    ```

    - The `tcpdump` capture file’s path is outside of the `chroot` environment because the toolbox container mounts the host’s root directory at `/host`.

7.  If a `tcpdump` capture is required for a specific container on the node, follow these steps.

    1.  Determine the target container ID. The `chroot host` command precedes the `crictl` command in this step because the toolbox container mounts the host’s root directory at `/host`:

        ``` terminal
        # chroot /host crictl ps
        ```

    2.  Determine the container’s process ID. In this example, the container ID is `a7fe32346b120`:

        ``` terminal
        # chroot /host crictl inspect --output yaml a7fe32346b120 | grep 'pid' | awk '{print $2}'
        ```

    3.  Initiate a `tcpdump` session on the container and redirect output to a capture file. This example uses `49628` as the container’s process ID and `ens5` as the interface name. The `nsenter` command enters the namespace of a target process and runs a command in its namespace. because the target process in this example is a container’s process ID, the `tcpdump` command is run in the container’s namespace from the host:

        ``` terminal
        # nsenter -n -t 49628 -- tcpdump -nn -i ens5 -w /host/var/tmp/my-cluster-node-my-container_$(date +%d_%m_%Y-%H_%M_%S-%Z).pcap
        ```

        - The `tcpdump` capture file’s path is outside of the `chroot` environment because the toolbox container mounts the host’s root directory at `/host`.

8.  Provide the `tcpdump` capture file to Red Hat Support for analysis, using one of the following methods.

    - Upload the file to an existing Red Hat support case.

      1.  Concatenate the `sosreport` archive by running the `oc debug node/<node_name>` command and redirect the output to a file. This command assumes you have exited the previous `oc debug` session:

          ``` terminal
          $ oc debug node/my-cluster-node -- bash -c 'cat /host/var/tmp/my-tcpdump-capture-file.pcap' > /tmp/my-tcpdump-capture-file.pcap
          ```

          - The debug container mounts the host’s root directory at `/host`. Reference the absolute path from the debug container’s root directory, including `/host`, when specifying target files for concatenation.

            > [!NOTE]
            > OpenShift Container Platform 4.17 cluster nodes running Red Hat Enterprise Linux CoreOS (RHCOS) are immutable and rely on Operators to apply cluster changes. Transferring a `tcpdump` capture file from a cluster node by using `scp` is not recommended. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to copy a `tcpdump` capture file from a node by running `scp core@<node>.<cluster_name>.<base_domain>:<file_path> <local_path>`.

      2.  Navigate to an existing support case within [the **Customer Support** page](https://access.redhat.com/support/cases/#/case/list) of the Red Hat Customer Portal.

      3.  Select **Attach files** and follow the prompts to upload the file.

</div>

# Providing diagnostic data to Red Hat Support

When investigating OpenShift Container Platform issues, Red Hat Support might ask you to upload diagnostic data to a support case. Files can be uploaded to a support case through the Red Hat Customer Portal.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

- You have SSH access to your hosts.

- You have a Red Hat standard or premium Subscription.

- You have a Red Hat Customer Portal account.

- You have an existing Red Hat Support case ID.

</div>

<div>

<div class="title">

Procedure

</div>

- Upload diagnostic data to an existing Red Hat support case through the Red Hat Customer Portal.

  1.  Concatenate a diagnostic file contained on an OpenShift Container Platform node by using the `oc debug node/<node_name>` command and redirect the output to a file. The following example copies `/host/var/tmp/my-diagnostic-data.tar.gz` from a debug container to `/var/tmp/my-diagnostic-data.tar.gz`:

      ``` terminal
      $ oc debug node/my-cluster-node -- bash -c 'cat /host/var/tmp/my-diagnostic-data.tar.gz' > /var/tmp/my-diagnostic-data.tar.gz
      ```

      - The debug container mounts the host’s root directory at `/host`. Reference the absolute path from the debug container’s root directory, including `/host`, when specifying target files for concatenation.

        > [!NOTE]
        > OpenShift Container Platform 4.17 cluster nodes running Red Hat Enterprise Linux CoreOS (RHCOS) are immutable and rely on Operators to apply cluster changes. Transferring files from a cluster node by using `scp` is not recommended. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to copy diagnostic files from a node by running `scp core@<node>.<cluster_name>.<base_domain>:<file_path> <local_path>`.

  2.  Navigate to an existing support case within [the **Customer Support** page](https://access.redhat.com/support/cases/#/case/list) of the Red Hat Customer Portal.

  3.  Select **Attach files** and follow the prompts to upload the file.

</div>

# About `toolbox`

`toolbox` is a tool that starts a container on a Red Hat Enterprise Linux CoreOS (RHCOS) system. The tool is primarily used to start a container that includes the required binaries and plugins that are needed to run commands such as `sosreport`.

The primary purpose for a `toolbox` container is to gather diagnostic information and to provide it to Red Hat Support. However, if additional diagnostic tools are required, you can add RPM packages or run an image that is an alternative to the standard support tools image.

## Installing packages to a `toolbox` container

By default, running the `toolbox` command starts a container with the `registry.redhat.io/rhel9/support-tools:latest` image. This image contains the most frequently used support tools. If you need to collect node-specific data that requires a support tool that is not part of the image, you can install additional packages.

<div>

<div class="title">

Prerequisites

</div>

- You have accessed a node with the `oc debug node/<node_name>` command.

- You can access your system as a user with root privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set `/host` as the root directory within the debug shell. The debug pod mounts the host’s root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host’s executable paths:

    ``` terminal
    # chroot /host
    ```

2.  Start the toolbox container:

    ``` terminal
    # toolbox
    ```

3.  Install the additional package, such as `wget`:

    ``` terminal
    # dnf install -y <package_name>
    ```

</div>

## Starting an alternative image with `toolbox`

By default, running the `toolbox` command starts a container with the `registry.redhat.io/rhel9/support-tools:latest` image.

> [!NOTE]
> You can start an alternative image by creating a `.toolboxrc` file and specifying the image to run. However, running an older version of the `support-tools` image, such as `registry.redhat.io/rhel8/support-tools:latest`, is not supported on OpenShift Container Platform 4.17.

<div>

<div class="title">

Prerequisites

</div>

- You have accessed a node with the `oc debug node/<node_name>` command.

- You can access your system as a user with root privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set `/host` as the root directory within the debug shell. The debug pod mounts the host’s root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host’s executable paths:

    ``` terminal
    # chroot /host
    ```

2.  Optional: If you need to use an alternative image instead of the default image, create a `.toolboxrc` file in the home directory for the root user ID, and specify the image metadata:

    ``` text
    REGISTRY=quay.io
    IMAGE=fedora/fedora:latest
    TOOLBOX_NAME=toolbox-fedora-latest
    ```

    - Optional: Specify an alternative container registry.

    - Specify an alternative image to start.

    - Optional: Specify an alternative name for the toolbox container.

3.  Start a toolbox container by entering the following command:

    ``` terminal
    # toolbox
    ```

    > [!NOTE]
    > If an existing `toolbox` pod is already running, the `toolbox` command outputs `'toolbox-' already exists. Trying to start…​`. To avoid issues with `sosreport` plugins, remove the running toolbox container with `podman rm toolbox-` and then spawn a new toolbox container.

</div>
