<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As an administrator, you can perform several tasks to make your clusters more efficient.

# Evacuating pods on nodes

You can remove, or evacuate, pods from a given node or nodes. Evacuating pods allows you to migrate all or selected pods to other nodes.

You can evacuate only pods that are backed by a replication controller. The replication controller creates new pods on other nodes and removes the existing pods from the specified node(s).

Bare pods, meaning those not backed by a replication controller, are unaffected by default. You can evacuate a subset of pods by specifying a pod selector. Because pod selectors are based on labels, all of the pods with the specified label are evacuated.

<div>

<div class="title">

Procedure

</div>

1.  Mark the nodes as unschedulable before performing the pod evacuation.

    1.  Mark the node as unschedulable by running the following command:

        ``` terminal
        $ oc adm cordon <node1>
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        node/<node1> cordoned
        ```

        </div>

    2.  Check that the node status is `Ready,SchedulingDisabled` by running the following command:

        ``` terminal
        $ oc get node <node1>
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME        STATUS                     ROLES     AGE       VERSION
        <node1>     Ready,SchedulingDisabled   worker    1d        v1.33.4
        ```

        </div>

2.  Evacuate the pods by using one of the following methods:

    - Evacuate all or selected pods on one or more nodes by running the `oc adm drain` command:

      ``` terminal
      $ oc adm drain <node1> <node2> [--pod-selector=<pod_selector>]
      ```

    - Force the deletion of bare pods by using the `--force` option with the `oc adm drain` command. When set to `true`, deletion continues even if there are pods not managed by a replication controller, replica set, job, daemon set, or stateful set.

      ``` terminal
      $ oc adm drain <node1> <node2> --force=true
      ```

    - Set a period of time in seconds for each pod to terminate gracefully by using the `--grace-period` option with the `oc adm drain` command. If negative, the default value specified in the pod will be used:

      ``` terminal
      $ oc adm drain <node1> <node2> --grace-period=-1
      ```

    - Ignore pods managed by daemon sets by using the `--ignore-daemonsets=true` option with the `oc adm drain` command:

      ``` terminal
      $ oc adm drain <node1> <node2> --ignore-daemonsets=true
      ```

    - Set the length of time to wait before giving up using the `--timeout` option with the `oc adm drain` command. A value of `0` sets an infinite length of time.

      ``` terminal
      $ oc adm drain <node1> <node2> --timeout=5s
      ```

    - Delete pods even if there are pods using `emptyDir` volumes by setting the `--delete-emptydir-data=true` option with the `oc adm drain` command. Local data is deleted when the node is drained.

      ``` terminal
      $ oc adm drain <node1> <node2> --delete-emptydir-data=true
      ```

    - List objects that would be migrated without actually performing the evacuation, by using the `--dry-run=true` option with the `oc adm drain` command:

      ``` terminal
      $ oc adm drain <node1> <node2>  --dry-run=true
      ```

      Instead of specifying specific node names (for example, `<node1> <node2>`), you can use the `--selector=<node_selector>` option with the `oc adm drain` command to evacuate pods on selected nodes.

3.  Mark the node as schedulable when done by using the following command.

    ``` terminal
    $ oc adm uncordon <node1>
    ```

</div>

# Understanding how to update labels on nodes

You can update any label on a node in order to adapt your cluster to evolving needs.

Node labels are not persisted after a node is deleted even if the node is backed up by a Machine.

> [!NOTE]
> Any change to a `MachineSet` object is not applied to existing machines owned by the compute machine set. For example, labels edited or added to an existing `MachineSet` object are not propagated to existing machines and nodes associated with the compute machine set.

- The following command adds or updates labels on a node:

  ``` terminal
  $ oc label node <node> <key_1>=<value_1> ... <key_n>=<value_n>
  ```

  For example:

  ``` terminal
  $ oc label nodes webconsole-7f7f6 unhealthy=true
  ```

  > [!TIP]
  > You can alternatively apply the following YAML to apply the label:
  >
  > ``` yaml
  > kind: Node
  > apiVersion: v1
  > metadata:
  >   name: webconsole-7f7f6
  >   labels:
  >     unhealthy: 'true'
  > #...
  > ```

- The following command updates all pods in the namespace:

  ``` terminal
  $ oc label pods --all <key_1>=<value_1>
  ```

  For example:

  ``` terminal
  $ oc label pods --all status=unhealthy
  ```

> [!IMPORTANT]
> In OpenShift Container Platform 4.12 and later, newly installed clusters include both the `node-role.kubernetes.io/control-plane` and `node-role.kubernetes.io/master` labels on control plane nodes by default.
>
> In OpenShift Container Platform versions earlier than 4.12, the `node-role.kubernetes.io/control-plane` label is not added by default. Therefore, you must manually add the `node-role.kubernetes.io/control-plane` label to control plane nodes in clusters upgraded from earlier versions.

# Understanding how to mark nodes as unschedulable or schedulable

You can mark a node as unschedulable in order to block any new pods from being scheduled on the node.

When you mark a node as unschedulable, existing pods on the node are not affected.

By default, healthy nodes with a `Ready` status are marked as schedulable, which means that you can place new pods on the node.

