<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To manage SR-IOV network devices and network attachments in your cluster, use the Single Root I/O Virtualization (SR-IOV) Network Operator.

# Configuring the SR-IOV Network Operator

To manage SR-IOV network devices and network attachments in your cluster, configure the Single Root I/O Virtualization (SR-IOV) Network Operator.

<div>

<div class="title">

Procedure

</div>

1.  Create a `SriovOperatorConfig` custom resource (CR). The following example creates a file named `sriovOperatorConfig.yaml`:

    ``` yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovOperatorConfig
    metadata:
      name: default
      namespace: openshift-sriov-network-operator
    spec:
      disableDrain: false
      enableInjector: true
      enableOperatorWebhook: true
      logLevel: 2
      featureGates:
        metricsExporter: false
    # ...
    ```

    where:

    `metadata.name`
    Specifies the name of the SR-IOV Network Operator instance. The only valid name for the `SriovOperatorConfig` resource is `default` and the name must be in the namespace where the Operator is deployed.

    `spec.enableInjector`
    Specifies if any `network-resources-injector` pod can run in the namespace. If not specified in the CR or explicitly set to `true`, defaults to `false` or `<none>`, preventing any `network-resources-injector` pod from running in the namespace. The recommended setting is `true`.

    `spec.enableOperatorWebhook`
    Specifies if any `operator-webhook` pods can run in the namespace. The `enableOperatorWebhook` field, if not specified in the CR or explicitly set to true, defaults to `false` or `<none>`, preventing any `operator-webhook` pod from running in the namespace. The recommended setting is `true`.

2.  Apply the resource to your cluster by running the following command:

    ``` terminal
    $ oc apply -f sriovOperatorConfig.yaml
    ```

</div>

# SR-IOV Network Operator config custom resource

To customize the SR-IOV Network Operator, configure the `sriovoperatorconfig` custom resource.

The following table describes the `sriovoperatorconfig` CR fields:

<table>
<caption>SR-IOV Network Operator config custom resource</caption>
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
<td style="text-align: left;"><p>Specifies the name of the SR-IOV Network Operator instance. The default value is <code>default</code>. Do not set a different value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>metadata.namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the namespace of the SR-IOV Network Operator instance. The default value is <code>openshift-sriov-network-operator</code>. Do not set a different value.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.configDaemonNodeSelector</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Specifies the node selection to control scheduling the SR-IOV Network Config Daemon on selected nodes. By default, this field is not set and the Operator deploys the SR-IOV Network Config daemon set on compute nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.disableDrain</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Specifies whether to disable the node draining process or enable the node draining process when you apply a new policy to configure the NIC on a node. Setting this field to <code>true</code> facilitates software development and installing OpenShift Container Platform on a single node. By default, this field is not set. For single-node clusters, set this field to <code>true</code> after installing the Operator. This field must remain set to <code>true</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.enableInjector</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Specifies whether to enable or disable the Network Resources Injector daemon set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.enableOperatorWebhook</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Specifies whether to enable or disable the Operator Admission Controller webhook daemon set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.logLevel</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Specifies the log verbosity level of the Operator. By default, this field is set to <code>0</code>, which shows only basic logs. Set to <code>2</code> to show all the available logs.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.featureGates</code></p></td>
<td style="text-align: left;"><p><code>map[string]bool</code></p></td>
<td style="text-align: left;"><p>Specifies whether to enable or disable the optional features. For example, <code>metricsExporter</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.featureGates.metricsExporter</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Specifies whether to enable or disable the SR-IOV Network Operator metrics. By default, this field is set to <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.featureGates.mellanoxFirmwareReset</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Specifies whether to reset the firmware on virtual function (VF) changes in the SR-IOV Network Operator. Some chipsets, such as the Intel C740 Series, do not completely power off the PCI-E devices, which is required to configure VFs on NVIDIA/Mellanox NICs. By default, this field is set to <code>false</code>.</p>
<div class="important">
<div class="title">
&#10;</div>
<p>The <code>spec.featureGates.mellanoxFirmwareReset</code> parameter is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.</p>
<p>For more information about the support scope of Red Hat Technology Preview features, see <a href="https://access.redhat.com/support/offerings/techpreview/">Technology Preview Features Support Scope</a>.</p>
</div></td>
</tr>
</tbody>
</table>

