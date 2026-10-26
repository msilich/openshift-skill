<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can increase the number of pod IP addresses available on each node by enlarging each node’s OVN-Kubernetes pod subnet after installation. This workflow updates the `k8s.ovn.org/node-subnets` node annotation while the Cluster Version Operator and Cluster Network Operator are scaled down.

<div class="important">

<div class="title">

</div>

- Enlarging per-node subnets does not change the support for increased pod density or the number of pods that can be supported per node. Red Hat supports tested cluster maximums rather than absolute cluster maximums. You must still adhere to the cluster scalability limits, node resources, workload behavior, and operational constraints. See "Planning your environment according to object maximums".

- This procedure applies only to the cluster network, is supported only with OVN-Kubernetes, and requires sequential node maintenance to apply the updated per-node subnet size.

</div>

# Cluster network hostPrefix overview

By enlarging the per-node pod subnet prefix length, you can allocate a larger per-node pod subnet from the same cluster network classless inter-domain routing (CIDR).

A larger per-node subnet removes pod IP address exhaustion as a bottleneck for some workloads; however, it does not guarantee a higher supported pod density per node.

<div class="important">

<div class="title">

</div>

- This operation supports increasing the per-node subnet size only. Decreasing the per-node subnet size is not covered by this workflow.

- This operation applies to the cluster network only. Changing the service network is not supported as part of this workflow.

- Do not patch the cluster `Network.config.openshift.io` object to change `spec.clusterNetwork[].hostPrefix`. The Cluster Network Operator rejects that change. The supported method updates the `k8s.ovn.org/node-subnets` annotation on each node while the Cluster Version Operator and Cluster Network Operator are scaled down.

- This operation requires sequential node maintenance to apply the updated per-node subnet size.

- During this process, your cluster’s network will be in an inconsistent state and pod connectivity will be unpredictable.

</div>

The per-node subnet size is recorded on each node in the `k8s.ovn.org/node-subnets` annotation. For example, with a cluster network CIDR of `10.128.0.0/14`, changing a node annotation from `{"default":["10.131.0.0/23"]}` to `{"default":["10.131.0.0/21"]}` enlarges that node’s allocation from a `/23` subnet to a `/21` subnet. The `/21` subnet provides more pod IP addresses per node than the `/23` subnet.

By default, a `/23` per-node subnet provides 512 addresses, with approximately 510 pod IP addresses available per node. Increasing the subnet size can provide more addresses per node; however, node-level pod density remains dependent on cluster scalability limits, node resources, workload behavior, and operational constraints.

# Planning for a cluster network hostPrefix increase

Increasing the per-node subnet size reduces the number of nodes the cluster network CIDR can support. Before you start, verify address capacity, workload disruption tolerance, and operational sequencing requirements.

When you increase the per-node subnet size, each node consumes a larger address block from the same `clusterNetwork` CIDR. As a result, the maximum number of nodes that can be allocated from that CIDR decreases. Validate that your target per-node prefix supports both your current and expected node count, and that the enlarged subnets do not overlap.

You must test the full workflow in a representative non-production environment before you apply the change to production. This testing must include:

- validating node draining and uncordoning

- validating annotation updates to `k8s.ovn.org/node-subnets`

- validating `ovnkube-node` restart and OVN logical switch verification

- validating pod rescheduling behavior

- validating that the selected per-node prefix and target pod density are appropriate for the environment

- validating drain command options against workload and operational requirements

- validating workload behavior during node evacuation

- validating that the Cluster Version Operator remains scaled down for the duration of the change on 4.22 and later

- validating post-change checks

You must also assess workload risk before you start, including:

- **Pod disruption budgets (PDBs)** can block eviction and delay node processing.

- Workloads that use `emptyDir` volumes can lose local data depending on drain options.

- Stateful and latency-sensitive workloads can experience disruption during drain and `ovnkube-node` restart cycles.

- Cluster autoscaling activity can interfere with node-by-node sequencing.

For cluster planning guidance, review the "Planning your environment according to object maximums" documentation.

# Increase the per-node subnet size

To increase the number of pod IP addresses available per node, enlarge each node’s OVN-Kubernetes pod subnet by updating the `k8s.ovn.org/node-subnets` annotation on the node while the Cluster Version Operator (CVO) and Cluster Network Operator (CNO) are scaled down.

<div class="important">

<div class="title">

</div>

- This workflow increases per-node subnets only. Complete this workflow in a representative non-production environment before you apply it to production.

- On OpenShift Container Platform 4.22 and later, including 5.0, scaling the network operator to `0` replicas is not enough. The CVO reconciles the network operator deployment back to `1` replica unless you also scale the CVO to `0` first.

- Choose target subnets that do not overlap. Enlarging a `/23` to a `/21` can collide with another node’s existing allocation; if that happens, select a non-overlapping `/21` block from the cluster network CIDR.

- If your workloads require modified drain behavior, adjust the `oc adm drain` options. Review the "Node drain options for hostPrefix changes" reference before you execute node maintenance.

</div>

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in with a user that has `cluster-admin` privileges.

