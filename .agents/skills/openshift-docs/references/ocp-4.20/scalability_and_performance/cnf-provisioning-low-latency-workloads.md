<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If your organization needs high performance computing and low, predictable latency, especially in the financial and telecommunications industries, you can use the Node Tuning Operator to implement automatic tuning to achieve low latency performance and consistent response time for OpenShift Container Platform applications.

You use the performance profile configuration to make these changes.

You can update the kernel to kernel-rt, reserve CPUs for cluster and operating system housekeeping duties, including pod infra containers, isolate CPUs for application containers to run the workloads, and disable unused CPUs to reduce power consumption.

> [!NOTE]
> When writing your applications, follow the general recommendations described in [RHEL for Real Time processes and threads](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux_for_real_time/9/html-single/understanding_rhel_for_real_time/index#assembly_rhel-for-real-time-processes-and-threads_understanding-RHEL-for-Real-Time-core-concepts).

<div>

<div class="title">

Additional resources

</div>

- [Creating a performance profile](cnf-tuning-low-latency-nodes-with-perf-profile.md#cnf-create-performance-profiles_cnf-tuning-low-latency-nodes-with-perf-profile)

</div>

# Scheduling a low latency workload onto a compute node

You can schedule low latency workloads onto a compute node where a performance profile that configures real-time capabilities is applied.

> [!NOTE]
> To schedule a workload on specific nodes, use label selectors in the `Pod` custom resource (CR). The label selectors must match the nodes that are attached to the machine config pool that was configured for low latency by the Node Tuning Operator.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in as a user with `cluster-admin` privileges.

- You have applied a performance profile in the cluster that tunes compute nodes for low latency workloads.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `Pod` CR for the low latency workload and apply it in the cluster, for example:

    <div class="formalpara">

    <div class="title">

    Example `Pod` spec configured to use real-time processing

    </div>

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: dynamic-low-latency-pod
      annotations:
        cpu-quota.crio.io: "disable"
        cpu-load-balancing.crio.io: "disable"
        irq-load-balancing.crio.io: "disable"
    spec:
      securityContext:
        runAsNonRoot: true
        seccompProfile:
          type: RuntimeDefault
      containers:
      - name: dynamic-low-latency-pod
        image: "registry.redhat.io/openshift4/cnf-tests-rhel8:v4.17"
        command: ["sleep", "10h"]
        resources:
          requests:
            cpu: 2
            memory: "200M"
          limits:
            cpu: 2
            memory: "200M"
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop: [ALL]
      nodeSelector:
        node-role.kubernetes.io/worker-cnf: ""
      runtimeClassName: performance-dynamic-low-latency-profile
    # ...
    ```

    </div>

    where

    `metadata.annotations.cpu-quota.crio.io`
    Disables the CPU completely fair scheduler (CFS) quota at the pod run time.

    `metadata.annotations.cpu-load-balancing.crio.io`
    Disables CPU load balancing.

    `metadata.annotations.irq-load-balancing.crio.io`
    Opts the pod out of interrupt handling on the node.

    `spec.nodeSelector.node-role.kubernetes.io/worker-cnf`
    The `nodeSelector` label must match the label that you specify in the `Node` CR.

    `spec.runtimeClassName`
    `runtimeClassName` must match the name of the performance profile configured in the cluster.

2.  Enter the pod `runtimeClassName` in the form performance-\<profile_name\>, where \<profile_name\> is the `name` from the `PerformanceProfile` YAML. In the previous YAML example, the `name` is `performance-dynamic-low-latency-profile`.

3.  Ensure the pod is running correctly. Status should be `running`, and the correct `cnf-worker` node should be set.

    ``` terminal
    $ oc get pod -o wide
    ```

    <div class="formalpara">

    <div class="title">

    Expected output

    </div>

    ``` terminal
    NAME                     READY   STATUS    RESTARTS   AGE     IP           NODE
    dynamic-low-latency-pod  1/1     Running   0          5h33m   10.131.0.10  cnf-worker.example.com
    ```

    </div>

4.  Get the CPUs that the pod configured for IRQ dynamic load balancing runs on:

    ``` terminal
    $ oc exec -it dynamic-low-latency-pod -- /bin/bash -c "grep Cpus_allowed_list /proc/self/status | awk '{print $2}'"
    ```

    <div class="formalpara">

    <div class="title">

    Expected output

    </div>

    ``` terminal
    Cpus_allowed_list:  2-3
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

1.  Log in to the node to verify the configuration.

    ``` terminal
    $ oc debug node/<node-name>
    ```

2.  Verify that you can use the node file system:

    ``` terminal
    sh-4.4# chroot /host
    ```

    <div class="formalpara">

    <div class="title">

    Expected output

    </div>

    ``` terminal
    sh-4.4#
    ```

    </div>

3.  Ensure the default system CPU affinity mask does not include the `dynamic-low-latency-pod` CPUs, for example, CPUs 2 and 3.

    ``` terminal
    sh-4.4# cat /proc/irq/default_smp_affinity
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    33
    ```

    </div>

4.  Ensure the system IRQs are not configured to run on the `dynamic-low-latency-pod` CPUs:

    ``` terminal
    sh-4.4# find /proc/irq/ -name smp_affinity_list -exec sh -c 'i="$1"; mask=$(cat $i); file=$(echo $i); echo $file: $mask' _ {} \;
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    /proc/irq/0/smp_affinity_list: 0-5
    /proc/irq/1/smp_affinity_list: 5
    /proc/irq/2/smp_affinity_list: 0-5
    /proc/irq/3/smp_affinity_list: 0-5
    /proc/irq/4/smp_affinity_list: 0
    /proc/irq/5/smp_affinity_list: 0-5
    /proc/irq/6/smp_affinity_list: 0-5
    /proc/irq/7/smp_affinity_list: 0-5
    /proc/irq/8/smp_affinity_list: 4
    /proc/irq/9/smp_affinity_list: 4
    /proc/irq/10/smp_affinity_list: 0-5
    /proc/irq/11/smp_affinity_list: 0
    /proc/irq/12/smp_affinity_list: 1
    /proc/irq/13/smp_affinity_list: 0-5
    /proc/irq/14/smp_affinity_list: 1
    /proc/irq/15/smp_affinity_list: 0
    /proc/irq/24/smp_affinity_list: 1
    /proc/irq/25/smp_affinity_list: 1
    /proc/irq/26/smp_affinity_list: 1
    /proc/irq/27/smp_affinity_list: 5
    /proc/irq/28/smp_affinity_list: 1
    /proc/irq/29/smp_affinity_list: 0
    /proc/irq/30/smp_affinity_list: 0-5
    ```

    </div>

    > [!WARNING]
    > When you tune nodes for low latency, the usage of execution probes in conjunction with applications that require guaranteed CPUs can cause latency spikes. Use other probes, such as a properly configured set of network probes, as an alternative.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Placing pods on specific nodes using node selectors](../nodes/scheduling/nodes-scheduler-node-selectors.md#nodes-pods-node-selectors)

- [Assigning pods to nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node)

</div>

# Creating a pod with a guaranteed QoS class

You can create a pod with a quality of service (QoS) class of `Guaranteed` for high-performance workloads. Configuring a pod with a QoS class of `Guaranteed` ensures that the pod has priority access to the specified CPU and memory resources.

To create a pod with a QoS class of `Guaranteed`, you must apply the following specifications:

- Set identical values for the memory limit and memory request fields for each container in the pod.

- Set identical values for CPU limit and CPU request fields for each container in the pod.

In general, a pod with a QoS class of `Guaranteed` will not be evicted from a node. One exception is during resource contention caused by system daemons exceeding reserved resources. In this scenario, the `kubelet` might evict pods to preserve node stability, starting with the lowest priority pods.

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster as a user with the `cluster-admin` role.

- The OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a namespace for the pod by running the following command:

    ``` terminal
    $ oc create namespace qos-example
    ```

    - qos-example: Specifies a `qos-example` example namespace.

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      namespace/qos-example created
      ```

      </div>

2.  Create the `Pod` resource:

    1.  Create a YAML file that defines the `Pod` resource:

        <div class="formalpara">

        <div class="title">

        Example `qos-example.yaml` file

        </div>

        ``` yaml
        apiVersion: v1
        kind: Pod
        metadata:
          name: qos-demo
          namespace: qos-example
        spec:
          securityContext:
            runAsNonRoot: true
            seccompProfile:
              type: RuntimeDefault
          containers:
          - name: qos-demo-ctr
            image: quay.io/openshifttest/hello-openshift:openshift
            resources:
              limits:
                memory: "200Mi"
                cpu: "1"
              requests:
                memory: "200Mi"
                cpu: "1"
            securityContext:
              allowPrivilegeEscalation: false
              capabilities:
                drop: [ALL]
        ```

        </div>

        where:

        `spec.containers.image`
        Specifies public image, such as the `hello-openshift` image.

        `spec.containers.resources.limits.memory`
        Specifies a memory limit of 200 MB.

        `spec.containers.resources.limits.cpu`
        Specifies a CPU limit of 1 CPU.

        `spec.containers.resources.requests.memory`
        Specifies a memory request of 200 MB.

        `spec.containers.resources.requests.cpu`
        Specifies a CPU request of 1 CPU.

        > [!NOTE]
        > If you specify a memory limit for a container, but do not specify a memory request, OpenShift Container Platform automatically assigns a memory request that matches the limit. Similarly, if you specify a CPU limit for a container, but do not specify a CPU request, OpenShift Container Platform automatically assigns a CPU request that matches the limit.

    2.  Create the `Pod` resource by running the following command:

        ``` terminal
        $ oc apply -f qos-example.yaml --namespace=qos-example
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        pod/qos-demo created
        ```

        </div>

</div>

<div>

<div class="title">

Verification

</div>

- View the `qosClass` value for the pod by running the following command:

  ``` terminal
  $ oc get pod qos-demo --namespace=qos-example --output=yaml | grep qosClass
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` yaml
      qosClass: Guaranteed
  ```

  </div>

</div>

# Disabling CPU load balancing in a Pod

Functionality to disable or enable CPU load balancing is implemented on the CRI-O level. Before CRI-O disables or enables CPU load balancing, you must ensure certain prerequisites are met.

The pod must use the `performance-<profile-name>` runtime class. You can get the proper name by looking at the status of the performance profile, as shown here:

``` yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
...
status:
  ...
  runtimeClass: performance-manual
```

The Node Tuning Operator is responsible for the creation of the high-performance runtime handler config snippet under relevant nodes and for creation of the high-performance runtime class under the cluster. It will have the same content as the default runtime handler except that it enables the CPU load balancing configuration functionality.

To disable the CPU load balancing for the pod, the `Pod` specification must include the following fields:

``` yaml
apiVersion: v1
kind: Pod
metadata:
  #...
  annotations:
    #...
    cpu-load-balancing.crio.io: "disable"
    #...
  #...
spec:
  #...
  runtimeClassName: performance-<profile_name>
  #...
```

> [!NOTE]
> Only disable CPU load balancing when the CPU manager static policy is enabled and for pods with guaranteed QoS that use whole CPUs. Otherwise, disabling CPU load balancing can affect the performance of other containers in the cluster.

# Disabling power saving mode for high priority pods

To protect high priority workloads when using power saving configurations on a node, apply performance settings at the pod level. This ensures that the configuration applies to all cores used by the pod, maintaining performance stability.

By disabling P-states and C-states at the pod level, you can configure high priority workloads for best performance and lowest latency.

<table>
<caption>Configuration for high priority workloads</caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 33%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Annotation</th>
<th style="text-align: left;">Possible Values</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>cpu-c-states.crio.io:</code></p></td>
<td style="text-align: left;"><ul>
<li><p><code>"enable"</code></p></li>
<li><p><code>"disable"</code></p></li>
<li><p><code>"max_latency:microseconds"</code></p></li>
</ul></td>
<td style="text-align: left;"><p>This annotation allows you to enable or disable C-states for each CPU. Alternatively, you can also specify a maximum latency in microseconds for the C-states. For example, enable C-states with a maximum latency of 10 microseconds with the setting <code>cpu-c-states.crio.io</code>: <code>"max_latency:10"</code>. Set the value to <code>"disable"</code> to provide the best performance for a pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cpu-freq-governor.crio.io:</code></p></td>
<td style="text-align: left;"><p>Any supported <code>cpufreq governor</code>.</p></td>
<td style="text-align: left;"><p>Sets the <code>cpufreq</code> governor for each CPU. The <code>"performance"</code> governor is recommended for high priority workloads.</p></td>
</tr>
</tbody>
</table>

<div>

<div class="title">

Prerequisites

</div>

- You have configured power saving in the performance profile for the node where the high priority workload pods are scheduled.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Add the required annotations to your high priority workload pods. The annotations override the `default` settings.

    <div class="formalpara">

    <div class="title">

    Example high priority workload annotation

    </div>

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      #...
      annotations:
        #...
        cpu-c-states.crio.io: "disable"
        cpu-freq-governor.crio.io: "performance"
        #...
      #...
    spec:
      #...
      runtimeClassName: performance-<profile_name>
      #...
    ```

    </div>

2.  Restart the pods to apply the annotation.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring power saving for nodes that run colocated high and low priority workloads](cnf-tuning-low-latency-nodes-with-perf-profile.md#cnf-configuring-power-saving-for-nodes_cnf-tuning-low-latency-nodes-with-perf-profile)

</div>

# Disabling CPU CFS quota

To eliminate CPU throttling for pinned pods, create a pod with the `cpu-quota.crio.io: "disable"` annotation. This annotation disables the CPU completely fair scheduler (CFS) quota when the pod runs.

<div>

<div class="title">

Procedure

</div>

- To eliminate CPU throttling for pinned pods, create a pod with the `cpu-quota.crio.io: "disable"` annotation. This annotation disables the CPU completely fair scheduler (CFS) quota when the pod runs.

  <div class="formalpara">

  <div class="title">

  Example pod specification with `cpu-quota.crio.io` disabled

  </div>

  ``` yaml
  apiVersion: v1
  kind: Pod
  metadata:
    annotations:
        cpu-quota.crio.io: "disable"
  spec:
      runtimeClassName: performance-<profile_name>
  #...
  ```

  </div>

  > [!NOTE]
  > Only disable CPU CFS quota when the CPU manager static policy is enabled and for pods with guaranteed QoS that use whole CPUs. For example, pods that contain CPU-pinned containers. Otherwise, disabling CPU CFS quota can affect the performance of other containers in the cluster.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Recommended firmware configuration for vDU cluster hosts](../edge_computing/ztp-vdu-validating-cluster-tuning.md#ztp-du-firmware-config-reference_vdu-config-ref)

</div>

# Disabling interrupt processing for CPUs where pinned containers are running

To achieve low latency for workloads, some containers require that the CPUs they are pinned to do not process device interrupts. You can use the `irq-load-balancing.crio.io` pod annotation to control whether device interrupts are processed on CPUs where the pinned containers are running.

To disable interrupt processing for CPUs where containers belonging to individual pods are pinned, ensure that `globallyDisableIrqLoadBalancing` is set to `false` in the performance profile. In the pod specification, set the `irq-load-balancing.crio.io` pod annotation to `disable`, as demonstrated in the following example:

``` yaml
apiVersion: performance.openshift.io/v2
kind: Pod
metadata:
  annotations:
      irq-load-balancing.crio.io: "disable"
spec:
    runtimeClassName: performance-<profile_name>
...
```

<div>

<div class="title">

Additional resources

</div>

- [Managing device interrupt processing for guaranteed pod isolated CPUs](cnf-tuning-low-latency-nodes-with-perf-profile.md#managing-device-interrupt-processing-for-guaranteed-pod-isolated-cpus_cnf-tuning-low-latency-nodes-with-perf-profile)

</div>
