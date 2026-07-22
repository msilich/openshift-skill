<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

After you deploy a hosted cluster on OpenShift Virtualization, you can manage the cluster.

# Accessing the hosted cluster

You can access the hosted cluster by either getting the `kubeconfig` file and `kubeadmin` credential directly from resources, or by using the `hcp` command-line interface to generate a `kubeconfig` file.

<div class="formalpara">

<div class="title">

Prerequisites

</div>

To access the hosted cluster by getting the `kubeconfig` file and credentials directly from resources, you must be familiar with the access secrets for hosted clusters. The *hosted cluster (hosting)* namespace has hosted cluster resources and the access secrets. The *hosted control plane* namespace is where the hosted control plane runs.

</div>

The secret name formats are as follows:

- `kubeconfig` secret: `<hosted_cluster_namespace>-<name>-admin-kubeconfig` (clusters-hypershift-demo-admin-kubeconfig)

- `kubeadmin` password secret: `<hosted_cluster_namespace>-<name>-kubeadmin-password` (clusters-hypershift-demo-kubeadmin-password)

The `kubeconfig` secret has a Base64-encoded `kubeconfig` field, which you can decode and save into a file to use with the following command:

``` terminal
$ oc --kubeconfig <hosted_cluster_name>.kubeconfig get nodes
```

The `kubeadmin` password secret is also Base64-encoded. You can decode it and use the password to log in to the API server or console of the hosted cluster.

To access the hosted cluster by using the `hcp` CLI to generate the `kubeconfig` file, take the following steps.

<div>

<div class="title">

Procedure

</div>

1.  Generate the `kubeconfig` file by entering the following command:

    ``` terminal
    $ hcp create kubeconfig --namespace <hosted_cluster_namespace> \
      --name <hosted_cluster_name> > <hosted_cluster_name>.kubeconfig
    ```

2.  After you save the `kubeconfig` file, you can access the hosted cluster by entering the following example command:

    ``` terminal
    $ oc --kubeconfig <hosted_cluster_name>.kubeconfig get nodes
    ```

</div>

# Enabling node auto-scaling for the hosted cluster

When you need more capacity in your hosted cluster and spare agents are available, you can enable auto-scaling to install new worker nodes.

<div>

<div class="title">

Procedure

</div>

1.  To enable auto-scaling, enter the following command:

    ``` terminal
    $ oc -n <hosted_cluster_namespace> patch nodepool <hosted_cluster_name> \
      --type=json \
      -p '[{"op": "remove", "path": "/spec/replicas"},{"op":"add", "path": "/spec/autoScaling", "value": { "max": 5, "min": 2 }}]'
    ```

    > [!NOTE]
    > In the example, the minimum number of nodes is 2, and the maximum is 5. The maximum number of nodes that you can add might be bound by your platform. For example, if you use the Agent platform, the maximum number of nodes is bound by the number of available agents.

2.  Create a workload that requires a new node.

    1.  Create a YAML file that has the workload configuration, by using the following example:

        ``` yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          creationTimestamp: null
          labels:
            app: reversewords
          name: reversewords
          namespace: default
        spec:
          replicas: 40
          selector:
            matchLabels:
              app: reversewords
          strategy: {}
          template:
            metadata:
              creationTimestamp: null
              labels:
                app: reversewords
            spec:
              containers:
              - image: quay.io/mavazque/reversewords:latest
                name: reversewords
                resources:
                  requests:
                    memory: 2Gi
        status: {}
        ```

    2.  Save the file as `workload-config.yaml`.

    3.  Apply the YAML by entering the following command:

        ``` terminal
        $ oc apply -f workload-config.yaml
        ```

