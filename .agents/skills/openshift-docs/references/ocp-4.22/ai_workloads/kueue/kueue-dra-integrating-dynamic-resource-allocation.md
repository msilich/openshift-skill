<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure Red Hat build of Kueue to manage quota for workloads that use Dynamic Resource Allocation (DRA) to request GPUs. When DRA quota management is configured, Red Hat build of Kueue counts DRA device requests toward quota in the same way that it counts traditional resources such as CPU and memory.

> [!IMPORTANT]
> Kueue integration with Dynamic Resource Allocation (DRA) is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

If DRA device quota is not configured, Red Hat build of Kueue does not account for GPU requests when admitting workloads, which can result in teams exceeding their GPU allocation.

# DRA quota management overview

Dynamic Resource Allocation (DRA) is a Kubernetes framework that provides structured discovery and allocation of specialized hardware such as GPUs. DRA drivers publish device information through `ResourceSlice` objects, and administrators group devices into categories using `DeviceClass` objects.

Without Red Hat build of Kueue DRA integration, GPU requests made through DRA are invisible to quota management. Red Hat build of Kueue cannot account for these requests when admitting workloads, which can result in teams exceeding their GPU allocation.

Red Hat build of Kueue provides two approaches for managing DRA device quota:

`ResourceClaimTemplate`
The default approach. Workloads explicitly reference a `ResourceClaimTemplate` object that defines device requirements. Administrators configure `deviceClassMappings` in the Kueue CR to map each `DeviceClass` object to a logical resource name for quota tracking. Use this approach when workloads need fine-grained control over device selection, such as targeting a specific GPU model or architecture using CEL selectors.

`Extended resources`
A simplified alternative that allows workloads to use standard Kubernetes `resources.requests` syntax, for example, `nvidia.com/gpu: "1"`, instead of explicitly creating DRA objects. When a `DeviceClass` object includes the `spec.extendedResourceName` field, the Kubernetes scheduler automatically generates `ResourceClaim` objects. Use this approach when you want the simplest possible user experience and backward compatibility with existing workload YAML.

> [!NOTE]
> If a `DeviceClass` object with the `extendedResourceName` field also appears in a `deviceClassMappings` entry, Red Hat build of Kueue uses the mapped logical name from the `deviceClassMappings` entry for quota instead of the extended resource name, unifying quota accounting across both paths.

For clusters with partitionable devices, such as NVIDIA Multi-Instance GPU (MIG), Red Hat build of Kueue can also charge quota in capacity units, such as GPU memory, rather than device count. Partitionable devices use `ResourceClaimTemplates` objects with CEL selectors to target specific partition profiles, and require administrators to configure counter-based `sources` in `deviceClassMappings`. This capability requires OpenShift Container Platform 4.22 or later.

## Configuring the resource claim template path

You can configure Red Hat build of Kueue to manage quota for workloads that explicitly reference `ResourceClaimTemplate` objects. This requires configuring the `deviceClassMappings` entry in the Red Hat build of Kueue custom resource (CR) and adding the DRA resource to your `ClusterQueue` object.

<div>

<div class="title">

Prerequisites

</div>

- You have installed Red Hat build of Kueue by using the Red Hat Build of Kueue Operator.

- You have created a `Kueue` custom resource (CR).

- Your cluster is running OpenShift Container Platform 4.21 or later.

- A DRA driver is installed in the cluster, for example, `nvidia-dra-driver`. You can verify that the DRA driver is publishing device information by running the following command:

  ``` terminal
  $ oc get resourceslices
  ```

  If the command returns one or more `ResourceSlice` objects, the DRA driver is running.

- At least one `DeviceClass` object exists in the cluster. You can verify this by running the following command:

  ``` terminal
  $ oc get deviceclass
  ```

</div>

<div>

<div class="title">

Procedure

</div>

