<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Pod priority ranks pods by importance to influence scheduling order, sort out-of-resource evictions, and enable preemption, where higher-priority pods can evict lower-priority pods when resources are constrained.

To use priority and preemption, you create priority classes that define the relative weight of your pods. Then, reference a priority class in the pod specification to apply that weight for scheduling.

# Understanding pod priority

Pod priority uses priority classes with integer values to determine scheduling order, with higher-priority pods placed ahead in the queue and scheduled before lower-priority pods when requirements are met.

## Pod priority classes

You can assign pods a priority class, which is a non-namespaced object that defines a mapping from a name to the integer value of the priority. The higher the value, the higher the priority.

A priority class object can take any 32-bit integer value smaller than or equal to 1000000000 (one billion). Reserve numbers larger than or equal to one billion for critical pods that must not be preempted or evicted. By default, OpenShift Container Platform has two reserved priority classes for critical system pods to have guaranteed scheduling.

``` terminal
$ oc get priorityclasses
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
NAME                      VALUE        GLOBAL-DEFAULT   AGE
system-node-critical      2000001000   false            72m
system-cluster-critical   2000000000   false            72m
openshift-user-critical   1000000000   false            3d13h
cluster-logging           1000000      false            29s
```

</div>

- **system-node-critical** - This priority class has a value of 2000001000 and is used for all pods that should never be evicted from a node. Examples of pods that have this priority class are `ovnkube-node`, and so forth. A number of critical components include the `system-node-critical` priority class by default, for example:

  - master-api

  - master-controller

  - master-etcd

  - ovn-kubernetes

  - sync

- **system-cluster-critical** - This priority class has a value of 2000000000 (two billion) and is used with pods that are important for the cluster. Pods with this priority class can be evicted from a node in certain circumstances. For example, pods configured with the `system-node-critical` priority class can take priority. However, this priority class does ensure guaranteed scheduling. Examples of pods that can have this priority class are fluentd, add-on components like descheduler, and so forth. A number of critical components include the `system-cluster-critical` priority class by default, for example:

  - fluentd

  - metrics-server

  - descheduler

- **openshift-user-critical** - You can use the `priorityClassName` field with important pods that cannot bind their resource consumption and do not have predictable resource consumption behavior. Prometheus pods under the `openshift-monitoring` and `openshift-user-workload-monitoring` namespaces use the `openshift-user-critical` `priorityClassName`. Monitoring workloads use `system-critical` as their first `priorityClass`, but this causes problems when monitoring uses excessive memory and the nodes cannot evict them. As a result, monitoring drops priority to give the scheduler flexibility, moving heavy workloads around to keep critical nodes operating.

- **cluster-logging** - This priority is used by Fluentd to make sure Fluentd pods are scheduled to nodes over other apps.

## Pod priority names

After you have one or more priority classes, you can create pods that specify a priority class name in a `Pod` spec. The priority admission controller uses the priority class name field to populate the integer value of the priority. If the named priority class is not found, the pod is rejected.

# Understanding pod preemption

With pod preemption, the scheduler can evict lower-priority pods from nodes when higher-priority pods cannot find available resources, enabling critical workloads to run even when cluster capacity is constrained.

When the scheduler preempts one or more pods on a node, the `nominatedNodeName` field of higher-priority `Pod` spec is set to the name of the node, along with the `nodename` field. The scheduler uses the `nominatedNodeName` field to keep track of the resources reserved for pods and also provides information to the user about preemptions in the clusters.

After the scheduler preempts a lower-priority pod, the scheduler honors the graceful termination period of the pod. If another node becomes available while scheduler is waiting for the lower-priority pod to terminate, the scheduler can schedule the higher-priority pod on that node. As a result, the `nominatedNodeName` field and `nodeName` field of the `Pod` spec might be different.

Also, if the scheduler preempts pods on a node and is waiting for termination, and a pod with a higher-priority pod than the pending pod needs to be scheduled, the scheduler can schedule the higher-priority pod instead. In such a case, the scheduler clears the `nominatedNodeName` of the pending pod, making the pod eligible for another node.

Preemption does not necessarily remove all lower-priority pods from a node. The scheduler can schedule a pending pod by removing a portion of the lower-priority pods.

The scheduler considers a node for pod preemption only if the pending pod can be scheduled on the node.

## Non-preempting priority classes