- The following command marks a node or nodes as unschedulable:

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  $ oc adm cordon <node>
  ```

  </div>

  For example:

  ``` terminal
  $ oc adm cordon node1.example.com
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  node/node1.example.com cordoned

  NAME                 LABELS                                        STATUS
  node1.example.com    kubernetes.io/hostname=node1.example.com      Ready,SchedulingDisabled
  ```

  </div>

- The following command marks a currently unschedulable node or nodes as schedulable:

  ``` terminal
  $ oc adm uncordon <node1>
  ```

  Instead of specifying specific node names (for example, `<node>`), you can use the `--selector=<node_selector>` option to mark selected nodes as schedulable or unschedulable.

# Handling errors in single-node OpenShift clusters when the node reboots without draining application pods

You can remove failed pods from a node by using the `--field-selector status.phase=Failed` flag with the `oc delete pods` command.

In single-node OpenShift clusters and in OpenShift Container Platform clusters in general, a situation can arise where a node reboot occurs without first draining the node. This can occur where an application pod requesting devices fails with the `UnexpectedAdmissionError` error. `Deployment`, `ReplicaSet`, or `DaemonSet` errors are reported because the application pods that require those devices start before the pod serving those devices. You cannot control the order of pod restarts.

While this behavior is to be expected, it can cause a pod to remain on the cluster even though it has failed to deploy successfully. The pod continues to report `UnexpectedAdmissionError`. This issue is mitigated by the fact that application pods are typically included in a `Deployment`, `ReplicaSet`, or `DaemonSet`. If a pod is in this error state, it is of little concern because another instance should be running. Belonging to a `Deployment`, `ReplicaSet`, or `DaemonSet` guarantees the successful creation and execution of subsequent pods and ensures the successful deployment of the application.

There is ongoing work upstream to ensure that such pods are gracefully terminated. Until that work is resolved, run the following command for a single-node OpenShift cluster to remove the failed pods:

``` terminal
$ oc delete pods --field-selector status.phase=Failed -n <POD_NAMESPACE>
```

> [!NOTE]
> The option to drain the node is unavailable for single-node OpenShift clusters.

# Deleting nodes from a cluster

You can delete a node from a OpenShift Container Platform cluster by scaling down the appropriate `MachineSet` object.

> [!IMPORTANT]
> When a cluster is integrated with a cloud provider, you must delete the corresponding machine to delete a node. Do not try to use the `oc delete node` command for this task.

When you delete a node by using the CLI, the node object is deleted in Kubernetes, but the pods that exist on the node are not deleted. Any bare pods that are not backed by a replication controller become inaccessible to OpenShift Container Platform. Pods backed by replication controllers are rescheduled to other available nodes. You must delete local manifest pods.

> [!NOTE]
> If you are running cluster on bare metal, you cannot delete a node by editing `MachineSet` objects. Compute machine sets are only available when a cluster is integrated with a cloud provider. Instead you must unschedule and drain the node before manually deleting it.

<div>

<div class="title">

Procedure

</div>

1.  View the compute machine sets that are in the cluster by running the following command:

    ``` terminal
    $ oc get machinesets -n openshift-machine-api
    ```

    The compute machine sets are listed in the form of `<cluster-id>-worker-<aws-region-az>`.

2.  Scale down the compute machine set by using one of the following methods:

    - Specify the number of replicas to scale down to by running the following command:

      ``` terminal
      $ oc scale --replicas=2 machineset <machine-set-name> -n openshift-machine-api
      ```

    - Edit the compute machine set custom resource by running the following command:

      ``` terminal
      $ oc edit machineset <machine-set-name> -n openshift-machine-api
      ```

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` yaml
      apiVersion: machine.openshift.io/v1beta1
      kind: MachineSet
      metadata:
        # ...
        name: <machine-set-name>
        namespace: openshift-machine-api
        # ...
      spec:
        replicas: 2
        # ...
      ```

      </div>

      where:

      `spec.replicas`
      Specifies the number of replicas to scale down to.

</div>

## Deleting nodes from a bare metal cluster

You can delete a node from a OpenShift Container Platform cluster that does not use machine sets by using the `oc delete node` command and decommissioning the node.

When you delete a node using the CLI, the node object is deleted in Kubernetes, but the pods that exist on the node are not deleted. Any bare pods not backed by a replication controller become inaccessible to OpenShift Container Platform. Pods backed by replication controllers are rescheduled to other available nodes. You must delete local manifest pods.

The following procedure deletes a node from an OpenShift Container Platform cluster running on bare metal.

<div>

<div class="title">

Procedure

</div>

1.  Mark the node as unschedulable:

    ``` terminal
    $ oc adm cordon <node_name>
    ```

2.  Drain all pods on the node:

    ``` terminal
    $ oc adm drain <node_name> --force=true
    ```

    This step might fail if the node is offline or unresponsive. Even if the node does not respond, the node might still be running a workload that writes to shared storage. To avoid data corruption, power down the physical hardware before you proceed.

3.  Delete the node from the cluster:

    ``` terminal
    $ oc delete node <node_name>
    ```

    Although the node object is now deleted from the cluster, it can still rejoin the cluster after reboot or if the kubelet service is restarted. To permanently delete the node and all its data, you must [decommission the node](https://access.redhat.com/solutions/84663).

4.  If you powered down the physical hardware, turn it back on so that the node can rejoin the cluster.

</div>

# Additional resources

- [Evacuating pods on nodes](nodes-nodes-working.md#nodes-nodes-working-evacuating_nodes-nodes-working)

- [Manually scaling a compute machine set](../../machine_management/manually-scaling-machineset.md#machineset-manually-scaling-manually-scaling-machineset)