1.  Use the following command to add a `deviceClassMappings` entry to the Red Hat build of Kueue configuration that maps each `DeviceClass` to a logical resource name for quota:

    ``` yaml
    $ oc patch kueue cluster -n openshift-kueue-operator --type=merge -p '{
      "spec": {
        "config": {
          "resources": {
            "deviceClassMappings": [{
              "name": "nvidia.com/gpu",
              "deviceClassNames": ["gpu.nvidia.com"]
            }]
          }
        }
      }
    }'
    ```

    Replace `"nvidia.com/gpu"` with the resource name used in `ClusterQueue` quotas and `Workload` status.

    Replace `"gpu.nvidia.com"` with one or more `DeviceClass` names that map to this resource.

    Multiple device classes can map to the same logical resource name. For example, if you have separate device classes for different GPU models but want a single quota pool, as shown in the following example:

    ``` yaml
    resources:
      deviceClassMappings:
      - name: nvidia.com/gpu
        deviceClassNames:
        - gpu-a100.nvidia.com
        - gpu-h100.nvidia.com
    ```

2.  Create a file called `rct-queues.yaml` that contains the following content:

    <div class="formalpara">

    <div class="title">

    Example quota configuration for a `ResourceClaimTemplate` object

    </div>

    ``` yaml
    apiVersion: kueue.x-k8s.io/v1beta2
    kind: ResourceFlavor
    metadata:
      name: "default-flavor"
    ---
    apiVersion: kueue.x-k8s.io/v1beta2
    kind: ClusterQueue
    metadata:
      name: "cluster-queue"
    spec:
      namespaceSelector: {}
      resourceGroups:
      - coveredResources: ["cpu", "memory", "nvidia.com/gpu"]
        flavors:
        - name: "default-flavor"
          resources:
          - name: "cpu"
            nominalQuota: 40
          - name: "memory"
            nominalQuota: 200Gi
          - name: "nvidia.com/gpu"
            nominalQuota: 8
    ---
    apiVersion: kueue.x-k8s.io/v1beta2
    kind: LocalQueue
    metadata:
      namespace: "default"
      name: "user-queue"
    spec:
      clusterQueue: "cluster-queue"
    ```

    </div>

3.  Apply the `rct-queues.yaml` file:

    ``` terminal
    $ oc apply -f rct-queues.yaml
    ```

