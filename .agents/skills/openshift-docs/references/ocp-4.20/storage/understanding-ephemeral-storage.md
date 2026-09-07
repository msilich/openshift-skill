<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Ephemeral storage provides temporary per-pod storage for scratch data, caches, and logs that do not persist beyond the pod’s lifetime. Understanding different ephemeral storage types and resource management helps you choose options for stateless workloads while preventing node storage exhaustion.

# Overview of ephemeral storage

Use ephemeral storage to provide temporary local storage for stateless applications that only need data for the duration of the pod lifecycle, such as caches, scratch files, and logs that do not need to persist after the pod terminates.

Both developers and administrators can use this feature.

Pods and containers can require ephemeral or transient local storage for their operation. The lifetime of this ephemeral storage does not extend beyond the life of the individual pod, and this ephemeral storage cannot be shared across pods.

Issues related to the lack of local storage accounting and isolation include the following:

- Pods cannot detect how much local storage is available to them.

- Pods cannot request guaranteed local storage.

- Local storage is a best-effort resource.

- Pods can be evicted due to other pods filling the local storage, after which new pods are not admitted until sufficient storage is reclaimed.

Unlike persistent volumes, ephemeral storage is unstructured and the space is shared between all pods running on a node, in addition to other uses by the system, the container runtime, and OpenShift Container Platform. The ephemeral storage framework allows pods to specify their transient local storage needs. It also allows OpenShift Container Platform to schedule pods where appropriate, and to protect the node against excessive use of local storage.

While the ephemeral storage framework allows administrators and developers to better manage local storage, I/O throughput and latency are not directly affected.

# Types of ephemeral storage

Provision ephemeral local storage by creating the primary partition using either root or runtime methods. Choose the method that aligns with your node configuration to ensure temporary storage is available for your workloads.

Root
This partition holds the kubelet root directory, `/var/lib/kubelet/` by default, and `/var/log/` directory. This partition can be shared between user pods, the operating system, and Kubernetes system daemons. This partition can be consumed by pods through `EmptyDir` volumes, container logs, image layers, and container-writable layers. Kubelet manages shared access and isolation of this partition. This partition is ephemeral, and applications cannot expect any performance SLAs, such as disk IOPS, from this partition.

Runtime
This is an optional partition that runtimes can use for overlay file systems. OpenShift Container Platform attempts to identify and provide shared access along with isolation to this partition. Container image layers and writable layers are stored here. If the runtime partition exists, the `root` partition does not hold any image layer or other writable storage.

# Ephemeral storage management overview

Cluster administrators can manage ephemeral storage within a project by setting quotas that define limit ranges and request counts for all pods in a non-terminal state. Developers can also set requests and limits on this resource at the pod and container level.

You can manage local ephemeral storage by specifying requests and limits. Each container in a pod can specify the following:

- `spec.containers[].resources.limits.ephemeral-storage`

- `spec.containers[].resources.requests.ephemeral-storage`

## Ephemeral storage management limits and requests

Express ephemeral storage limits and requests using byte quantities with suffixes like G, M, K or power-of-two equivalents Gi, Mi, Ki. Pod-level limits aggregate all container limits plus `emptyDir` volumes, enabling proper scheduling and preventing pods from exhausting node storage.

Limits and requests for ephemeral storage are measured in byte quantities. You can express storage as a plain integer or as a fixed-point number by using one of these suffixes: E, P, T, G, M, K. You can also use the power-of-two equivalents: Ei, Pi, Ti, Gi, Mi, Ki. For example, the following quantities all represent approximately the same value: 128974848, 129e6, 129M, and 123Mi. Pod-level limits aggregate all container limits plus `emptyDir` volumes, enabling proper scheduling and preventing pods from exhausting node storage.

> [!IMPORTANT]
> The suffixes for each byte quantity are case-sensitive. Be sure to use the correct case. Use the case-sensitive "M", such as used in "400M", to set the request at 400 megabytes. Use the case-sensitive "400Mi" to request 400 mebibytes. If you specify "400m" of ephemeral storage, the storage request is only 0.4 bytes.

The following example configuration file shows a pod with two containers:

- Each container requests 2GiB of local ephemeral storage.

- Each container has a limit of 4GiB of local ephemeral storage.

- At the pod level, kubelet works out an overall pod storage limit by adding up the limits of all the containers in that pod.

  - In this case, the total storage usage at the pod level is the sum of the disk usage from all containers plus the `emptyDir` volumes of a pod.

  - Therefore, the pod has a request of 4GiB of local ephemeral storage, and a limit of 8GiB of local ephemeral storage.

<div class="formalpara">

<div class="title">

Example ephemeral storage configuration with quotas and limits

</div>

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: frontend
spec:
  containers:
  - name: app
    image: images.my-company.example/app:v4
    resources:
      requests:
        ephemeral-storage: "2Gi"
      limits:
        ephemeral-storage: "4Gi"
    volumeMounts:
    - name: ephemeral
      mountPath: "/tmp"
  - name: log-aggregator
    image: images.my-company.example/log-aggregator:v6
    resources:
      requests:
        ephemeral-storage: "2Gi"
      limits:
        ephemeral-storage: "4Gi"
    volumeMounts:
    - name: ephemeral
      mountPath: "/tmp"
  volumes:
    - name: ephemeral
      emptyDir: {}
```

</div>

- `spec.containers.name.resources.requests.ephemeral-storage`: Specifies the container request for local ephemeral storage.

- `spec.containers.name.resources.limits.ephemeral-storage`: Specifies the container limit for local ephemeral storage.

<div>

<div class="title">

Additional resources

</div>

- [Resources managed by quotas](../applications/quotas/quotas-setting-per-project.md#quotas-setting-per-project_quotas-setting-per-project)

</div>

## Ephemeral storage management configuration affects pod scheduling and eviction

Configure ephemeral storage requests and limits in the pod spec to control how the scheduler places pods on nodes and when kubelet evicts pods that exceed their allocated storage.

- First, the scheduler ensures that the sum of the resource requests of the scheduled containers is less than the capacity of the node. In this case, the pod can be assigned to a node only if the node’s available ephemeral storage (allocatable resource) is more than 4GiB.

- Second, at the container level, because the first container sets a resource limit, kubelet eviction manager measures the disk usage of this container and evicts the pod if the storage usage of the container exceeds its limit (4GiB). The kubelet eviction manager also marks the pod for eviction if the total usage exceeds the overall pod storage limit (8GiB).

# Monitoring ephemeral storage

Monitor ephemeral storage usage with the `/bin/df` utility to track disk space consumption on `/var/lib/kubelet` and `/var/lib/containers`. Regular monitoring helps you identify storage-hungry workloads and adjust resource limits before kubelet evicts pods due to storage exhaustion.

When you use the `df` command, the available space for only `/var/lib/kubelet` is shown if `/var/lib/containers` is placed on a separate disk by the cluster administrator.

You can use `/bin/df` as a tool to monitor ephemeral storage usage on the volume where ephemeral container data is located, which is `/var/lib/kubelet` and `/var/lib/containers`. The available space for only `/var/lib/kubelet` is shown when you use the `df` command if `/var/lib/containers` is placed on a separate disk by the cluster administrator.

<div>

<div class="title">

Procedure

</div>

- To show the human-readable values of used and available space in `/var/lib`, run the following command:

  ``` terminal
  $ df -h /var/lib
  ```

  The output shows the ephemeral storage usage in `/var/lib`:

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  Filesystem  Size  Used Avail Use% Mounted on
  /dev/disk/by-partuuid/4cd1448a-01    69G   32G   34G  49% /
  ```

  </div>

</div>