Pods with the preemption policy set to `Never` are placed in the scheduling queue ahead of lower-priority pods, but they cannot preempt other pods. A non-preempting pod waiting to be scheduled stays in the scheduling queue until sufficient resources are free and it can be scheduled. Non-preempting pods, like other pods, are subject to scheduler back-off. This means that if the scheduler tries unsuccessfully to schedule these pods, they are retried with lower frequency, allowing other pods with lower priority to be scheduled before them.

Non-preempting pods can still be preempted by other, high-priority pods.

## Pod preemption and other scheduler settings

If you enable pod priority and preemption, consider your other scheduler settings:

Pod priority and pod disruption budget
A pod disruption budget specifies the minimum number or percentage of replicas that must be up at a time. If you specify pod disruption budgets, OpenShift Container Platform respects them when preempting pods at a best effort level. The scheduler attempts to preempt pods without violating the pod disruption budget. If no such pods are found, lower-priority pods might be preempted despite their pod disruption budget requirements.

Pod priority and pod affinity
Pod affinity requires a new pod to be scheduled on the same node as other pods with the same label.

If a pending pod has inter-pod affinity with one or more of the lower-priority pods on a node, the scheduler cannot preempt the lower-priority pods without violating the affinity requirements. In this case, the scheduler looks for another node to schedule the pending pod. However, there is no guarantee that the scheduler can find an appropriate node and pending pod might not be scheduled.

To prevent this situation, carefully configure pod affinity with equal-priority pods.

## Graceful termination of preempted pods

When preempting a pod, the scheduler waits for the pod graceful termination period to expire, allowing the pod to finish working and exit. If the pod does not exit after the period, the scheduler kills the pod. This graceful termination period creates a time gap between the point that the scheduler preempts the pod and the time when the pending pod can be scheduled on the node.

To minimize this gap, configure a small graceful termination period for lower-priority pods.

# Configuring priority and preemption

Configure pod priority and preemption by creating priority class objects with assigned values and referencing them in pod specifications through the `priorityClassName` field.

> [!NOTE]
> You cannot add a priority class directly to an existing scheduled pod.

<div>

<div class="title">

Procedure

</div>

1.  Create one or more priority classes:

    1.  Create a YAML file similar to the following:

        ``` yaml
        apiVersion: scheduling.k8s.io/v1
        kind: PriorityClass
        metadata:
          name: high-priority
        value: 1000000
        preemptionPolicy: PreemptLowerPriority
        globalDefault: false
        description: "This priority class should be used for XYZ service pods only."
        ```

        where:

        `metadata.name`
        Specifies the name of the priority class object.

        `value`
        Specifies the priority value of the object.

        `preemptionPolicy`
        Optional. Specifies whether this priority class is preempting or non-preempting. The preemption policy defaults to `PreemptLowerPriority`, which allows pods of that priority class to preempt lower-priority pods. If the preemption policy is set to `Never`, pods in that priority class are non-preempting.

        `globalDefault`
        Optional. Specifies whether this priority class should be used for pods without a priority class name specified. This field is `false` by default. Only one priority class with `globalDefault` set to `true` can exist in the cluster. If there is no priority class with `globalDefault:true`, the priority of pods with no priority class name is zero. Adding a priority class with `globalDefault:true` affects only pods created after the priority class is added and does not change the priorities of existing pods.

        `description`
        Optional. Describes which pods developers should use with this priority class. Enter an arbitrary text string.

    2.  Create the priority class:

        ``` terminal
        $ oc create -f <file-name>.yaml
        ```

2.  Create a pod spec to include the name of a priority class:

    1.  Create a YAML file similar to the following:

        ``` yaml
        apiVersion: v1
        kind: Pod
        metadata:
          name: nginx
          labels:
            env: test
        spec:
          securityContext:
            runAsNonRoot: true
            seccompProfile:
              type: RuntimeDefault
          containers:
          - name: nginx
            image: nginx
            imagePullPolicy: IfNotPresent
            securityContext:
              allowPrivilegeEscalation: false
              capabilities:
                drop: [ALL]
          priorityClassName: high-priority
        ```

        where:

        `spec.priorityClassName`
        Specifies the priority class to use with this pod.

    2.  Create the pod:

        ``` terminal
        $ oc create -f <file-name>.yaml
        ```

    You can add the priority name directly to the pod configuration or to a pod template.

</div>