4.  Create a `ResourceClaimTemplate` object and a workload to verify the configuration. Create a file called `rct-job.yaml` by running the following command:

    ``` terminal
    $ oc create -f rct-job.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example `ResourceClaimTemplate` workload

    </div>

    ``` yaml
    apiVersion: resource.k8s.io/v1
    kind: ResourceClaimTemplate
    metadata:
      name: my-gpu
      namespace: default
    spec:
      spec:
        devices:
          requests:
          - name: gpu
            exactly:
              deviceClassName: gpu.nvidia.com
    ---
    apiVersion: batch/v1
    kind: Job
    metadata:
      generateName: rct-test-job-
      namespace: default
      labels:
        kueue.x-k8s.io/queue-name: user-queue
    spec:
      template:
        spec:
          restartPolicy: Never
          resourceClaims:
          - name: gpu
            resourceClaimTemplateName: my-gpu
          containers:
          - name: worker
            image: registry.k8s.io/e2e-test-images/agnhost:2.53
            args: ["pause"]
            resources:
              claims:
              - name: gpu
              requests:
                cpu: "1"
                memory: "200Mi"
    ```

    </div>

    where:

    `spec.spec.drivers.requests.exactly.deviceClassName:`
    References the `DeviceClass` object configured in the `deviceClassMappings` entry.

    `metadata.labels.kueue.x-k8s.io/queue-name:`
    Identifies the local queue to submit the job to.

    `spec.template.spec.resourceClaims.resourceClaimTemplateName:`
    References the `ResourceClaimTemplate` object defined above. The template must exist in the same namespace as the job.

    `spec.template.spec.containers.resources.claims.name:`
    Attaches the resource claim to this container.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the workload has been created and admitted:

    ``` terminal
    $ oc -n default get workloads
    ```

2.  Verify that a `ResourceClaim` object was created from the template:

    ``` terminal
    $ oc -n default get resourceclaims
    ```

    If the workload is not admitted, verify the following:

    - Check if the namespace is managed by Red Hat build of Kueue:

      ``` terminal
      $ oc label namespace default kueue.openshift.io/managed=true
      ```

    - The `deviceClassMappings` in the `Kueue` CR maps the `DeviceClass` object to the resource name in the `coveredResources` parameter.

    - The `ClusterQueue` object has sufficient quota available.

    - The `ResourceClaimTemplate` object exists in the same namespace as the job.

</div>

## Configuring the extended resources path

You can configure Red Hat build of Kueue to manage quota for workloads that request GPUs by using the standard `resources.requests` syntax, for example, `nvidia.com/gpu: "1"`.

When a `DeviceClass` object includes the `spec.extendedResourceName` field, the Kubernetes scheduler automatically generates `ResourceClaim` objects. This path does not require `deviceClassMappings` configuration because Red Hat build of Kueue auto-discovers the mapping by indexing `DeviceClass` objects.

> [!NOTE]
> The Red Hat build of Kueue Operator automatically enables the required Red Hat build of Kueue feature gates when it detects the `DRAExtendedResource` Kubernetes feature gate on the cluster. No manual Red Hat build of Kueue feature gate configuration is required.
>
> To use the extended resources path, you must enable the `DRAExtendedResource` Kubernetes feature gate. This feature is expected to be generally available in a future OpenShift Container Platform release.

<div>

<div class="title">

Prerequisites

</div>

- You have cluster administrator permissions.

- You have installed Red Hat build of Kueue by using the Red Hat Build of Kueue Operator.

- You have created a `Kueue` CR.

- Your cluster is running OpenShift Container Platform 4.21 or later.

- A DRA driver is installed in the cluster, for example, `nvidia-dra-driver`. You can verify that the DRA driver is publishing device information by running the following command:

  ``` terminal
  $ oc get resourceslices
  ```

  If the command returns one or more `ResourceSlice` objects, the DRA driver is running.

- At least one `DeviceClass` object exists in the cluster. You can verify this by running the following command:

  ``` terminal
  $ oc get deviceclass
  ```

- You have enabled the `DRAExtendedResource` Kubernetes feature gate by adding the `CustomNoUpgrade` feature set to the `FeatureGate` CR named `cluster`, as shown in the following example:

  ``` yaml
  apiVersion: config.openshift.io/v1
  kind: FeatureGate
  metadata:
    name: cluster
  spec:
    featureSet: CustomNoUpgrade
    customNoUpgrade:
      enabled:
      - DRAExtendedResource
  ```

  > [!WARNING]
  > Enabling the `CustomNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. This feature set is not supported on production clusters.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that the `DeviceClass` object has `spec.extendedResourceName` set by running the following command:

    ``` terminal
    $ oc get deviceclass gpu.nvidia.com -o jsonpath='{.spec.extendedResourceName}'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    nvidia.com/gpu
    ```

    </div>

    If the command does not return a value, add the `extendedResourceName` field by running the following command:

    ``` terminal
    $ oc patch deviceclass gpu.nvidia.com --type=merge -p '{"spec":{"extendedResourceName":"nvidia.com/gpu"}}'
    ```

2.  Create a `ClusterQueue` object that includes the GPU resource in the `coveredResources` parameter by creating a file called `er-queues.yaml`, as shown in the following example:

    <div class="formalpara">

    <div class="title">

    Example quota configuration for extended resources

    </div>

    ``` yaml
    apiVersion: kueue.x-k8s.io/v1beta2
    kind: ResourceFlavor
    metadata:
      name: "default-flavor"
    ---
    apiVersion: kueue.x-k8s.io/v1beta2
    kind: ClusterQueue
    metadata:
      name: "cluster-queue"
    spec:
      namespaceSelector: {}
      resourceGroups:
      - coveredResources: ["cpu", "memory", "nvidia.com/gpu"]
        flavors:
        - name: "default-flavor"
          resources:
          - name: "cpu"
            nominalQuota: 40
          - name: "memory"
            nominalQuota: 200Gi
          - name: "nvidia.com/gpu"
            nominalQuota: 8
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: team-a
      labels:
        kueue.openshift.io/managed: "true"
    ---
    apiVersion: kueue.x-k8s.io/v1beta2
    kind: LocalQueue
    metadata:
      namespace: "team-a"
      name: "user-queue"
    spec:
      clusterQueue: "cluster-queue"
    ```

    </div>

3.  Apply the quota configuration by running the following command:

    ``` terminal
    $ oc apply -f er-queues.yaml
    ```