- Your cluster uses the OVN-Kubernetes network plugin.

- You have verified that the target per-node prefix and cluster CIDR provide sufficient address capacity for your node count.

- You have reviewed workload disruption risks and validated node maintenance windows.

- If you intend to schedule a higher pod density after the subnet change, you have planned a `KubeletConfig` that sets appropriate `maxPods` and `podPidsLimit` values for the target machine config pool.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Record the current per-node subnet annotations by entering the following command:

    ``` terminal
    $ oc get nodes -o custom-columns='NAME:.metadata.name,SUBNET:.metadata.annotations.k8s\.ovn\.org/node-subnets'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                         SUBNET
    ip-10-0-26-42.us-west-2.compute.internal     {"default":["10.131.0.0/23"]}
    ip-10-0-42-58.us-west-2.compute.internal     {"default":["10.128.2.0/23"]}
    ```

    </div>

2.  Scale the CVO to `0` replicas so that it cannot reconcile the network operator during the change:

    ``` terminal
    $ oc -n openshift-cluster-version scale deployment/cluster-version-operator --replicas=0
    ```

3.  Scale the network operator to `0` replicas and wait until it is no longer available:

    ``` terminal
    $ oc -n openshift-network-operator scale deployment/network-operator --replicas=0
    ```

    ``` terminal
    $ oc -n openshift-network-operator wait deployment/network-operator --for=condition=Available=false --timeout=60s
    ```

4.  For each node that requires a larger per-node subnet, complete the following steps one node at a time:

    1.  Drain the node by entering the following command:

        ``` terminal
        $ oc adm drain <node_name> --ignore-daemonsets --delete-emptydir-data --force
        ```

        where:

        `<node_name>`
        Specifies the name of the node to update.

    2.  Display the current `k8s.ovn.org/node-subnets` annotation for the node by entering the following command:

        ``` terminal
        $ oc get node <node_name> -o jsonpath='{.metadata.annotations.k8s\.ovn\.org/node-subnets}{"\n"}'
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        {"default":["10.131.0.0/23"]}
        ```

        </div>

    3.  Update the annotation to the target prefix length by entering the following command:

        ``` terminal
        $ oc annotate node <node_name> --overwrite \
          k8s.ovn.org/node-subnets='{"default":["10.131.0.0/21"]}'
        ```

        where:

        `<node_name>`
        Specifies the name of the node to update.

        `10.131.0.0/21`
        Specifies the enlarged per-node subnet for this node. Replace this value with the correct subnet for the node you are updating. Keep the same network address unless that `/21` block would overlap another node; in that case, choose a non-overlapping block from the cluster network CIDR.

    4.  Identify the `ovnkube-node` pod on the node by entering the following command:

        ``` terminal
        $ OVN_POD=$(oc -n openshift-ovn-kubernetes get pods \
          --field-selector spec.nodeName=<node_name> \
          -l app=ovnkube-node -o jsonpath='{.items[0].metadata.name}')
        ```

    5.  Delete the `ovnkube-node` pod so that OVN-Kubernetes reloads the updated subnet by entering the following command:

        ``` terminal
        $ oc -n openshift-ovn-kubernetes delete pod ${OVN_POD}
        ```

    6.  After the pod restarts, verify that the OVN northbound logical switch uses the enlarged subnet by entering the following commands:

        ``` terminal
        $ OVN_POD=$(oc -n openshift-ovn-kubernetes get pods \
          --field-selector spec.nodeName=<node_name> \
          -l app=ovnkube-node -o jsonpath='{.items[0].metadata.name}')
        ```

        ``` terminal
        $ oc -n openshift-ovn-kubernetes get pod ${OVN_POD}
        ```

        ``` terminal
        $ oc rsh -n openshift-ovn-kubernetes ${OVN_POD} \
          ovn-nbctl find logical_switch name=<node_name>
        ```

        Confirm that the logical switch subnet matches the annotated `/21` or your custom value before you continue.

    7.  Uncordon the node by entering the following command:

        ``` terminal
        $ oc adm uncordon <node_name>
        ```

    8.  Confirm that the node is `Ready` and that critical workloads can schedule before you process the next node.

5.  After every required node is updated, scale the network operator back to `1` replica:

    ``` terminal
    $ oc -n openshift-network-operator scale deployment/network-operator --replicas=1
    ```

6.  Scale the CVO back to `1` replica:

    ``` terminal
    $ oc -n openshift-cluster-version scale deployment/cluster-version-operator --replicas=1
    ```

7.  Optional: If you need higher pod density after enlarging the per-node subnets, apply a `KubeletConfig` to the target machine config pool and wait for the pool to update. The following example configures worker nodes:

    ``` terminal
    $ oc label machineconfigpool worker custom-kubelet=config-worker --overwrite
    ```

    ``` terminal
    $ oc apply -f - <<EOF
    apiVersion: machineconfiguration.openshift.io/v1
    kind: KubeletConfig
    metadata:
      name: set-allocatable-worker
    spec:
      autoSizingReserved: true
      kubeletConfig:
        containerLogMaxFiles: 7
        podPidsLimit: 8192
        containerLogMaxSize: 100Mi
        maxPods: 2500
      machineConfigPoolSelector:
        matchLabels:
          custom-kubelet: config-worker
    EOF
    ```

    Adjust `maxPods`, `podPidsLimit`, and the machine config pool selector for your environment. Wait until the selected nodes reboot and the machine config pool reports an updated state before you continue.