# About the Network Resources Injector

You can use the Network Resources Injector, a Kubernetes Dynamic Admission Controller application, to mutate resource requests and limits in a pod specification and mutate a pod specification with a Downward API volume.

The Network Resources Injector provides the following capabilities:

- Mutation of resource requests and limits in a pod specification to add an SR-IOV resource name according to an SR-IOV network attachment definition annotation.

- Mutation of a pod specification with a Downward API volume to expose pod annotations, labels, and huge pages requests and limits. Containers that run in the pod can access the exposed information as files under the `/etc/podnetinfo` path.

The SR-IOV Network Operator enables the Network Resources Injector when the `enableInjector` is set to `true` in the `SriovOperatorConfig` CR. The `network-resources-injector` pod runs as a daemon set on all control plane nodes. The following is an example of Network Resources Injector pods running in a cluster with three control plane nodes:

``` terminal
$ oc get pods -n openshift-sriov-network-operator
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
NAME                                      READY   STATUS    RESTARTS   AGE
network-resources-injector-5cz5p          1/1     Running   0          10m
network-resources-injector-dwqpx          1/1     Running   0          10m
network-resources-injector-lktz5          1/1     Running   0          10m
```

</div>

By default, the `failurePolicy` field in the Network Resources Injector webhook is set to `Ignore`. This default setting prevents pod creation from being blocked if the webhook is unavailable.

If you set the `failurePolicy` field to `Fail`, and the Network Resources Injector webhook is unavailable, the webhook attempts to mutate all pod creation and update requests. This behavior can block pod creation and disrupt normal cluster operations. To prevent such issues, you can enable the `featureGates.resourceInjectorMatchCondition` feature in the `SriovOperatorConfig` object to limit the scope of the Network Resources Injector webhook. If this feature is enabled, the webhook applies only to pods with the secondary network annotation `k8s.v1.cni.cncf.io/networks`.

If you set the `failurePolicy` field to `Fail` after enabling the `resourceInjectorMatchCondition` feature, the webhook applies only to pods with the secondary network annotation `k8s.v1.cni.cncf.io/networks`. If the webhook is unavailable, the cluster still deploys pods without this annotation; this prevents unnecessary disruptions to cluster operations.

The `featureGates.resourceInjectorMatchCondition` feature is disabled by default. To enable this feature, set the `featureGates.resourceInjectorMatchCondition` field to `true` in the `SriovOperatorConfig` object.

<div class="formalpara">

<div class="title">

Example `SriovOperatorConfig` object configuration

</div>

``` yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovOperatorConfig
metadata:
  name: default
  namespace: sriov-network-operator
spec:
# ...
  featureGates:
    resourceInjectorMatchCondition: true
# ...
```

</div>

# Disabling or enabling the Network Resources Injector

To control the automatic configuration of your cluster workloads, enable or disable the Network Resources Injector.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- You must have installed the SR-IOV Network Operator.

</div>

<div>

<div class="title">

Procedure

</div>

- Set the `enableInjector` field. Replace `<value>` with `false` to disable the feature or `true` to enable the feature.

  ``` terminal
  $ oc patch sriovoperatorconfig default \
    --type=merge -n openshift-sriov-network-operator \
    --patch '{ "spec": { "enableInjector": <value> } }'
  ```

  > [!TIP]
  > You can alternatively apply the following YAML to update the Operator:
  >
  > ``` yaml
  > apiVersion: sriovnetwork.openshift.io/v1
  > kind: SriovOperatorConfig
  > metadata:
  >   name: default
  >   namespace: openshift-sriov-network-operator
  > spec:
  >   enableInjector: <value>
  > # ...
  > ```

</div>

# About the SR-IOV Network Operator admission controller webhook

You can use the SR-IOV Network Operator Admission Controller webhook to mutate or validate the `SriovNetworkNodePolicy` CR.

- Validation of the `SriovNetworkNodePolicy` CR when it is created or updated.

- Mutation of the `SriovNetworkNodePolicy` CR by setting the default value for the `priority` and `deviceType` fields when the CR is created or updated.