4.  Create a workload that uses the standard resource request syntax by creating a file called `er-job.yaml`, as shown in the following example:

    <div class="formalpara">

    <div class="title">

    Example workload using extended resources

    </div>

    ``` yaml
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: er-test-job
      namespace: team-a
      labels:
        kueue.x-k8s.io/queue-name: user-queue
    spec:
      template:
        spec:
          containers:
          - name: worker
            image: registry.k8s.io/e2e-test-images/agnhost:2.53
            args: ["pause"]
            resources:
              requests:
                cpu: "1"
                memory: "200Mi"
                nvidia.com/gpu: "1"
              limits:
                nvidia.com/gpu: "1"
          restartPolicy: Never
    ```

    </div>

    where:

    `metadata.labels.kueue.x-k8s.io/queue-name`
    Identifies the local queue to submit the job to.

    `spec.template.spec.containers.resources.requests.cpu.nvidia.com/gpu`
    Requests a GPU by using the standard extended resource syntax. No `ResourceClaimTemplate` or `resourceClaims` section is needed. The `DeviceClass` object with the `spec.extendedResourceName` field causes the Kubernetes scheduler to generate a `ResourceClaim` object automatically.

    `spec.template.spec.containers.resources.limits.cpu.nvidia.com/gpu`
    Replace `"1"` with a GPU by using the standard extended resource syntax. No `ResourceClaimTemplate` or `resourceClaims` section is needed. The `DeviceClass` object with the `spec.extendedResourceName` field causes the Kubernetes scheduler to generate a `ResourceClaim` object automatically.

5.  Create the workload by running the following command:

    ``` terminal
    $ oc apply -f er-job.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that a workload has been created and admitted by running the following command:

    ``` terminal
    $ oc -n team-a get workloads
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                          QUEUE        RESERVED IN     ADMITTED   AGE
    job-er-test-job-4m2x-d3f4g   user-queue   cluster-queue   True       10s
    ```

    </div>

2.  Verify that a `ResourceClaim` was automatically created by running the following command:

    ``` terminal
    $ oc -n team-a get resourceclaims
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                         STATE                AGE
    er-test-job-jj7vz-extended-resources-bggzk   allocated,reserved   24s
    ```

    </div>

    The Kubernetes scheduler creates a `ResourceClaim` for each pod that requests an extended resource backed by a `DeviceClass`.

    If the workload is not admitted, verify the following:

    - The `DRAExtendedResource` Kubernetes feature gate is enabled on the cluster.

    - The `DeviceClass` has `spec.extendedResourceName` set.

    - The `ClusterQueue` includes the extended resource name in `coveredResources`.

    - The `ClusterQueue` has sufficient quota available.

</div>

## Configuring the partitionable devices

You can configure Red Hat build of Kueue to manage quota for partitionable devices based on actual device capacity rather than device count. Partitionable devices, such as NVIDIA Multi-Instance GPU (MIG) capable GPUs, allow a single GPU to be dynamically subdivided into smaller partitions.

When counter-based quota is configured, Red Hat build of Kueue charges quota in capacity units such as GPU memory rather than counting whole devices. For example, a `1g.5gb` MIG partition on an A100-40GB charges `4864Mi` of GPU memory quota, while a whole GPU charges `40320Mi`.

> [!NOTE]
> To use partitionable devices, your cluster must be running OpenShift Container Platform 4.22 or later and must have the `CustomNoUpgrade` feature set enabled with explicit `DRAPartitionableDevices` gate enablement.

<div>

<div class="title">

Prerequisites

</div>

- You have cluster administrator permissions.

- You have installed Red Hat build of Kueue by using the Red Hat Build of Kueue Operator.

- You have created a `Kueue` custom resource (CR).

- Your cluster is running OpenShift Container Platform 4.22 or later.

- A DRA driver that publishes `consumesCounters` in `ResourceSlice` objects is installed, for example, `nvidia-dra-driver`. You can verify that the DRA driver is publishing device information by running the following command:

  ``` terminal
  $ oc get resourceslices
  ```

  If the command returns one or more `ResourceSlice` objects, the DRA driver is running.

- At least one `DeviceClass` object exists in the cluster. You can verify this by running the following command:

  ``` terminal
  $ oc get deviceclass
  ```

- MIG is enabled on the GPU hardware.

- You have enabled the `DRAPartitionableDevices` Kubernetes feature gate by adding the `CustomNoUpgrade` feature set to the `FeatureGate` CR named `cluster`, as shown in the following example:

  ``` yaml
  apiVersion: config.openshift.io/v1
  kind: FeatureGate
  metadata:
    name: cluster
  spec:
    featureSet: CustomNoUpgrade
    customNoUpgrade:
      enabled:
      - DRAPartitionableDevices
  ```

  > [!WARNING]
  > Enabling the `CustomNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. This feature set is not supported on production clusters. For information about enabling feature gates, see "Enabling features using feature gates".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that your DRA driver publishes counter data by running the following command:

    ``` terminal
    $ oc get resourceslices -o jsonpath='{range .items[*]}{.spec.driver}{"\t"}{range .spec.devices[*]}: {"\n"}{end}{end}'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    gpu.nvidia.com   gpu-0: [{"counterSet":"shared","counters":{"memory":{"value":"40Gi"}}}]
    ```

    </div>

    If the output does not show `consumesCounters` data, verify that your DRA driver version supports partitionable devices and that MIG is enabled on the GPU hardware.