</div>

<div>

<div class="title">

Verification

</div>

1.  Confirm that each updated node still has the enlarged subnet annotation:

    ``` terminal
    $ oc get nodes -o custom-columns='NAME:.metadata.name,SUBNET:.metadata.annotations.k8s\.ovn\.org/node-subnets'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                         SUBNET
    ip-10-0-26-42.us-west-2.compute.internal     {"default":["10.131.0.0/21"]}
    ip-10-0-42-58.us-west-2.compute.internal     {"default":["10.128.2.0/21"]}
    ```

    </div>

2.  Confirm that the network operator and CVO are available again:

    ``` terminal
    $ oc get co network cluster-version
    ```

3.  Verify critical workloads and pod scheduling behavior. If you completed the optional `KubeletConfig` step, confirm that new pods receive addresses from the enlarged per-node subnets.

    > [!NOTE]
    > The cluster `Network.config.openshift.io` object might continue to report the original `hostPrefix` value. That is expected for this workflow. The effective per-node subnet size is the value in the `k8s.ovn.org/node-subnets` annotation and in the OVN northbound logical switch, not a patched `spec.clusterNetwork[].hostPrefix` field.

</div>

# Node drain options for hostPrefix changes

The `oc adm drain` command supports options that control how pods are evicted and data is handled when you drain a node before updating its subnet annotation.

The following command is a common starting point, but you must validate each option against your workloads before production use.

``` terminal
$ oc adm drain <node> --force --delete-emptydir-data --ignore-daemonsets --disable-eviction
```

where:

`<node>`
Specifies the node name to drain.

The command options have the following effects:

`--force`
Allows drain to continue for pods that are not managed by a controller. This can interrupt unmanaged workloads.

`--delete-emptydir-data`
Deletes pods using `emptyDir` volumes. Data stored in `emptyDir` is lost when those pods are removed.

`--ignore-daemonsets`
Continues drain without evicting DaemonSet-managed pods. DaemonSet pods remain and can affect full node evacuation expectations.

`--disable-eviction`
Uses delete operations instead of eviction API behavior. This bypasses pod disruption budget protections and can cause greater disruption.

Use caution when workloads include:

- Stateful applications that depend on local data.

- Applications with strict pod disruption budgets.

- Applications with long startup times or strict availability objectives.

- Applications that are sensitive to forced deletion behavior.

If these conditions apply, customize drain behavior for your environment and validate the command in non-production before production use.

# Troubleshooting hostPrefix increases

Common issues when enlarging per-node subnets include annotation synchronization failures, pod scheduling delays, and partial-completion scenarios across nodes.

## Node does not receive an updated subnet

If a node does not reflect the expected subnet allocation after you annotate it and restart `ovnkube-node`:

- Confirm that the `k8s.ovn.org/node-subnets` annotation on the node shows the target prefix, for example `{"default":["10.131.0.0/21"]}`.

- Confirm that the Cluster Version Operator and network operator deployments are still scaled to `0` replicas while you make the change.

- Verify the OVN northbound logical switch for the node with `ovn-nbctl find logical_switch name=<node_name>`.

- Verify node readiness and that the `ovnkube-node` pod on the node is `Running`.

- If the enlarged subnet overlaps another node’s allocation, choose a non-overlapping block from the cluster network CIDR and update the annotation again.

## Pods do not reschedule after node drain

If workloads do not recover after draining a node:

- Check for pod disruption budget constraints.

- Check for insufficient cluster capacity on remaining schedulable nodes.

- Review workload-specific constraints, such as affinity, taints, tolerations, and storage requirements.

## Partial completion across nodes

If only some nodes are updated:

- Stop processing additional nodes until operator and workload health are restored.

- Confirm that each completed node is in `Ready` state.

- Continue only when the cluster reports stable operator conditions.

## Data to collect for a support case

Before opening a support case, collect:

- A must-gather capture.

- Current network configuration:

  ``` terminal
  $ oc get network.config.openshift.io cluster -o yaml
  ```

- Cluster operator state:

  ``` terminal
  $ oc get clusteroperators network -o yaml
  ```

- Node status and conditions:

  ``` terminal
  $ oc get nodes -o wide
  $ oc describe node <node>
  ```

- Recent events in affected namespaces:

  ``` terminal
  $ oc get events -A --sort-by=.lastTimestamp
  ```

# Additional resources

- [CIDR range definitions](../networking_overview/cidr-range-definitions.md#cidr-range-definitions)

- [Configuring the cluster network range](../configuring_network_settings/configuring-cluster-network-range.md#configuring-cluster-network-range)

- [Planning your environment according to object maximums](../../scalability_and_performance/planning-your-environment-according-to-object-maximums.md#planning-your-environment-according-to-object-maximums)