The SR-IOV Network Operator Admission Controller webhook is enabled by the Operator when the `enableOperatorWebhook` is set to `true` in the `SriovOperatorConfig` CR. The `operator-webhook` pod runs as a daemon set on all control plane nodes.

> [!NOTE]
> Use caution when disabling the SR-IOV Network Operator Admission Controller webhook. You can disable the webhook under specific circumstances, such as troubleshooting, or if you want to use unsupported devices. For information about configuring unsupported devices, see "Configuring the SR-IOV Network Operator to use an unsupported NIC".

The following is an example of the Operator Admission Controller webhook pods running in a cluster with three control plane nodes:

``` terminal
$ oc get pods -n openshift-sriov-network-operator
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
NAME                                      READY   STATUS    RESTARTS   AGE
operator-webhook-9jkw6                    1/1     Running   0          16m
operator-webhook-kbr5p                    1/1     Running   0          16m
operator-webhook-rpfrl                    1/1     Running   0          16m
```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring the SR-IOV Network Operator to use an unsupported NIC](https://access.redhat.com/articles/7010183)

</div>

# Disabling or enabling the SR-IOV Network Operator admission controller webhook

To manage validation of your network configurations, enable or disable the SR-IOV Network Operator admission controller webhook.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- You must have installed the SR-IOV Network Operator.

</div>

<div>

<div class="title">

Procedure

</div>

- Set the `enableOperatorWebhook` field. Replace `<value>` with `false` to disable the feature or `true` to enable it:

  ``` terminal
  $ oc patch sriovoperatorconfig default --type=merge \
    -n openshift-sriov-network-operator \
    --patch '{ "spec": { "enableOperatorWebhook": <value> } }'
  ```

  > [!TIP]
  > You can alternatively apply the following YAML to update the Operator:
  >
  > ``` yaml
  > apiVersion: sriovnetwork.openshift.io/v1
  > kind: SriovOperatorConfig
  > metadata:
  >   name: default
  >   namespace: openshift-sriov-network-operator
  > spec:
  >   enableOperatorWebhook: <value>
  > # ...
  > ```

</div>

# Configuring a custom NodeSelector for the SR-IOV Network Config daemon

The SR-IOV Network Config daemon discovers and configures the SR-IOV network devices on cluster nodes. By default, the daemon is deployed to all the compute nodes in the cluster. You can use node labels to specify on which nodes the SR-IOV Network Config daemon runs.

> [!IMPORTANT]
> When you update the `configDaemonNodeSelector` field, the SR-IOV Network Config daemon is recreated on each selected node. While the daemon is recreated, cluster users are unable to apply any new SR-IOV Network node policy or create new SR-IOV pods.

<div>

<div class="title">

Procedure

</div>

- To update the node selector for the Operator, enter the following command:

  ``` terminal
  $ oc patch sriovoperatorconfig default --type=json \
    -n openshift-sriov-network-operator \
    --patch '[{
        "op": "replace",
        "path": "/spec/configDaemonNodeSelector",
        "value": {<node_label>}
      }]'
  ```

  Replace `<node_label>` with a label to apply as in the following example: `"node-role.kubernetes.io/worker": ""`.

  > [!TIP]
  > You can alternatively apply the following YAML to update the Operator:
  >
  > ``` yaml
  > apiVersion: sriovnetwork.openshift.io/v1
  > kind: SriovOperatorConfig
  > metadata:
  >   name: default
  >   namespace: openshift-sriov-network-operator
  > spec:
  >   configDaemonNodeSelector:
  >     <node_label>
  > # ...
  > ```

</div>

# Configuring the SR-IOV Network Operator for single node installations

By default, the SR-IOV Network Operator drains workloads from a node before every policy change. The Operator performs this action to ensure that no workloads are using the virtual functions before the reconfiguration. As a result, you must configure the Operator to not drain workloads from the single node.

For installations on a single node, other nodes do not receive the workloads.

> [!IMPORTANT]
> After performing the following procedure to disable draining workloads, you must remove any workload that uses an SR-IOV network interface before you change any SR-IOV network node policy.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- You must have installed the SR-IOV Network Operator.

</div>

<div>

<div class="title">

Procedure

</div>

- To set the `disableDrain` field to `true` and the `configDaemonNodeSelector` field to `node-role.kubernetes.io/master: ""`, enter the following command:

  ``` terminal
  $ oc patch sriovoperatorconfig default --type=merge -n openshift-sriov-network-operator --patch '{ "spec": { "disableDrain": true, "configDaemonNodeSelector": { "node-role.kubernetes.io/master": "" } } }'
  ```

  > [!TIP]
  > You can alternatively apply the following YAML to update the Operator:
  >
  > ``` yaml
  > apiVersion: sriovnetwork.openshift.io/v1
  > kind: SriovOperatorConfig
  > metadata:
  >   name: default
  >   namespace: openshift-sriov-network-operator
  > spec:
  >   disableDrain: true
  >   configDaemonNodeSelector:
  >    node-role.kubernetes.io/master: ""
  > # ...
  > ```

</div>

## Deploying the SR-IOV Operator for hosted control planes

After you configure and deploy your hosting service cluster, you can create a subscription to the SR-IOV Operator on a hosted cluster. The SR-IOV pod runs on worker machines rather than the control plane.

<div class="formalpara">

<div class="title">

Prerequisites

</div>

You must configure and deploy the hosted cluster on AWS.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a namespace and an Operator group:

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: openshift-sriov-network-operator
    ---
    apiVersion: operators.coreos.com/v1
    kind: OperatorGroup
    metadata:
      name: sriov-network-operators
      namespace: openshift-sriov-network-operator
    spec:
      targetNamespaces:
      - openshift-sriov-network-operator
    ```

2.  Create a subscription to the SR-IOV Operator:

    ``` yaml
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: sriov-network-operator-subsription
      namespace: openshift-sriov-network-operator
    spec:
      channel: stable
      name: sriov-network-operator
      config:
        nodeSelector:
          node-role.kubernetes.io/worker: ""
      source: redhat-operators
      sourceNamespace: openshift-marketplace
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  To verify that the SR-IOV Operator is ready, run the following command and view the resulting output:

    ``` terminal
    $ oc get csv -n openshift-sriov-network-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                         DISPLAY                   VERSION               REPLACES                                     PHASE
    sriov-network-operator.4.17.0-202211021237   SR-IOV Network Operator   4.17.0-202211021237   sriov-network-operator.4.17.0-202210290517   Succeeded
    ```

    </div>

2.  To verify that the SR-IOV pods are deployed, run the following command:

    ``` terminal
    $ oc get pods -n openshift-sriov-network-operator
    ```

</div>

# About the SR-IOV network metrics exporter

The Single Root I/O Virtualization (SR-IOV) network metrics exporter reads the metrics for SR-IOV virtual functions (VFs) and exposes these VF metrics in Prometheus format. When the SR-IOV network metrics exporter is enabled, you can query the SR-IOV VF metrics by using the OpenShift Container Platform web console to monitor the networking activity of the SR-IOV pods.

When you query the SR-IOV VF metrics by using the web console, the SR-IOV network metrics exporter fetches and returns the VF network statistics along with the name and namespace of the pod that the VF is attached to.

The following table describes the SR-IOV VF metrics that the metrics exporter reads and exposes in Prometheus format:

| Metric | Description | Example PromQL query to examine the VF metric |
|----|----|----|
| `sriov_vf_rx_bytes` | Received bytes per virtual function. | `sriov_vf_rx_bytes * on (pciAddr,node) group_left(pod,namespace,dev_type) sriov_kubepoddevice` |
| `sriov_vf_tx_bytes` | Transmitted bytes per virtual function. | `sriov_vf_tx_bytes * on (pciAddr,node) group_left(pod,namespace,dev_type) sriov_kubepoddevice` |
| `sriov_vf_rx_packets` | Received packets per virtual function. | `sriov_vf_rx_packets * on (pciAddr,node) group_left(pod,namespace,dev_type) sriov_kubepoddevice` |
| `sriov_vf_tx_packets` | Transmitted packets per virtual function. | `sriov_vf_tx_packets * on (pciAddr,node) group_left(pod,namespace,dev_type) sriov_kubepoddevice` |
| `sriov_vf_rx_dropped` | Dropped packets upon receipt per virtual function. | `sriov_vf_rx_dropped * on (pciAddr,node) group_left(pod,namespace,dev_type) sriov_kubepoddevice` |
| `sriov_vf_tx_dropped` | Dropped packets during transmission per virtual function. | `sriov_vf_tx_dropped * on (pciAddr,node) group_left(pod,namespace,dev_type) sriov_kubepoddevice` |
| `sriov_vf_rx_multicast` | Received multicast packets per virtual function. | `sriov_vf_rx_multicast * on (pciAddr,node) group_left(pod,namespace,dev_type) sriov_kubepoddevice` |
| `sriov_vf_rx_broadcast` | Received broadcast packets per virtual function. | `sriov_vf_rx_broadcast * on (pciAddr,node) group_left(pod,namespace,dev_type) sriov_kubepoddevice` |
| `sriov_kubepoddevice` | Virtual functions linked to active pods. | \- |

SR-IOV VF metrics

You can also combine these queries by using the `kube-state-metrics` tool to get more information about the SR-IOV pods. For example, you can use the following query to get the VF network statistics along with the application name from the standard Kubernetes pod label:

``` terminal
(sriov_vf_tx_packets * on (pciAddr,node)  group_left(pod,namespace)  sriov_kubepoddevice) * on (pod,namespace) group_left (label_app_kubernetes_io_name) kube_pod_labels
```

## Enabling the SR-IOV network metrics exporter

To enable the SR-IOV network metrics exporter, set the `spec.featureGates.metricsExporter` field to `true`. Because the exporter is disabled by default, you must explicitly enable the SR-IOV network metrics exporter.

> [!IMPORTANT]
> When the metrics exporter is enabled, the SR-IOV Network Operator deploys the metrics exporter only on nodes with SR-IOV capabilities.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in as a user with `cluster-admin` privileges.

- You have installed the SR-IOV Network Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enable cluster monitoring by running the following command:

    ``` terminal
    $ oc label ns/openshift-sriov-network-operator openshift.io/cluster-monitoring=true
    ```

    To enable cluster monitoring, you must add the `openshift.io/cluster-monitoring=true` label in the namespace where you have installed the SR-IOV Network Operator.

2.  Set the `spec.featureGates.metricsExporter` field to `true` by running the following command:

    ``` terminal
    $ oc patch -n openshift-sriov-network-operator sriovoperatorconfig/default \
        --type='merge' -p='{"spec": {"featureGates": {"metricsExporter": true}}}'
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Check that the SR-IOV network metrics exporter is enabled by running the following command:

    ``` terminal
    $ oc get pods -n openshift-sriov-network-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                     READY   STATUS    RESTARTS   AGE
    operator-webhook-hzfg4                   1/1     Running   0          5d22h
    sriov-network-config-daemon-tr54m        1/1     Running   0          5d22h
    sriov-network-metrics-exporter-z5d7t     1/1     Running   0          10s
    sriov-network-operator-cc6fd88bc-9bsmt   1/1     Running   0          5d22h
    ```

    </div>

    Ensure that `sriov-network-metrics-exporter` pod is in the `READY` state.

2.  Optional: Examine the SR-IOV virtual function (VF) metrics by using the OpenShift Container Platform web console. For more information, see "Querying metrics".

</div>

<div>

<div class="title">

Additional resources

</div>

- [Querying metrics for all projects with the monitoring dashboard](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/accessing_metrics/accessing-metrics-as-an-administrator#querying-metrics-for-all-projects-with-mon-dashboard_accessing-metrics-as-an-administrator)

- [Querying metrics for user-defined projects as a developer](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/4.20/html/accessing_metrics/accessing-metrics-as-a-developer#querying-metrics-for-user-defined-projects-with-mon-dashboard_accessing-metrics-as-a-developer)

- [Configuring an SR-IOV network device](../../hardware_networks/configuring-sriov-device.md#configuring-sriov-device)

- [Uninstalling the SR-IOV Network Operator](uninstalling-sriov-operator.md#uninstalling-sriov-operator)

</div>