2.  Configure counter-based quota by adding a `deviceClassMappings` entry with a `sources` section to the `config.resources` section of the Red Hat build of Kueue CR, as shown in the following example:

    ``` yaml
    apiVersion: kueue.openshift.io/v1
    kind: Kueue
    metadata:
      name: cluster
      namespace: openshift-kueue-operator
    spec:
      config:
        resources:
          deviceClassMappings:
          - name: gpu.memory
            deviceClassNames:
            - gpu.nvidia.com
            - mig.nvidia.com
            sources:
            - type: Counter
              counter:
                name: memory
                driver: gpu.nvidia.com
                deviceSelector:
                  type: CEL
                  cel:
                    expression: "device.driver == 'gpu.nvidia.com'"
    # ...
    ```

    where:

    `spec.config.resources.deviceClassMappings.name`
    The logical resource name used in `ClusterQueue` quotas. When counter-based sources are configured, quota is charged in capacity units rather than device count.

    `spec.config.resources.deviceClassMappings.deviceClassNames`
    The `DeviceClass` names that map to this resource. Include both the whole-GPU class (`gpu.nvidia.com`) and the MIG class (`mig.nvidia.com`).

    `spec.config.resources.deviceClassMappings.sources`
    Defines how Red Hat build of Kueue computes the quota charge.

    `spec.config.resources.deviceClassMappings.sources.counter.name`
    The counter name must match a counter key published by the DRA driver in `ResourceSlice` devices.

    `spec.config.resources.deviceClassMappings.sources.counter.deviceSelector`
    Scopes which devices are eligible for counter-based quota accounting.

    > [!NOTE]
    > The Red Hat build of Kueue Operator automatically enables the required Red Hat build of Kueue feature gates when it detects the `DRAPartitionableDevices` Kubernetes feature gate and `sources` are configured in `deviceClassMappings`. No manual Red Hat build of Kueue feature gate configuration is required.

3.  Create a `ClusterQueue` object with counter-based quota. Set the quota in capacity units rather than device count. Create a file called `pd-queues.yaml` with the following content:

    <div class="formalpara">

    <div class="title">

    Example quota configuration for partitionable devices

    </div>

    ``` yaml
    apiVersion: kueue.x-k8s.io/v1beta2
    kind: ResourceFlavor
    metadata:
      name: "default-flavor"
    ---
    apiVersion: kueue.x-k8s.io/v1beta2
    kind: ClusterQueue
    metadata:
      name: "cluster-queue"
    spec:
      namespaceSelector: {}
      resourceGroups:
      - coveredResources: ["cpu", "memory", "gpu.memory"]
        flavors:
        - name: "default-flavor"
          resources:
          - name: "cpu"
            nominalQuota: 40
          - name: "memory"
            nominalQuota: 200Gi
          - name: "gpu.memory"
            nominalQuota: 800Gi
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: team-a
      labels:
        kueue.openshift.io/managed: "true"
    ---
    apiVersion: kueue.x-k8s.io/v1beta2
    kind: LocalQueue
    metadata:
      namespace: "team-a"
      name: "user-queue"
    spec:
      clusterQueue: "cluster-queue"
    ```

    </div>

    where:

    `spec.resourceGroups.coveredResources`
    The `gpu.memory` entry must match the `name` value in `deviceClassMappings`.

    `spec.resourceGroups.flavors.resources.name`
    Specify `"gpu.memory"` to set the total GPU memory quota. For example, `800Gi` accommodates twenty A100-40GB GPUs or equivalent MIG partitions.

    > [!NOTE]
    > When `ClusterQueue` objects share a cohort, ensure all queues use the same unit scale for counter resources. Red Hat build of Kueue does not validate unit consistency across `ClusterQueue` objects.