3.  Extract the `admin-kubeconfig` secret by entering the following command:

    ``` terminal
    $ oc extract -n <hosted_cluster_namespace> \
      secret/<hosted_cluster_name>-admin-kubeconfig \
      --to=./hostedcluster-secrets --confirm
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

        hostedcluster-secrets/kubeconfig

    </div>

4.  You can check if new nodes are in the `Ready` status by entering the following command:

    ``` terminal
    $ oc --kubeconfig ./hostedcluster-secrets get nodes
    ```

5.  To remove the node, delete the workload by entering the following command:

    ``` terminal
    $ oc --kubeconfig ./hostedcluster-secrets -n <namespace> \
      delete deployment <deployment_name>
    ```

6.  Wait for several minutes to pass without requiring the additional capacity. On the Agent platform, the agent is decommissioned and can be reused. You can confirm that the node was removed by entering the following command:

    ``` terminal
    $ oc --kubeconfig ./hostedcluster-secrets get nodes
    ```

    > [!NOTE]
    > For IBM Z® agents, if you are using an OSA network device in Processor Resource/Systems Manager (PR/SM) mode, auto scaling is not supported. You must delete the old agent manually and scale up the node pool because the new agent joins during the scale down process.

</div>

# Storage for hosted control planes on OpenShift Virtualization

If you do not provide any advanced storage configuration, the default storage class is used for the KubeVirt virtual machine (VM) images, the KubeVirt Container Storage Interface (CSI) mapping, and the etcd volumes.

The following table lists the capabilities that the infrastructure must provide to support persistent storage in a hosted cluster:

<table>
<caption>Persistent storage modes in a hosted cluster</caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Infrastructure CSI provider</th>
<th style="text-align: left;">Hosted cluster CSI provider</th>
<th style="text-align: left;">Hosted cluster capabilities</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Any RWX <code>Block</code> CSI provider</p></td>
<td style="text-align: left;"><p><code>kubevirt-csi</code></p></td>
<td style="text-align: left;"><ul>
<li><p>Basic RWO <code>Block</code> and <code>File</code></p></li>
<li><p>Basic RWX <code>Block</code> and <code>Snapshot</code></p></li>
<li><p>CSI volume cloning</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>Any RWX <code>Block</code> CSI provider</p></td>
<td style="text-align: left;"><p>Red Hat OpenShift Data Foundation</p></td>
<td style="text-align: left;"><p>Red Hat OpenShift Data Foundation feature set. External mode has a smaller footprint and uses a standalone Red Hat Ceph Storage. Internal mode has a larger footprint, but is self-contained and suitable for use cases that require expanded capabilities such as RWX <code>File</code>.</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> OpenShift Virtualization handles storage on hosted clusters, which especially helps customers whose requirements are limited to block storage.

## Mapping KubeVirt CSI storage classes

You can map the infrastructure storage class to the hosted storage class during cluster creation.

> [!NOTE]
> KubeVirt CSI supports mapping only an infrastructure storage class that is capable of `ReadWriteMany` (RWX) access.

The following table shows how volume and access mode capabilities map to KubeVirt CSI storage classes:

| Infrastructure CSI capability | Hosted cluster CSI capability | VM live migration support | Notes |
|----|----|----|----|
| RWX: `Block` or `Filesystem` | `ReadWriteOnce` (RWO) `Block` or `Filesystem` RWX `Block` only | Supported | Use `Block` mode because `Filesystem` volume mode results in degraded hosted `Block` mode performance. RWX `Block` volume mode is supported only when the hosted cluster is OpenShift Container Platform 4.16 or later. |
| RWO `Block` storage | RWO `Block` storage or `Filesystem` | Not supported | Lack of live migration support affects the ability to update the underlying infrastructure cluster that hosts the KubeVirt VMs. |
| RWO `FileSystem` | RWO `Block` or `Filesystem` | Not supported | Lack of live migration support affects the ability to update the underlying infrastructure cluster that hosts the KubeVirt VMs. Use of the infrastructure `Filesystem` volume mode results in degraded hosted `Block` mode performance. |

Mapping KubeVirt CSI storage classes to access and volume modes

<div>

<div class="title">

Procedure

</div>

- To map the infrastructure storage class to the hosted storage class, use the `--infra-storage-class-mapping` argument as shown in the following example:

  ``` terminal
  $ hcp create cluster kubevirt \
    --name my-hosted-cluster \
    --node-pool-replicas 2 \
    --pull-secret /user/name/pullsecret \
    --memory 8Gi \
    --cores 2 \
    --infra-storage-class-mapping=<infrastructure_storage_class>/<hosted_storage_class>
  ```

  - `--name` specifies the name of your hosted cluster.

  - `--node-pool-replicas` specifies the worker count.

  - `--pull-secret` specifies the path to your pull secret.

  - `--memory` specifies a value for memory.

  - `--cores` specifies a value for CPU.

  - `--infra-storage-class-mapping` specifies the storage class names for the infrastructure and hosted cluster. Replace `<infrastructure_storage_class>` with the infrastructure storage class name and `<hosted_storage_class>` with the hosted cluster storage class name. You can use the `--infra-storage-class-mapping` argument multiple times within the `hcp create cluster` command.

    After you create the hosted cluster, the infrastructure storage class is visible within the hosted cluster. When you create a Persistent Volume Claim (PVC) within the hosted cluster that uses one of those storage classes, KubeVirt CSI provisions that volume by using the infrastructure storage class mapping that you configured during cluster creation.

</div>

## Mapping a single KubeVirt CSI volume snapshot class

You can expose your infrastructure volume snapshot class to the hosted cluster by using KubeVirt CSI.

<div>

<div class="title">

Procedure

</div>

- To map your volume snapshot class to the hosted cluster, use the `--infra-volumesnapshot-class-mapping` argument when creating a hosted cluster as shown in the following example:

  ``` terminal
  $ hcp create cluster kubevirt \
    --name my-hosted-cluster \
    --node-pool-replicas 2 \
    --pull-secret /user/name/pullsecret \
    --memory 8Gi \
    --cores 2 \
    --infra-storage-class-mapping=<infrastructure_storage_class>/<hosted_storage_class> \
    --infra-volumesnapshot-class-mapping=<infrastructure_volume_snapshot_class>/<hosted_volume_snapshot_class>
  ```

  - `--name` specifies the name of your hosted cluster.

  - `--node-pool-replicas` specifies the worker count.

  - `--pull-secret` specifies the path to your pull secret.

  - `--memory` specifies a value for memory.

  - `--cores` specifies a value for CPU.

  - `--infra-storage-class-mapping` specifies the storage classes. Replace `<infrastructure_storage_class>` with the storage class in the infrastructure cluster, and replace `<hosted_storage_class>` with the storage class in the hosted cluster.

  - `--infra-volumesnapshot-class-mapping` specifies the volume snapshot classes. Replace `<infrastructure_volume_snapshot_class>` with the volume snapshot class in the infrastructure cluster, and replace `<hosted_volume_snapshot_class>` with the volume snapshot class in the hosted cluster.

    > [!NOTE]
    > If you do not use the `--infra-storage-class-mapping` and `--infra-volumesnapshot-class-mapping` arguments, a hosted cluster is created with the default storage class and the volume snapshot class. Therefore, you must set the default storage class and the volume snapshot class in the infrastructure cluster.

</div>

## Mapping multiple KubeVirt CSI volume snapshot classes

You can map multiple volume snapshot classes to the hosted cluster by assigning them to a specific group. The infrastructure storage class and the volume snapshot class are compatible with each other only if they belong to a same group.

<div>

<div class="title">

Procedure

</div>

- To map multiple volume snapshot classes to the hosted cluster, use the `group` option when creating a hosted cluster, as shown in the following example:

  ``` terminal
  $ hcp create cluster kubevirt \
    --name my-hosted-cluster \
    --node-pool-replicas 2 \
    --pull-secret /user/name/pullsecret \
    --memory 8Gi \
    --cores 2 \
    --infra-storage-class-mapping=<infrastructure_storage_class>/<hosted_storage_class>,group=<group_name> \
    --infra-storage-class-mapping=<infrastructure_storage_class>/<hosted_storage_class>,group=<group_name> \
    --infra-storage-class-mapping=<infrastructure_storage_class>/<hosted_storage_class>,group=<group_name> \
    --infra-volumesnapshot-class-mapping=<infrastructure_volume_snapshot_class>/<hosted_volume_snapshot_class>,group=<group_name> \
    --infra-volumesnapshot-class-mapping=<infrastructure_volume_snapshot_class>/<hosted_volume_snapshot_class>,group=<group_name>
  ```

  - `--name` specifies the name of your hosted cluster.

  - `--node-pool-replicas` specifies the worker count.

  - `--pull-secret` specifies the path to your pull secret.

  - `--memory` specifies a value for memory.

  - `--cores` specifies a value for CPU.

  - `--infra-storage-class-mapping` specifies the storage classes. Replace `<infrastructure_storage_class>` with the storage class in the infrastructure cluster, `<hosted_storage_class>` with the storage class in the hosted cluster, and `<group_name>` with the group name. For example, `infra-storage-class-mygroup/hosted-storage-class-mygroup,group=mygroup` and `infra-storage-class-mymap/hosted-storage-class-mymap,group=mymap`.

  - `--infra-volumesnapshot-class-mapping` specifies the volume snapshot classes. Replace `<infrastructure_volume_snapshot_class>` with the volume snapshot class in the infrastructure cluster and `<hosted_volume_snapshot_class>` with the volume snapshot class in the hosted cluster. For example, `infra-vol-snap-mygroup/hosted-vol-snap-mygroup,group=mygroup` and `infra-vol-snap-mymap/hosted-vol-snap-mymap,group=mymap`.

</div>

## Configuring KubeVirt VM root volume

At cluster creation time, you can configure the storage class that is used to host the KubeVirt virtual machine (VM) root volumes by using the `--root-volume-storage-class` argument.

<div>

<div class="title">

Procedure

</div>

- To set a custom storage class and volume size for KubeVirt VMs, run a command as shown in the following example:

  ``` terminal
  $ hcp create cluster kubevirt \
    --name my-hosted-cluster \
    --node-pool-replicas 2 \
    --pull-secret /user/name/pullsecret \
    --memory 8Gi \
    --cores 2 \
    --root-volume-storage-class ocs-storagecluster-ceph-rbd \
    --root-volume-size 64
  ```

  - `--name` specifies the name of your hosted cluster.

  - `--node-pool-replicas` specifies the worker count.

  - `--pull-secret` specifies the path to your pull secret.

  - `--memory` specifies a value for memory.

  - `--cores` specifies a value for CPU.

  - `--root-volume-storage-class` specifies a name of the storage class to host the KubeVirt VM root volumes.

  - `--root-volume-size` specifies the volume size.

    As a result, you get a hosted cluster created with VMs hosted on persistent volume claims (PVCs).

</div>

## Enabling KubeVirt VM image caching

To optimize both cluster startup time and storage usage, you can use KubeVirt virtual machine (VM) image caching.

KubeVirt VM image caching supports the use of a storage class that is capable of smart cloning and the `ReadWriteMany` access mode. For more information about smart cloning, see "Cloning a data volume using smart-cloning".

Image caching works as follows:

1.  The VM image is imported to a persistent volume claim (PVC) that is associated with the hosted cluster.

2.  A unique clone of that PVC is created for every KubeVirt VM that is added as a worker node to the cluster.

Image caching reduces VM startup time by requiring only a single image import. It can further reduce overall cluster storage usage when the storage class supports copy-on-write cloning.

<div>

<div class="title">

Procedure

</div>

- To enable image caching, during cluster creation, use the `--root-volume-cache-strategy=PVC` argument by running a command as shown in the following example:

  ``` terminal
  $ hcp create cluster kubevirt \
    --name my-hosted-cluster \
    --node-pool-replicas 2 \
    --pull-secret /user/name/pullsecret \
    --memory 8Gi \
    --cores 2 \
    --root-volume-cache-strategy=PVC
  ```

  - `--name` specifies the name of your hosted cluster.

  - `--node-pool-replicas` specifies the worker count.

  - `--pull-secret` specifies the path to your pull secret.

  - `--memory` specifies a value for memory.

  - `--cores` specifies a value for CPU.

  - `--root-volume-cache-strategy` specifies a strategy for image caching.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Cloning a data volume using smart-cloning](../../virt/creating_vms_advanced/virt-creating-vms-by-cloning-pvcs.md#smart-cloning_virt-creating-vms-by-cloning-pvcs)

</div>

## KubeVirt CSI storage security and isolation

KubeVirt Container Storage Interface (CSI) extends the storage capabilities of the underlying infrastructure cluster to hosted clusters.

The CSI driver ensures secure and isolated access to the infrastructure storage classes and hosted clusters by using the following security constraints:

- The storage of a hosted cluster is isolated from the other hosted clusters.

- Compute nodes in a hosted cluster do not have a direct API access to the infrastructure cluster. The hosted cluster can provision storage on the infrastructure cluster only through the controlled KubeVirt CSI interface.

- The hosted cluster does not have access to the KubeVirt CSI cluster controller. As a result, the hosted cluster cannot access arbitrary storage volumes on the infrastructure cluster that are not associated with the hosted cluster. The KubeVirt CSI cluster controller runs in a pod in the hosted control plane namespace.

- Role-based access control (RBAC) of the KubeVirt CSI cluster controller limits the persistent volume claim (PVC) access to only the hosted control plane namespace. Therefore, KubeVirt CSI components cannot access storage from the other namespaces.

## Configuring etcd storage

At cluster creation time, you can configure the storage class that is used to host etcd data by using the `--etcd-storage-class` argument.

<div>

<div class="title">

Procedure

</div>

- To configure a storage class for etcd, run a command similar to the following example:

  ``` terminal
  $ hcp create cluster kubevirt \
    --name my-hosted-cluster \
    --node-pool-replicas 2 \
    --pull-secret /user/name/pullsecret \
    --memory 8Gi \
    --cores 2 \
    --etcd-storage-class=lvm-storageclass
  ```

  - `--name` specifies the name of your hosted cluster.

  - `--node-pool-replicas` specifies the worker count.

  - `--pull-secret` specifies the path to your pull secret.

  - `--memory` specifies a value for memory.

  - `--cores` specifies a value for CPU.

  - `--etcd-storage-class` specifies the etcd storage class name. If you do not provide an `--etcd-storage-class` argument, the default storage class is used.

</div>

# Attaching NVIDIA GPU devices by using the hcp CLI

You can attach one or more NVIDIA graphics processing unit (GPU) devices to node pools by using the `hcp` command-line interface (CLI) in a hosted cluster on OpenShift Virtualization.

> [!IMPORTANT]
> Attaching NVIDIA GPU devices to node pools is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You have exposed the NVIDIA GPU device as a resource on the node where the GPU device resides. For more information, see [NVIDIA GPU Operator with OpenShift Virtualization](https://docs.nvidia.com/datacenter/cloud-native/openshift/latest/openshift-virtualization.html).

- You have exposed the NVIDIA GPU device as an [extended resource](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#extended-resources) on the node to assign it to node pools.

</div>

<div>

<div class="title">

Procedure

</div>

- You can attach the GPU device to node pools during cluster creation by running a command similar to the following example:

  ``` terminal
  $ hcp create cluster kubevirt \
    --name my-hosted-cluster \
    --node-pool-replicas 3 \
    --pull-secret /user/name/pullsecret \
    --memory 16Gi \
    --cores 2 \
    --host-device-name="nvidia-a100,count:2"
  ```

  - `--name` specifies the name of your hosted cluster.

  - `--node-pool-replicas` specifies the worker count.

  - `--pull-secret` specifies the path to your pull secret.

  - `--memory` specifies a value for memory.

  - `--cores` specifies a value for CPU.

  - `--host-device-name` specifies the GPU device name and the count. The `--host-device-name` argument takes the name of the GPU device from the infrastructure node and an optional count that represents the number of GPU devices you want to attach to each virtual machine (VM) in node pools. The default count is `1`. For example, if you attach 2 GPU devices to 3 node pool replicas, all 3 VMs in the node pool are attached to the 2 GPU devices.

    > [!TIP]
    > You can use the `--host-device-name` argument multiple times to attach multiple devices of different types.

</div>

# Attaching NVIDIA GPU devices by using the NodePool resource

You can attach one or more NVIDIA graphics processing unit (GPU) devices to node pools by configuring the `nodepool.spec.platform.kubevirt.hostDevices` field in the `NodePool` resource.

> [!IMPORTANT]
> Attaching NVIDIA GPU devices to node pools is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Procedure

</div>

- To attach a single GPU device, configure the `NodePool` resource by using the following example configuration:

  ``` yaml
  apiVersion: hypershift.openshift.io/v1beta1
  kind: NodePool
  metadata:
    name: <hosted_cluster_name>
    namespace: <hosted_cluster_namespace>
  spec:
    arch: amd64
    clusterName: <hosted_cluster_name>
    management:
      autoRepair: false
      upgradeType: Replace
    nodeDrainTimeout: 0s
    nodeVolumeDetachTimeout: 0s
    platform:
      kubevirt:
        attachDefaultNetwork: true
        compute:
          cores: <cpu>
          memory: <memory>
        hostDevices:
        - count: <count>
          deviceName: <gpu_device_name>
        networkInterfaceMultiqueue: Enable
        rootVolume:
          persistent:
            size: 32Gi
          type: Persistent
      type: KubeVirt
    replicas: <worker_node_count>
  ```

  - `<hosted_cluster_name>` specifies the name of your hosted cluster; for example, `my-hosted-cluster`.

  - `<hosted_cluster_namespace>` specifies the name of the hosted cluster namespace; for example, `my-hc-namespace`.

  - `<cpu>` specifies a value for CPU; for example, `2`.

  - `<memory>` specifies a value for memory; for example, `16Gi`.

  - `<count>` specifies the number of GPU devices you want to attach to each virtual machine (VM) in node pools. For example, if you attach 2 GPU devices to 3 node pool replicas, all 3 VMs in the node pool are attached to the 2 GPU devices. The default count is `1`. The `hostDevices` field defines a list of different types of GPU devices that you can attach to node pools.

  - `<gpu_device_name>` specifies the GPU device name; for example,`nvidia-a100`.

  - `<worker_node_count>` specifies the worker count; for example, `3`.

- To attach multiple GPU devices, configure the `NodePool` resource by using the following example configuration:

  ``` yaml
  apiVersion: hypershift.openshift.io/v1beta1
  kind: NodePool
  metadata:
    name: <hosted_cluster_name>
    namespace: <hosted_cluster_namespace>
  spec:
    arch: amd64
    clusterName: <hosted_cluster_name>
    management:
      autoRepair: false
      upgradeType: Replace
    nodeDrainTimeout: 0s
    nodeVolumeDetachTimeout: 0s
    platform:
      kubevirt:
        attachDefaultNetwork: true
        compute:
          cores: <cpu>
          memory: <memory>
        hostDevices:
        - count: <count>
          deviceName: <gpu_device_name>
        - count: <count>
          deviceName: <gpu_device_name>
        - count: <count>
          deviceName: <gpu_device_name>
        - count: <count>
          deviceName: <gpu_device_name>
        networkInterfaceMultiqueue: Enable
        rootVolume:
          persistent:
            size: 32Gi
          type: Persistent
      type: KubeVirt
    replicas: <worker_node_count>
  ```

  - `<hosted_cluster_name>` specifies the name of your hosted cluster; for example, `my-hosted-cluster`.

  - `<hosted_cluster_namespace>` specifies the name of the hosted cluster namespace; for example, `my-hc-namespace`.

  - `<cpu>` specifies a value for CPU; for example, `2`.

  - `<memory>` specifies a value for memory; for example, `16Gi`.

  - `<count>` specifies the number of GPU devices you want to attach to each VM in node pools. For example, if you attach 2 GPU devices to 3 node pool replicas, all 3 VMs in the node pool are attached to the 2 GPU devices. The default count is `1`. The `hostDevices` field defines a list of different types of GPU devices that you can attach to node pools.

  - `<gpu_device_name>` specifies the GPU device name; for example,`nvidia-a100`.

  - `<worker_node_count>` specifies the worker count; for example, `3`.

</div>

# Evicting KubeVirt virtual machines

In cases where KubeVirt virtual machines (VMs) cannot be live migrated, such as when you use GPU passthrough, the VMs must be evicted at the same time as the `NodePool` resource of the hosted cluster. Otherwise, the compute nodes might be shut down without being drained from the workload. This might also happen when you are upgrading the OpenShift Virtualization Operator. To achieve a synchronized restart, you can set the `evictionStrategy` parameter on the `hyperconverged` resource to ensure that only VMs that are drained from workloads are rebooted.

<div>

<div class="title">

Procedure

</div>

1.  To learn more about the `hyperconverged` resource and the allowed values for the `evictionStrategy` parameter, enter the following command:

    ``` terminal
    $ oc explain hyperconverged.spec.evictionStrategy
    ```

2.  Patch the `hyperconverged` resource by entering the following command:

    ``` terminal
    $ oc -n openshift-cnv patch hyperconverged kubevirt-hyperconverged \
      --type=merge \
      -p '{"spec": {"evictionStrategy": "External"}}'
    ```

3.  Patch the workload update strategy and the workload update methods by entering the following command:

    ``` terminal
    $ oc -n openshift-cnv patch hyperconverged kubevirt-hyperconverged \
      --type=merge \
      -p '{"spec": {"workloadUpdateStrategy": {"workloadUpdateMethods": ["LiveMigrate","Evict"]}}}'
    ```

    By applying this patch, you specify that VMs should be live-migrated if possible, and that only the VMs that cannot be live-migrated should be evicted.

</div>

<div>

<div class="title">

Verification

</div>

- Check whether the patch command was applied properly by entering the following command:

  ``` terminal
  $ oc -n openshift-cnv get hyperconverged kubevirt-hyperconverged -ojsonpath='{.spec.evictionStrategy}'
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  External
  ```

  </div>

</div>

# Spreading node pool VMs by using topologySpreadConstraint

By default, KubeVirt virtual machines (VMs) created by a node pool are scheduled on any available nodes that have the capacity to run the VMs. By default, the `topologySpreadConstraint` constraint is set to schedule VMs on multiple nodes.

In some scenarios, node pool VMs might run on the same node, which can cause availability issues. To avoid distribution of VMs on a single node, use the descheduler to continuously honor the `topologySpreadConstraint` constraint to spread VMs on multiple nodes.

<div>

<div class="title">

Prerequisites

</div>

- You installed the Kube Descheduler Operator. For more information, see "Installing the descheduler".

</div>

<div>

<div class="title">

Procedure

</div>

- Open the `KubeDescheduler` custom resource (CR) by entering the following command, and then modify the `KubeDescheduler` CR to use the `SoftTopologyAndDuplicates` and `KubeVirtRelieveAndMigrate` profiles so that you maintain the `topologySpreadConstraint` constraint settings.

  The `KubeDescheduler` CR named `cluster` runs in the `openshift-kube-descheduler-operator` namespace.

  ``` terminal
  $ oc edit kubedescheduler cluster -n openshift-kube-descheduler-operator
  ```

  <div class="formalpara">

  <div class="title">

  Example `KubeDescheduler` configuration

  </div>

  ``` yaml
  apiVersion: operator.openshift.io/v1
  kind: KubeDescheduler
  metadata:
    name: cluster
    namespace: openshift-kube-descheduler-operator
  spec:
    mode: Automatic
    managementState: Managed
    deschedulingIntervalSeconds: 30
    profiles:
    - SoftTopologyAndDuplicates
    - KubeVirtRelieveAndMigrate
    profileCustomizations:
      devDeviationThresholds: AsymmetricLow
      devActualUtilizationProfile: PrometheusCPUCombined
  # ...
  ```

  </div>

  - Sets the number of seconds between the descheduler running cycles.

  - This profile evicts pods that follow the soft topology constraint: `whenUnsatisfiable: ScheduleAnyway`.

  - This profile balances resource usage between nodes and enables the strategies, such as `RemovePodsHavingTooManyRestarts` and `LowNodeUtilization`.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing the descheduler](../../nodes/scheduling/descheduler/nodes-descheduler-configuring.md#nodes-descheduler-installing_virt-enabling-descheduler-evictions)

</div>