4.  Apply the quota configuration by running the following command:

    ``` terminal
    $ oc apply -f pd-queues.yaml
    ```

5.  Create a workload that requests a MIG partition by creating a file called `pd-job.yaml`, as shown in the following example:

    <div class="formalpara">

    <div class="title">

    Example workload requesting a MIG partition

    </div>

    ``` yaml
    apiVersion: resource.k8s.io/v1
    kind: ResourceClaimTemplate
    metadata:
      namespace: team-a
      name: gpu-partition
    spec:
      spec:
        devices:
          requests:
          - name: gpu
            exactly:
              deviceClassName: mig.nvidia.com
              count: 1
              selectors:
              - cel:
                  expression: "device.attributes['gpu.nvidia.com'].profile == '1g.5gb'"
    ---
    apiVersion: batch/v1
    kind: Job
    metadata:
      generateName: pd-test-job
      namespace: team-a
      labels:
        kueue.x-k8s.io/queue-name: user-queue
    spec:
      template:
        spec:
          containers:
          - name: worker
            image: registry.k8s.io/e2e-test-images/agnhost:2.53
            args: ["pause"]
            resources:
              claims:
              - name: gpu
              requests:
                cpu: "1"
                memory: "200Mi"
          resourceClaims:
          - name: gpu
            resourceClaimTemplateName: gpu-partition
          restartPolicy: Never
    ```

    </div>

    where:

    `spec.spec.devices.requests.exactly.deviceClassName`
    References the MIG `DeviceClass`.

    `spec.spec.devices.requests.exactly.selectors.cel.expression:`
    Selects a specific MIG partition profile. Available profiles depend on the GPU model, for example, `1g.5gb`, `2g.10gb`, `3g.20gb`, or `7g.40gb` for the A100-40GB.

    `metadata.labels.kueue.x-k8s.io/queue-name:`
    Identifies the local queue to submit the job to.

    `spec.template.spec.resourceClaims.resourceClaimTemplateName:`
    References the `ResourceClaimTemplate` defined above. The `ResourceClaimTemplate` must exist in the same namespace as the job.

6.  Create the workload by running the following command:

    ``` terminal
    $ oc create -f pd-job.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the workload is admitted and that quota was charged in capacity units by running the following command:

    ``` terminal
    $ oc -n team-a get workloads -o jsonpath='{range .items[*]}{.metadata.name}: {.status.admission.podSetAssignments[0].resourceUsage}{"\n"}{end}'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    job-pd-test-job-xxxxx: {"cpu":"1","gpu.memory":"5100273664","memory":"200Mi"}
    ```

    </div>

    The `gpu.memory` value reflects the actual memory capacity of the requested MIG partition rather than a device count of `1`.

2.  If the workload is not admitted, verify the following:

    - The `DRAPartitionableDevices` Kubernetes feature gate is enabled on the cluster.

    - The `name` value of the `deviceClassMappings` object matches the resource name in `coveredResources`.

    - The `counter.name` in `sources` matches a counter key in the `ResourceSlice` objects.

    - The `ClusterQueue` has sufficient GPU memory quota for the requested partition size.

    - MIG is enabled on the GPU hardware.

</div>

# Additional resources

- [Allocating GPUs to pods by using DRA](../../nodes/pods/nodes-pods-allocate-dra.md#nodes-pods-allocate-dra)

- [Configuring quotas](configuring-quotas.md#configuring-quotas)

- [Creating a Kueue custom resource](install-kueue.md#create-kueue-cr_install-kueue)

- [Enabling features using feature gates](../../nodes/clusters/nodes-cluster-enabling-features.md#nodes-cluster-enabling-features)
