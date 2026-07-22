<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The containerized Data Plane Development Kit (DPDK) application is supported on OpenShift Container Platform. You can use Single Root I/O Virtualization (SR-IOV) network hardware with the Data Plane Development Kit (DPDK) and with remote direct memory access (RDMA).

Before you perform any tasks in the following documentation, ensure that you [installed the SR-IOV Network Operator](../networking_operators/sr-iov-operator/installing-sriov-operator.md#installing-sriov-operator).

# Example use of a virtual function in a pod

You can run a remote direct memory access (RDMA) or a Data Plane Development Kit (DPDK) application in a pod with SR-IOV VF attached.

This example shows a pod using a virtual function (VF) in RDMA mode:

<div class="formalpara">

<div class="title">

`Pod` spec that uses RDMA mode

</div>

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: rdma-app
  annotations:
    k8s.v1.cni.cncf.io/networks: sriov-rdma-mlnx
spec:
  containers:
  - name: testpmd
    image: <RDMA_image>
    imagePullPolicy: IfNotPresent
    securityContext:
      runAsUser: 0
      capabilities:
        add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW"]
    command: ["sleep", "infinity"]
```

</div>

The following example shows a pod with a VF in DPDK mode:

<div class="formalpara">

<div class="title">

`Pod` spec that uses DPDK mode

</div>

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: dpdk-app
  annotations:
    k8s.v1.cni.cncf.io/networks: sriov-dpdk-net
spec:
  containers:
  - name: testpmd
    image: <DPDK_image>
    securityContext:
      runAsUser: 0
      capabilities:
        add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW"]
    volumeMounts:
    - mountPath: /dev/hugepages
      name: hugepage
    resources:
      limits:
        memory: "1Gi"
        cpu: "2"
        hugepages-1Gi: "4Gi"
      requests:
        memory: "1Gi"
        cpu: "2"
        hugepages-1Gi: "4Gi"
    command: ["sleep", "infinity"]
  volumes:
  - name: hugepage
    emptyDir:
      medium: HugePages
```

</div>

# Using a virtual function in DPDK mode with an Intel NIC

You can use a virtual function (VF) in Data Plane Development Kit (DPDK) mode with an Intel NIC by creating a `SriovNetworkNodePolicy` object and then deploying a pod.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Install the SR-IOV Network Operator.

- Log in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the following `SriovNetworkNodePolicy` object, and then save the YAML in the `intel-dpdk-node-policy.yaml` file.

    ``` yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetworkNodePolicy
    metadata:
      name: intel-dpdk-node-policy
      namespace: openshift-sriov-network-operator
    spec:
      resourceName: intelnics
      nodeSelector:
        feature.node.kubernetes.io/network-sriov.capable: "true"
      priority: <priority>
      numVfs: <num>
      nicSelector:
        vendor: "8086"
        deviceID: "158b"
        pfNames: ["<pf_name>", ...]
        rootDevices: ["<pci_bus_id>", "..."]
      deviceType: vfio-pci
    ```

    where:

    `spec.deviceType`
    Specifies the driver type for the virtual functions. Set to `vfio-pci`.

    > [!NOTE]
    > See the `Configuring SR-IOV network devices` section for a detailed explanation on each option in `SriovNetworkNodePolicy`.
    >
    > When applying the configuration specified in a `SriovNetworkNodePolicy` object, the SR-IOV Operator might drain the nodes, and in some cases, reboot nodes. It might take several minutes for a configuration change to apply. Ensure that there are enough available nodes in your cluster to handle the evicted workload beforehand.
    >
    > After the configuration update is applied, all the pods in `openshift-sriov-network-operator` namespace will change to a `Running` status.

2.  Create the `SriovNetworkNodePolicy` object by running the following command:

    ``` terminal
    $ oc create -f intel-dpdk-node-policy.yaml
    ```

3.  Create the following `SriovNetwork` object, and then save the YAML in the `intel-dpdk-network.yaml` file.

    ``` yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetwork
    metadata:
      name: intel-dpdk-network
      namespace: openshift-sriov-network-operator
    spec:
      networkNamespace: <target_namespace>
      ipam: |-
    # ...
      vlan: <vlan>
      resourceName: intelnics
    ```

    where:

    `spec.ipam`
    Specifies a configuration object for the IPAM CNI plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition.

    > [!NOTE]
    > See the "Configuring SR-IOV additional network" section for a detailed explanation on each option in `SriovNetwork`.

    An optional library, app-netutil, provides several API methods for gathering network information about a container’s parent pod.

4.  Create the `SriovNetwork` object by running the following command:

    ``` terminal
    $ oc create -f intel-dpdk-network.yaml
    ```

5.  Create the following `Pod` spec, and then save the YAML in the `intel-dpdk-pod.yaml` file.

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: dpdk-app
      namespace: <target_namespace>
      annotations:
        k8s.v1.cni.cncf.io/networks: intel-dpdk-network
    spec:
      containers:
      - name: testpmd
        image: <DPDK_image>
        securityContext:
          runAsUser: 0
          capabilities:
            add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW"]
        volumeMounts:
        - mountPath: /mnt/huge
          name: hugepage
        resources:
          limits:
            openshift.io/intelnics: "1"
            memory: "1Gi"
            cpu: "4"
            hugepages-1Gi: "4Gi"
          requests:
            openshift.io/intelnics: "1"
            memory: "1Gi"
            cpu: "4"
            hugepages-1Gi: "4Gi"
        command: ["sleep", "infinity"]
      volumes:
      - name: hugepage
        emptyDir:
          medium: HugePages
    ```

    where:

    `metadata.namespace`
    Specifies the same namespace where the `SriovNetwork` object `intel-dpdk-network` is created. If you want to create the pod in a different namespace, change `target_namespace` in both the `Pod` spec and the `SriovNetwork` object.

    `spec.containers.image`
    Specifies the DPDK image which includes your application and the DPDK library used by application.

    `spec.containers.securityContext.capabilities.add`
    Specifies additional capabilities required by the application inside the container for hugepage allocation, system resource allocation, and network interface access.

    `spec.containers.volumeMounts.mountPath`
    Specifies the path where a hugepage volume is mounted in the DPDK pod. The hugepage volume is backed by the `emptyDir` volume type with the medium being `Hugepages`.

    `spec.containers.resources.limits.openshift.io/intelnics`
    Optional: Specifies the number of DPDK devices allocated to DPDK pod. If not explicitly specified, this resource request and limit is automatically added by the SR-IOV network resource injector. The SR-IOV network resource injector is an admission controller component managed by the SR-IOV Operator. It is enabled by default and can be disabled by setting `enableInjector` option to `false` in the default `SriovOperatorConfig` CR.

    `spec.containers.resources.limits.cpu`
    Specifies the number of CPUs. The DPDK pod usually requires exclusive CPUs to be allocated from the kubelet. This is achieved by setting CPU Manager policy to `static` and creating a pod with `Guaranteed` QoS.

    `spec.containers.resources.limits.hugepages-1Gi`
    Specifies the hugepage size `hugepages-1Gi` or `hugepages-2Mi` and the quantity of hugepages that will be allocated to the DPDK pod. Configure `2Mi` and `1Gi` hugepages separately. Configuring `1Gi` hugepage requires adding kernel arguments to Nodes. For example, adding kernel arguments `default_hugepagesz=1GB`, `hugepagesz=1G` and `hugepages=16` will result in `16*1Gi` hugepages be allocated during system boot.

6.  Create the DPDK pod by running the following command:

    ``` terminal
    $ oc create -f intel-dpdk-pod.yaml
    ```

</div>

# Using a virtual function in DPDK mode with a Mellanox NIC

You can create a network node policy and create a Data Plane Development Kit (DPDK) pod by using a virtual function in DPDK mode with a Mellanox NIC.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have installed the Single Root I/O Virtualization (SR-IOV) Network Operator.

- You have logged in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Save the following `SriovNetworkNodePolicy` YAML configuration to an `mlx-dpdk-node-policy.yaml` file:

    ``` yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetworkNodePolicy
    metadata:
      name: mlx-dpdk-node-policy
      namespace: openshift-sriov-network-operator
    spec:
      resourceName: mlxnics
      nodeSelector:
        feature.node.kubernetes.io/network-sriov.capable: "true"
      priority: <priority>
      numVfs: <num>
      nicSelector:
        vendor: "15b3"
        deviceID: "1015"
        pfNames: ["<pf_name>", ...]
        rootDevices: ["<pci_bus_id>", "..."]
      deviceType: netdevice
      isRdma: true
    ```

    where:

    `spec.nicSelector.deviceID`
    Specifies the device hex code of the SR-IOV network device. The value `"1015"` is associated with a Mellanox NIC.

    `spec.deviceType`
    Specifies the driver type for the virtual functions. A Mellanox SR-IOV Virtual Function (VF) can work in DPDK mode without using the `vfio-pci` device type. Set to `netdevice`. The VF device is displayed as a kernel network interface inside a container.

    `spec.isRdma`
    Setting to `true` enables Remote Direct Memory Access (RDMA) mode. This is required for Mellanox cards to work in DPDK mode.

    > [!NOTE]
    > See *Configuring an SR-IOV network device* for a detailed explanation of each option in the `SriovNetworkNodePolicy` object.
    >
    > When applying the configuration specified in an `SriovNetworkNodePolicy` object, the SR-IOV Operator might drain the nodes, and in some cases, reboot nodes. It might take several minutes for a configuration change to apply. Ensure that there are enough available nodes in your cluster to handle the evicted workload beforehand.
    >
    > After the configuration update is applied, all the pods in the `openshift-sriov-network-operator` namespace will change to a `Running` status.

2.  Create the `SriovNetworkNodePolicy` object by running the following command:

    ``` terminal
    $ oc create -f mlx-dpdk-node-policy.yaml
    ```

3.  Save the following `SriovNetwork` YAML configuration to an `mlx-dpdk-network.yaml` file:

    ``` yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetwork
    metadata:
      name: mlx-dpdk-network
      namespace: openshift-sriov-network-operator
    spec:
      networkNamespace: <target_namespace>
      ipam: |-
    ...
      vlan: <vlan>
      resourceName: mlxnics
    ```

    where:

    `spec.ipam`
    Specifies a configuration object for the IP Address Management (IPAM) Container Network Interface (CNI) plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition.

    > [!NOTE]
    > See *Configuring an SR-IOV network device* for a detailed explanation on each option in the `SriovNetwork` object.

    The `app-netutil` option library provides several API methods for gathering network information about the parent pod of a container.

4.  Create the `SriovNetwork` object by running the following command:

    ``` terminal
    $ oc create -f mlx-dpdk-network.yaml
    ```

5.  Save the following `Pod` YAML configuration to an `mlx-dpdk-pod.yaml` file:

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: dpdk-app
      namespace: <target_namespace>
      annotations:
        k8s.v1.cni.cncf.io/networks: mlx-dpdk-network
    spec:
      containers:
      - name: testpmd
        image: <DPDK_image>
        securityContext:
          runAsUser: 0
          capabilities:
            add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW"]
        volumeMounts:
        - mountPath: /mnt/huge
          name: hugepage
        resources:
          limits:
            openshift.io/mlxnics: "1"
            memory: "1Gi"
            cpu: "4"
            hugepages-1Gi: "4Gi"
          requests:
            openshift.io/mlxnics: "1"
            memory: "1Gi"
            cpu: "4"
            hugepages-1Gi: "4Gi"
        command: ["sleep", "infinity"]
      volumes:
      - name: hugepage
        emptyDir:
          medium: HugePages
    ```

    where:

    `metadata.namespace`
    Specifies the same namespace where `SriovNetwork` object `mlx-dpdk-network` is created. To create the pod in a different namespace, change `target_namespace` in both the `Pod` spec and `SriovNetwork` object.

    `spec.containers.image`
    Specifies the DPDK image which includes your application and the DPDK library used by the application.

    `spec.containers.securityContext.capabilities.add`
    Specifies additional capabilities required by the application inside the container for hugepage allocation, system resource allocation, and network interface access.

    `spec.containers.volumeMounts.mountPath`
    Specifies the path where the hugepage volume is mounted in the DPDK pod. The hugepage volume is backed by the `emptyDir` volume type with the medium being `Hugepages`.

    `spec.containers.resources.limits.openshift.io/mlxnics`
    Optional: Specifies the number of DPDK devices allocated for the DPDK pod. If not explicitly specified, this resource request and limit is automatically added by the SR-IOV network resource injector. The SR-IOV network resource injector is an admission controller component managed by SR-IOV Operator. It is enabled by default and can be disabled by setting the `enableInjector` option to `false` in the default `SriovOperatorConfig` CR.

    `spec.containers.resources.limits.cpu`
    Specifies the number of CPUs. The DPDK pod usually requires that exclusive CPUs be allocated from the kubelet. To do this, set the CPU Manager policy to `static` and create a pod with `Guaranteed` Quality of Service (QoS).

    `spec.containers.resources.limits.hugepages-1Gi`
    Specifies the hugepage size `hugepages-1Gi` or `hugepages-2Mi` and the quantity of hugepages that will be allocated to the DPDK pod. Configure `2Mi` and `1Gi` hugepages separately. Configuring `1Gi` hugepages requires adding kernel arguments to Nodes.

6.  Create the DPDK pod by running the following command:

    ``` terminal
    $ oc create -f mlx-dpdk-pod.yaml
    ```

</div>

# Using the TAP CNI to run a rootless DPDK workload with kernel access

DPDK applications can use `virtio-user` as an exception path to inject certain types of packets, such as log messages, into the kernel for processing. For more information about this feature, see [Virtio_user as Exception Path](https://doc.dpdk.org/guides/howto/virtio_user_as_exception_path.html).

In OpenShift Container Platform version 4.14 and later, you can use non-privileged pods to run DPDK applications alongside the tap CNI plugin. To enable this functionality, you need to mount the `vhost-net` device by setting the `needVhostNet` parameter to `true` within the `SriovNetworkNodePolicy` object.

<figure>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABfAAAAKXCAIAAABCDvxMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyhpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDkuMS1jMDAxIDc5LmE4ZDQ3NTM0OSwgMjAyMy8wMy8yMy0xMzowNTo0NSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIDI0LjcgKE1hY2ludG9zaCkiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6Q0Y2RjE5RjE0RDg1MTFFRUI2QTZGMDA2OEFEREU3QTQiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6Q0Y2RjE5RjI0RDg1MTFFRUI2QTZGMDA2OEFEREU3QTQiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDpDRjZGMTlFRjREODUxMUVFQjZBNkYwMDY4QURERTdBNCIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDpDRjZGMTlGMDREODUxMUVFQjZBNkYwMDY4QURERTdBNCIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PqbM5fUAANubSURBVHja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5FSvXl0FLrzwwtq1a5vbJFXz3zDoqKqK0y6hE3oDGjsyKd7XXntt8uTJ6t4pErVt21av1SkMLaxOnnppu3btsn5/0+H38ssvf/311zr2rOeAaCHr1q1T6NS7OgjHjBmj3p56lppujhl1WFVA61WH79///rfWnpubq/KKNeoU3nzzzXpxzTXXHO16K+Phhx9+8cUXTTrGpNIVAhQi3377bU2/++67A+uvkPG///1PfeWff/5ZsVhdVXWF58+fr3ikPr2V8HrsscfGjx/v9jOpZf3duXPnW2+9pdnVhQ287dl33313++23K/pb1/dqYKDg8tVXX916661alLlT9V133fXuu++afHw1/0+smlGr1vQnn3ySoAAAVUztwtVXX71161ZFaaubqwCuluj999/XX9NuVj6Am6ZQS1OH8ptvvnnwwQfVadaSs7OzT2CLZtYSGxurVvj+++9Xe6qGWA1QZmam+vT699VXX9XQwixQQ4VLL71U1TCVN82ZqmTavqVLl06YMMHK6ajHfN9996kVrub/mdf8EK1+s1rMmTNnqllUR/yodggABiknb4coFlXz55cDf5Q1Y/4VK1ao075582aT3FFA/vbbb5966qn69eurcFpa2ueff67Q16xZM0VIc46Jpu/bt08hUcOTFi1aDB48+NChQ+rGa17FRoVE8/QoDR8010MPPdSpUycFwO+///7DDz9MSkq64IIL1GSogJajmK+IrRnz8vKs0zZnzJjRvXv34cOHN2/eXDVXqFTM1HDJan1EkbZ///6Kw1ryES8gUnnVXK1DRkaGmgBzhqaWYNaondCnT5+DBw9qyKb6aBR22WWXWeuypmtwZB6kYzYkJSUlNTV1ypQpobuuXr16ZvaKN1DtlJonUystXK+136ZNm2ZOIKqgVtqEL774Qu2XRprWqVgadmmL7rnnHrU+5mILrb3yVcXpmNA5NegLPWnSpI8//lgHhg4hRY333ntPoSe0pHppQ4cO1UGlEGCe/6e/OorUR9y0aZPe+uqrr8xt1c35bDoIFV9+/PFHdS5r1KhhUtom3OjoMr9J6mAbN25c7dq1FdQUFs3xqXDz/PPP64g1F3xVfr1HtGzZstdee02xVTXs0KFD69at1dNV9fRXMeUvf/mLKWbVX3/VMbUuQtYLzasafvTRR6rGyy+/bMpfddVVaga0LaqwOaFdMV3hr3r16urrP/LII59++qkiVDX/o3CHDBmimKW3zKmM2v/qf5vT/3766SdN1JR//vOfilzmcYPab1qsFqi1a7+98MILjRs3vu222/jqAkBVeuaZZ7Zt25bo17t3bwXwtWvXbt26VYH6rrvusn4FqXwAN02hYr5eqLOrRlAtixlynMAWzVqL6vPZZ5/p3+TkZI0KTCOlF6p8y5YttYRq/gsT1FmfPn26OeNd7aC5lFgNn3nMbd++fa+44gqz5LFjx06cOFHtu9pHFTNnyKtbrPZO1diyZYtJ6NCiAahiZpRhrpMyj7hSRNLo3VwS1bRpUw0lzI1U9Fcd+FdeeaVz587XXXed+uSzZ8/WKEPh/fXXX1eU0ywKegsXLlRw0xIuvvhic72SItgPP/ygaKaI96c//alRo0aPP/645lUY17hAsTQvLy8tLU2zFBcXa5xiHryltau8+Q3brF3vPvroo/Pnz9eKtJCuXbtq9LRu3TqNcebNm6dgrkWpvIKnSvbo0aNdu3aK4YrzqpJqqyHJGWecMWDAAOuclMMxp1uqaVD43bhxo4ZXmti/f381XtoD2nxtoOpjfs9WPQOv5LKmm2uXzPhRU1TVf//734fbdSalWPEG9urVS3UwtVq+fLk+Ji35z3/+s7nA6nC10obMmTPniSee0FarpNoa7fYdO3YsWbLkl19++de//qXRZfv27c3lWpWsKo9CJ6FjYzpI1NNSVNJhpkNl9OjRChzllnz++ef379+fkJCgWZ566qmbbrpJ5XVsqI+rnt/q1avfeecd83tg4MJXrVp10UUXqb/YpEkTHWnqNQYW0HGontzIkSO12ClTpjzyyCM6nBSF9+zZs3v3bnVPj229h7N06VLzy6RC4X//+19zuZb60JMnT/7DH/6QkpISGvu0iltvvbVfv34KxDNmzHj33XcVERQ7tFLVpEuXLip2/vnnDx06VPFCUV59U5VUiNe2KF4oaitYpKenK/6q5LPPPqvwoaBsgtR9991Xt25d1eq5557r1KnTe++9p57xjz/+qE9EZdT3VZhTG6Ndt379+jvuuMP8lvvqq68OHDgw8Gx2AMBJlZ2drWCuCGzuN6f+n5muTuHPP/98yy23mH+PIYCracvMzFSjoIbgkksuUbujtqPab49lCf2BXa2k2iC12kfboqnp1GDg9ttvb968+YYNG1588UVzruiBAwdeeumlt956q5r/tnFqr7VS9bDPPPNMbYjaLNX5s88+U+U1XdtrEjorV66cNGmSCqg+2oR7771XDaX20n/+858vv/xSbfRf//rXY9shAHDMFKbUD1fk0VBCQc+EUI0pvvjiC0Uzxcw+ffpofKGIZJ31r2D7t7/9bfDgwYqrKn/eeefdf//9CowaYiiiqqPesWNHEzYV97QoTTHPhPr222+1LkVghe6DBw8uW7ZMS9Pso0aNMql5FbvmmmtUUvFZf4PODDJpkY8++mjhwoWRkZFnn332Qw89VL9+/Wr+G3e+8cYbGhBpdrUOGqPdeOONqrnCsmYxd+357rvvNNYwaabKXL6qqmpQo2GXxiZa+PLlyzXx2muvVWRWu3ZsT7mqeNfVrl1b21XxBg4YMEDbYmqlzUlLS1MlNcJq06aN6lNurbQ3MjIyNLuqrZZOc2kTzOf++eefqyVVkzpx4kSNHwMb0IqrWqdOHU7SOU0TOr7f2H3/6hhTD9I8zkP9M3UEQ7tW27dvX7BggQ42HTx9+/a9+eabdYzpkLjnnnsWL148b948LeSrr7668847A6OVYpCW9v7775v7Cjdt2jQoXZKQkDB8+HDzw6YOs48//njJkiUm+2t27LGt97DfJP8Zifp76NChu+++W11bxfR27dr985//LLe86n/llVc+++yz5t8LLrhANXnttdf0Nzc3V+s1CR1RzzhwxhYtWqh66tfGx8era67VmW2ZO3eu5lVs0iZPmTLF7BAFONVEUS81NVX/fvrppwo6Jpf8wAMPNGvWTJusCD569OhBgwYpiqWnp2vhf/rTnwgNAHD8vf/KXJVgPURDnelPPvlErUPbtm3V4+zdu/cf//hHq9gxBHDzA/L48eMvv/zywDW++eabjz76qDnrM5DGCRqZqNU4qhZNJdUQv/LKK+Yi5W7duqn90hhA3dmYmJgffvhBg5969erprXP8rBkbNWqkBmvOnDnm1pUqZqbPmDFD7WBiYqLqc++991oZrvPPP18bqObymHcIAAYpxxPSFWTGjRsXuO3mTA29ZW4cpshj3XTG3MtSkVwFTDJdZbp27frll18qdmmKufm9CmzYsCEjI2PFihWKihoxrV+/ft26dSacNm/eXOMUc1Xptm3bFNMaNGigxkLRtX379ubmvqFVNTe1UTzX6+Tk5BEjRjRu3Nhcz6UZ//GPf1gfosfj0TBB75oEutmW7t27K2hn+SkaV+apxJpRldHmW3cCNrdYNvvH3FWn8o6461S9ymyglmNqZX0oplaaWG6tNOWnn34yty667rrr1NxoXWbPqFFbuXKl2h393bRpk3Z+5T9lgsZpmtAxp0lb557ZlA4eHWBvvfWWgpS2Zf78+bfffvt//vMfc4mQRX04FdBEc5ubc88911w8pX/NjAoNKqNuZeCvglq4+pcVhBhzH3XrX3UNzWKt7vWxrfdwLrroorp165oFzpo1SyHG3PlcXUz1LG+77bagqKFPNuhJVUOGDJk6darJf61du9aarrDy1VdfKbib30vPOuusvLy8oGeCWNui6KboE5jeCrwnpRoMcx6mKqPur7UrzHW2ZX4bN26k+wsAx5/EKfULCv6Bz0w1TbzagksvvVR9xOrVq+/evfvVV19VhFc3QH3Ec845Rx1Thf1jC+DmV9PQ2+erNcnOzg59AIdaENPrPaoWzXSLA1t2rbFPnz7vvPOOJu7bt08bZRI6Kqml/fDDD5qobWnSpIkGElqy+cHZ2qK0tDT1v1X5+Ph4dakDu0ZWNocWDWCQ8rtQWLOijenM16lT57zzzhswYECNGjVCT/rweDzWPWgUdYMGQZpy/vnnT58+XTF54cKFileKft99911ubq72sMnpK0heeOGFy5cvX7NmzbBhwxo1atSgQYOGDRt27NhRrYPeDV2pGpFff/117969qmHnzp0Vuq1LbrVG69nk1fznpKiwwumyZctU3tzNp2XLlia6HtXlQkFpvuNP/FWw6yq/gUdbK+0Kk6Pp1auX9Zwvc1GbPuXPPvtMK9qyZYu5lLiSnzJOx4SOvhDq5Sg6mOeu2Xfn6jBQYFJQGDx4sAJEQkLC559/PmLEiPHjxwflfUwP0tzqfPv27dYhpwZDAcWcFxd67B3xaXCBs4TuyWNeb7kUSiZNmqSt27Rpk+lNao06vNetW3f33Xdv27bthRdeCPqpNqhKUX4mHpkcczX/HcXuvfdexSwzMDCxVQ2GeaBg6LZIBQ+LNRHfnDq4fv16s0CTeDZnIanCp9sTKAHgBFJ8NjcyU3dTfU01Lup8BxbYunVr4LjIvHjwwQcPHjz44Ycfqk9vbhisUKwpH3zwwYIFCz799FN13I8tgJtfTUP7+jF+od0P04k/2hZNawlatWmJzC8rpgKZmZnDhw9XN8A8IMY0YYF3fAhqqsxV0od7TjktGsAgpeq3XbFl9OjR2gPmIhoFHO0HxXzzqKnKXFgUtNM0V6tWrc4444xFixatWLFix44dKSkpCxcu1JJbtGhx1llnmUe+XH311Sr5ySefZGRkrFmzZvny5QrjWmmXLl0efvhhkzEPpMCoZsg8oDD0ycLWCMKE8bfeemvatGnmUb/mVjImg3+0p9VUwf4/2g08Brm5uVqRPtPExMTAFsT6JV5rVHN2VJ8yTseEjvmxS/2YU+DbkJeXpxikCPX888/rMFAP7+2331bcGTVqlFVG8UhdOvMMC/M0bnMinLnTmDlZzrpl+gl0wtd78cUXL168WL1Vba+67Bs2bDCpbkV/Bcpbb721TZs2gZ9y0Fk2W7ZsUVfePM7DnJ6n2c2jScwzRPr06aMor4lLly5VQA98wqu1Laq8ucV6ucz1bibMPfnkk40bNzY9YC3KPLxQrYV1DiEA4GjVr19fAVxxWMF83759H3zwwYgRI6x3t2/fPmvWLNNLVitj7oBm0h8TJkwYNmzY/Pnz169fr+ZASygoKDA3mpk0adK///3vExjA1S5369Yt9DHh6rxaSziqFi0wOWWY02e0jdo0bYWmaCumT5+unrf2TMeOHbt27ao6p6WlmWf9hjZVWpfaRO2x5s2b06IBDFLCgbrZCvLNmjWzcjfmup4j3ja44v154YUX/vDDD1lZWWvWrFELsm3bNq3okksuUfA0P/RqyHDLLbf069fvl19+2eWnyKzXixYteuONNx577LHQxWpcoFHMwYMHNY4wA4SgPI5Jms+ZM2f8+PGactlll11++eXx8fGaZfny5WqqTtIZWOahvYG79Nj2W2U28BiWrEZKNdRnoSWbWxpZy9QUs9jKXLqB0z2hUy3k9DD7MuF+9OjR6enpH330UWJiog6/Z555pl69ekOGDDFlWrVq1bJly3Xr1qmbqNikPpl1frh6w4plob8inhAnfL2ZmZk6/v/sZ6ao/3rPPffExcWpV6pwE1hYK1Us1m5p0qSJ/t24ceOYMWOsAHTeeeeZiTt37lRvWNH8zTffvPLKK8285iwn86Auo4Wfesaq8/fffz916tQbb7yxmv8kqeeee06bZv7t06fPe++9Z7LaO3bs+Pvf/x6YTjpcpxkAUEmK2Oqar127Vh1ltXcvvPCCuobXXHONudH+E088sXfvXvNs8tq1a//hD3+wZtQsaoM6d+5sNUMDBgxQC6V+vFqKExvAG/qdqBZNG1hQUPD111+rWVdt1f19+eWXNTjRZqoNOvPMM83TLRcuXKgpxcXF3bp1mz17tvlJQxvSu3fvoMdvqQV8//33TWv49NNPt23bVr3qav67IE+ZMuXxxx9PTk6mRQMYpPwuFOLMaYYnaoFa1Nlnn52amrpnz54FCxaoe19SUpKSkqJIaK3FDBDq1KmjYuaOMAqbo0aN+uabbzSEycvLCzpLRTOqZIMGDdTiaLixadOmdu3aqZjJDVmXHWmxixYtUuHWrVtraVqpub+yVq0GK2jkcqK+NuZJiCb/Yh6Rfgxfp0puoJV2tFZhVl1BFknLMXcgmj9/fqdOncyP/aaSc+fO1V99QBo/6iMI/VEEJHT+D33P9GU6ZU4VjoyMfOmllzZv3qwOq3X/QvVl+/XrV81/dsnQoUPVFVNXb//+/VddddV1113XokWLrVu3Tps2Td24119//WT8yHbC1/uvf/3rgw8+uOKKK/r27duqVSt9fNpefY4KOoqz1nNnDfPY8ksvvdQ8e1V9X4WkmJgYBSOt1Fzzb4UbvUhLS9Mgwdzlcc2aNUH3adYQ4sYbb1RX29xU6P777//888+1Rs2lJZsT2q+//vrLL798/PjxqpW2XV1ztQHm6tw5c+aoq60PRUsgPAHA8Rg2bJjagoMHD5rEzaOPPjpu3DjTQTQnfqpHqFD/j3/8o3HjxmaWVatWqUGsV6/etdde271791q1aik+Z2dnKyAXFRWZZzhWcQCvfItmOseqwMyZM5s2bWpu22nyNcXFxUOGDDF3EzAtmmqYlZWlzrdK6t3Zs2eb+30GrvrKK6989dVX1WfQli5ZsqR///4a7RQUFKh7vXPnzt27d0+YMKF+/fq0aACDlFOAgqoCmqLcZ599pqGBybNodNCkSRNzw2MNoxTfFixYoNGBubpKAVY9f3OvMfX8TQojKHuitkYBXAs8dOjQc889N2LECEVdc7nQm2++qVmGDx9ufY6BCQ5NVAul1urYzp05XDZHDYE2ROv96aefNDYxN8jPzc1Vw6HGMagVqMwCK7OBZhdZeRy1I/v27WvXrp22Wg1Q6ENvtNVnnXWWmrwNGzZ8+OGHzZo1u+iiizSvpr/77rv6CDSjPqnmzZvrU6N9IaFzhECpA1jfueTk5FMmBZ6SkvL6669fddVVpo+rDfzb3/42Y8YMHRV6d/Dgwer/TZ06VeFJx+Hzzz9vfuVTyR07dqib+9VXX7Vt2/aE1+oErvfTTz+dMmWKQoN6wIpNpsuufqqmqFN+1113BT1V3QRorWX79u3mmlVFZAVQ1eTZZ581J6i3b9++devW6vjGx8crVCmUaLFbt27V3lP/Nei7MXToUIXIadOmmds/q+bmxgeaV5FuzJgxF1xwgRoMLee6665TlRRYv/76a3V8zVdOG65QqJ3w5JNPnsAIDgCnmxYtWjz99NNq49RJVdBWbDe3RTOhXv1CTb/22mutS7H07wMPPLB///6cnJzRo0crOCt0m368CteuXds8ubx69epVFsCPtkVTv1a92+/8VEabrAZIPfVBgwbdcMMNpsyll146e/ZsLUoN38UXX9ywYUP1B/Ra2xLULVbnR82xZjRbqpHMunXr1N03N4rWmKdXr17aY1W5QwCcwoOUcNirf/jDH2bNmmXumKMQ2rdvXxO7FPq0w1955ZV58+Z9/vnnvXv3Nk8+Wb58+aJFi1TmwgsvDB0UVPOfpK+3Fi5cqBHBsmXL7rzzzg4dOig2bty4UUMPvZuamnrrrbf27Nnzyy+/TE9Pf/TRR6+88kotaufOnV988YWmnMB76KiBUMzXutSgqGl45JFHzjvvPI1QtBV79uwxQ5WjXWZlNvDGG280V8OZc2qq+Z8dPHfuXH2BVRk1xEHLVBm1LFrUww8/rBZq7Nix5gfyXbt2rVq1Sp9OvXr1brvttsDHZoGETvl06Ooo2rdvX9euXYNuyGQL6pLqWNXxY93H1+jcufO4ceP++te/HjhwQEeCig0cOFC9xk6dOunwGz9+vA489SDNu9pqxSYdjc2aNbv99tutm0pqgToIze2KrTsHB8rLy9N0rV1lAnddudMrv97DLdaiLuwZZ5xhsi0m72vO9NMnOGzYsNCrW7Wcyy67TJ+1+qYqrD2mruqZZ575xBNP9OnTx5SpVavWyy+/rGps2bLFPMVQCzz77LO1fHM7tMA9rOg/YcIEzfLf//5XYVHbollMNc4991yFJHPKugLojBkzHnrooZ9//lnzmnMItVhF7QEDBlx99dX0fQHgOF133XW1a9cePXr06tWrFYfNb4MK3fqr6Yrq//rXv6ynYKinqw66QnRmZqZeqzkwN/rVXOqDPvfcc9blwJUP4Edssyp2VC2auX/kzTffrJ66ei+aReVr1qw5ePBglbQeRnnLLbekpaVNnTpV76p66sTXqFFDY5gffvghOztbazFnyxvqpr/33nsjR45cu3atObNda1EB7b2///3v2oFHu0MAMEg5noRLgZ/63pW5eZCV9goqf7jpCtRdunRp3rz5L7/8oiCm8KsRgUnumBjbqlWrTZs2ac9v3LhR8VllFPGSk5M1qvrzn/+skubH8sAlm1s4P/zww4rPX375pXngoLltvKb069dP4VdBVYMOLeGTTz6ZNWvWt99+a66EOueccxSft23bZl0Pe7iah264tsUEc9PkWW9psQrdqsNPP/2kvxp5VfM/l/3uu+/WIMWcwWrKV3LXVWYDza2O1LCqsejQoYNaZLVr2ofm3t6mZVGbq8Wa+yubtZtxkwat2gPffPONqUBMTEzHjh3vuecetcvmF5ej/ZRxEo9QffzhVid9vVauXJmRkaFjW12iExsr9UXX8X/y7luu2n7wwQf79+83v9dde+219evXDyzw2WefbdmyxTzFQ991BaxLL73UeldH2tdff71hwwYdgbVq1dK7l1xyiclEGDpWtXwdwFq4jiv1+YIq8PHHH+vw0/JVRms3V9pXML2S6614discL1myZPny5Qq4JqXSsGFDbV2PHj2sMuq5XnzxxXFxcQp2w4cPf/bZZ//3v//p41b0adOmjVYa+qC7vXv3fvTRR4o+WmDbtm0HDhy4fv16RUOzE0L3sCowZ84c7WTF+jp16vTq1euPf/xj0PPd1cvXehcvXqyvmd5SUOvdu7e5cQ9wyjh48KB6OYzoUJWNYCB16ebOnatwvWvXLjWO6h8rhqvZKvf2Ltu3b1+0aFFaWtqvv/6q1iQhIeGss8664oorQp/fUZkAXpk2q2KVadGuuuoqNTcaSKhRM49lmT17ttqs1NRUVSn0cemiplZjBi0wJSVFu0I97OnTp+s4VYPVtGlTLTCwcE5Ojrb0xx9/zMzM1Frat2+vVjLoZsy0aEBVNoIndZByPAkXRYmT1+Irlip2aQyiQKRuvCJqxRuu8opI6roHlT/cdImPj3/88cc//PDDav47J/zlL3+xfrfWGEFtltqIZcuWbd68OSsrS5+Cwuw555zTqVMnr9erhVSwRs2uj0yBdOfOnZqiCKnGRSMdk3wxl8cuXbpUC9c+TExM1DIV57/77jsFcwVqLU1ltMbD1TxowzWkWrFiRTX/nfXr1asX+NO+tiI3N1ethpajf1u3bq2Qrobjiy++UHOpb5RqpelHtesq3kDrJkRqCg8cOKCW4pdffjFPJdeqO3furBGrPlmtXZXp2bOnVVutRV/yBQsWaI1qibQ6NUDnnnuu9o/J5hzbp4xy6RNp2bJl4M1hA61bt06fnT4s85Sx0Hd1RIRpQmfVqlUmVp7wL0FV9mURykro5OfnDxs2bNy4cewTgIQOTsmEzinPSuiYK55CUy0ATr2EzskbpIRtQsc8ntyccFFQUHDE0y6sJ38HlS93urlK1OPx/O1vf9O+TU1NnTRpUp06dYLuuxwREaEZtcM1XbOY83TM6ZMVrNEsX9PNjWCq+c/oLy0tNff6tQoojJv0h/nFvaioSFP02tx9ueLlB214lJ9eq5hWFPSJqBrmmlzz2tRfLYi5ssyclFT5XVfJDbTyLypmpmvvaQnm/Fmzdk0vLCwMrK3Km0WJypvrHoIeZH60VcVJSui42YkAAAAAgFDmqoKjKl/kd8Tp1pOeZsyYoaGpRrbnnHNOgwYNQldnHq1lZRzMPSKOuEazCpMoMfMGPVXQFDA3mlGB0tJSs9igClSw/KBiJX7Wv0EFVG0tOeix4tb1ttZFT5XZdZXfQMOkZkwZk0gyVzcHrb2C8sf8KeNkI6EDAAAAAKg6Lpfr4MGDkydP3rt37+rVq30+X2Ji4hVXXFHBeU/HcyPqI85bZXe5Pkkrqsxij3bV3PnbFsI0oeP7DZ/QKeaIN3UGAMAWjvPWywDsiEHKiWKucpo7d+6ePXvMlUpDhgxp3749J3cARyVMEzo6pM2lkoTLU0zz5s2ff/55cw1np06d2CEAAJu64447Lr30UnPr5dTUVHYIcDpgkHKieL3e2NjYvn377tu3Lzk5+dxzz+3Vq5f1cCsAlRSON0U21x8WFhYmJSWd8FjJ/SABnCa4KTJoBAHQCNplkHI8tTqpN0U+qTV3uVzmNr3m3iukyXC6OTVviqwjWX3NqKgobosNAAAAgEHKKbk/zfWq5d52F0BlhPU9dPh4AAAAADBIOVX3JzsBOB5hmtBxOBxOp5NbDAIAAABgkBImtPnV/NeJBE10uVz66/P5vL8J3W+hSzPlj6oCWlE1/yPAD/eu08+c/qOFB+WMTE1Cp4eWOYa6nTo5Ardbe8B6BPvJPqAq2NV6V2Wsj7vij8+8q++AeSi7BH1PzFV+paWlp9SHFZ6BsqioqKCgIDk5mawtAAAAAAYpv7vIyEhtvsbJ0f+PvfOAi+ro/v4uu/QuSJMmImIjCPYuauy9iyXRWPNEI0ax965o1Mdeo4mxYm+xYZegURRUjIrY6L3XfX9w/rnvPruAREUXOd+PH7x7d/qcO3fO2ZkzWlqkgUN/1tTUTE1NffXqVXJyslQqNTU1NTIy0tXVzczMFDRn6NWFHl+FdHR0dBCy5Day9PR0KomyDQI3k5KSoqKi8Bcpm5uboySigi1dQjBcU/mL72jUiIpXDntZIpFER0ejDStXrlzaJi30OzoU7YxMC5UBOkcSPUsuoiBR2dnZ6urqZNdTkCWUNj4+PjIyErEMDAzMzMz09fUpCnUrAsTFxVlYWCDAF/MIq6JBB+PCixcv0BPu7u7oA96kyjAMwzAMwzAMKymfESjMERERM2fOtLW1nTp1KvRhcQG+vr779+9Hy2hqakJzxh1nZ+dmzZp16tTJxMQkMzMT9+/fvz9//nxSyOXTtLS09PDw6NixI8K8c90E2h+pzZ49G9fz5s2Td2aEskGTP3z48OnTp8PCwmgVFXJv2rRpjx49ateunZ6ejgIjyo0bN3x8fMaMGdOlSxeyDSlX8+LFiwjzww8/tGvX7os/eAv1RXOlpaXRR4lEkpqaOn369ODg4DVr1tSvX7/0WoAEAxLl6uoKiULWCs8UAkC60B0LFiwwNTVFgPPnz69evXr8+PFt2rQRCkZWRX9//yNHjty+fRuSQEnZ2dm1atWqZ8+eEDP0tYaGxqVLl5YuXYro6H1U+cuw6ajolqusrCyypfH5LAzDMAzDMAzDsJLyGYHC/ObNmx9//DEuLm7w4MFUfajNa9eu3bp1a8OGDSdOnFipUqXk5OSwsLDr16+vWrVqz549kyZN8vDwgL4NdfrRo0dNmjSpXLmysBADKndgYOCcOXMCAgKg1Wtpab1znQ40cKQv+l/nO9ra2sHBwbNnz0YW9evXHzFiBBT4pKSk+/fvnzx58tSpUyh2nz590HfIsVq1aiiMr69v27ZtUQvlDVkIc+zYMUSvWbPml22zo068du1aTExMp06dqPHp0DF9fX09PT30SKmaPEgwXrx4ERoa6uDgMHz4cFoYJR8gMTERAagY+AgBe/r0Kf4KO/hog9WGDRu2bNmiq6vbqlUrZ2dnFD4yMvLPP//ETcjA5MmTGzVqhCcXffrVV19Nnz4dCZJN5wvoR9X1oUPwa4NhGIZhGIZhGFZSPhfQmaF4z507Nzo6euPGjTVq1IAmrKmpef369R07dgwYMAAKs7a2NhRm8l8zdOjQ27dvb9q0CWozKd7UYl27du3du7ewLoZ2NkEV37p1a/Xq1aHPl0TBVldXl/+IYoSEhEyYMAHJrlixAvo8tHpaPYTyPH78ePny5fPnz8fHvn37IoyNjc3XX3+9f/9+fAXdXmEjGBIPDQ319/fv2LGjnZ3dl6HwFyPMmZmZPj4+aLEePXpQv+Tl5WloaMybNw8fTUxMStuNDsqA7NDU27Ztc3FxcXd3V1g2BfmR73HBW5MQHR/XrFkDsezcufO4ceNsbW2lUikJAMnh7Nmz8W2dOnW0tLQqVqy4YMECBIAwm5mZ1a9fv9BVWmULNR6XGYZhGIZhGIZhmEKByn3gwAF/f/+ZM2fWqlWLzBxQqq9du2ZoaDhkyBCo3CkpKeRgCBf4tnHjxtCimzVrJr9hJycnJ0sOfKWjo/Pdd985OjpevHgRqvW/tZTRJiwfH5+4uLglS5Z07doVKaAAqamp+IuvatSosWLFitq1a69aterx48e0S6tNmza5ubkXLlxQ9tOMivj5+aEkHTt2LMZNL9LRLUBbW1sqlco3lJaWlkItJBIJggl54YJikS2D0hF8xCgnRdERhhzNvLNIhQYTUkO+VGyKAhCY7gB8pG5Ct1pbW5PvYfkCC7koF1jeQCOEoawp2aJAdiNHjjQzM1u6dGlCQoJ8e74TVOqPP/7YsmULun7RokW2trbodEEAUPimTZuuXr16+vTpkDRUB1KH9KdOnWpjYwORQJhCfXWXLaQ8QjEMwzAMwzAMwzCFqItSaWRk5J49e77++uvWrVvLb4qhdTrK6jo054yMDIlEonzKu8IdqN8mJiaVKlWKiopKT0+H1v2v9vgg67Nnz167dm306NEtWrRISkpSyAslRPo//vjjmDFj9u3bN3PmTKj0tWrVcnV1vXTp0jfffGNgYCD47kGBkQISrFmzZvXq1QtdnKKuro7wf/75Z2hoaG5uroWFhYuLS8WKFVERsVj88OHDxMTE2rVro2BUEaQZERHx999/46aRkRFupqSk3Lhxw97e3tbW9sGDB0+ePEFEJOLo6Ih2o8IgFiVVr169hISEe/fuRUdHW1lZ1alTx9DQUGFVkYaGBkoSGBiIXLKzs9GYbm5u+vr6QjAhtbp166Irr1+/rq2t3bBhw2fPniUnJ6PkqPWFCxfQ/rq6uign6hgUFEQVQY/gWxTYzs4OZQ4ICEAsiAQ1EbKTN3shIioYHBwcEhKCC0RHGHxELrgmeVBuUiSCqnl7e48cOXL9+vXTp09HdUoiBkgQKe/atQu9gC5G7gotg7JBXKtVqyYq2CxJN3GBjoA8eHl5nT9/vkePHmV9HZaKGnRk/8BjKMMwDMMwDMMwrKR8FqAn37p1KzIyslevXgpOZ5ycnA4ePOjr6/vNN9/o6enRSeGE8snlhaKhoZGYmIjE39tjC3Ry6OcdO3YsanNQenq6u7t7vXr1rl69+vbtW3Nzc21t7Q4dOsybNy8gIAAXgkEHhcGdx48fe3t7ozzKer5EIkFpFy5cePPmTTMzM9yJi4tDamiZgQMHGhoa0jqmHTt26OjoULJI8/bt29OnT8fNhg0bomVQWXzs2bNnUlLS5cuXaTsbKt65c+cffviBItKSqL/++qt///64QEiyTdjY2EyYMKF58+bCRiGEDA8PX7ZsGfoIcdXU1FJSUipXrjxx4kRUmQwcCLN///7AwEDEXbNmTVRUFNJxcHBYu3bty5cv0aeo1IwZMzIzM6tWrbp69Wp9fX2hIsbGxlRglAQF8PPz09TURApIdujQocOHDxdEAvcjIiJWrVqFMOhKiA3K3KlTJ0R/8eLFtm3baCdUUX3k4eExePDgnTt3orPat29fws139+7dCw4ORkTUSMH/joCyYKBZmjZtWr169VOnTqGEyq6U2KDzEYBAoIcgfGzTYRiGYRiGYRiGlZTPxbVr1+zt7RUWrWRnZ3fo0OHq1atr1qy5cuWKm5ubnZ2dlZWVra2tiYmJnp4eOZAWwqPFoOcbGBjQnhrSoqGE//rrr0+ePJk0aZKOjs6/WishkUji4uIQt0qVKtbW1kUZdMjLL4p348aNyMhICtmkSRMzM7MzZ860bdtWPvDZs2eNjY2bN29OB10rm5+2bNly+/btZcuW1alTBym/efPm0KFDr169Kmr5iVAG4RoVR3lOnTrl4eGxatUqlCcmJub48eNoB7TG3LlzaSsTwoSHh58+ffqbb75B4fHxwYMHGzZsmDx5MhqcjDVoycTExClTpjx79uynn35q1qwZ5DMoKGj16tUTJkxYt26d4CSIFrPs3r17wIAByBe1Q8j58+enpKTMmjULnYJ8EZLEW8ESRwVGW6G7d+7cqa+vj/oiC6SPlkcD0mospD9t2jTkPnLkyNatWyPY06dP9+zZc+vWLVojUwxoHyQyatSo+/fvr1ixolatWpaWlu88XQsFo0VJ7u7u/8p9dW5urq6ubuPGjdF3r1+/trGxKbS72aDz/qA/MGSYm5ujofnMcoZhGIZhGIZhWEn59NCalGfPnkEnNzY2lje45OTkGBkZLV269MiRIxcuXPD19aWFOVKp1NHRsUWLFl26dDEzMxPUcg0NjTNnzkDJJysPtHE1NTUo8FD4u3Xr1rdvXzI9IHqhe7iUndciBdxELAsLC21t7WKMQTKZDGGQb1xcHJmioMOjhOfOnQsNDa1cuXJWVpa6ujp0+ytXrjRv3tzW1lY5O5Q2NTXV398fATp27BgfH49SOTk5TZ06lWxJwjnuyuVUcNSCAnz99dezZs2iE9NMTU1dXFwMDAzWrl3bsmXLdu3aUZV1dHRmzpyJr+iA7U6dOtWoUWP48OHr1q1bv349GgpNunfvXjKCdO7cGcVDMA8PDzs7u2HDhm3atOnnn38WziND3X/66aeePXuSkyN0FroPvYOKa2lpOTs700IhMm0oVAQ3GzRoMGHCBLQ2ItauXXvixIkPHjw4efIkKiIqMHRu27bt9u3bixYtIr/XCNa0aVM3N7chQ4aUxLMywuvr66OEI0aM8PHxgVyVxLsNWgbl1NPTe49n2dXVdevWreh0CAAbdD4ykCTIBASLrTkMwzAMwzAMw7CS8lkQfAzb29srr0CBGqyrq/vtt9/269cvLi7uzZs3b9++ffr06b17937++efTp09Dva9atapgG/r7778RRjiC6vnz5xUrVly4cGHbtm3JN41UKsXN27dvy7v1RWsbGRk1b95c2dcv2R1KsgmOPC4LpiJct2vXztfX9/Lly05OTllZWRoaGjdv3kQtOnbsWEzvm5mZ3blzByEdHBxoPQud7fXOA9eVDUzkaYhsGbju27fv0aNHyURCp6fr6ekZGxuj8ckElpycXLlyZU9PTx8fn8ePH9etWzcxMfHChQv169dv3bp1UlISNQKCoWy9evXauXNnaGgoaicqsL4hR0QRUqPuQ8Wp9chNdTEFtrGxQTnJ8AGRsLW1tbOzI6dFdLj4+fPnUZJOnTqhAPSAIC9UAX0XGxtbkmZBH7m6uv7www8Qm3r16qGm73zQyOjzHsvlkDK6UkdHBxJb1h9Slfahw68NhmEYhmEYhmFYSfksQGFOKkDhsHABKPnQwyUSibm5uZWVFflJwZ1Tp04tWLBg3bp1Pj4+tMcqIyNj+PDh3bt3J9sKUvb29r579y50eG1tbTJtIJeQkBDEwh0hi6ysLEdHxyZNmigs2YBObmxsbGJiEhkZGRcXp6enV5RVBRFDQ0N1dXURmGwESNPFxaVGjRpnzpzp16+fpqYmCnD69Olq1arVrl270M0+dN7TiBEjZs+ePWzYMFtbW4cC3Nzcvvrqq6LOnyoKBb+/tE7Hycnp1atXycnJRkZGlKNCjRAMeeEiLCysYcOG0QV4eHigheXNMYiF2iEdBHN2dqabaPMSOhsulJycHCEuLuhULMHxc0xMTGxsbMuWLdGDCiX5V9ZPyEbfvn3v3LmzevVqdETdunWLDw+RQxlevnzZqFGjf/sg0wliiYmJZf4hVc1ioXHpaDR+bTAMwzAMwzAMw0qKymmSBYgKbCtQ+DMzM1NTU6GT42bv3r0bN24cEhICVV8wduBCvQC0oY6OTv/+/ZOSkvbt2ydYajIyMlq1anX8+PH9chw5cmTlypV0lpN87rQpyc3N7fnz50FBQVpaWoUWEnmhDDdu3HBwcBC8pSApQ0PDjh07Pn78GHH19PQePXp079493MH9omwQqGCdOnW2bdvm7e3t4uKSmJi4d+/eMWPGLFu2DMl+4AHYdKa46F3rTSQFkD2C/E8Xeig4HRleejuJ5C2bQkk+3LcUbdnz8vJCj6BV09LSirGUQeScnZ0rVqx4/vz5rKysop7KQvfBfVGPoWoODREREU+fPqXj33isZBiGYRiGYRiGlZRPDPRz3QKUF7+gNbKzsxGAzBDyURAY3worOOS/yvuH9PT0evXqNW7c+NixY8+ePSMDBDkw1ldCR0enKJW+c+fOUP5/+eWX1NRU5WVE6CbE9fX1ffLkSffu3Y2MjARjDQrfrFkzJH769GlU4Y8//tDU1GzRokXxRhB8a2Ji0qdPn5kzZ65du/bQoUOenp579+69c+cOqoDElT3mFGroUbgpkUhSUlJevHhhamqK1qZ2U06KtqRlZWWRSyCUxNjYODg4mALLpxYSEoLWoAUspS0k6O4KFSoYGho+evRIoSTvYUzBw2VnZ+ft7Y0m3bp1K1q1qBTQF/b29u3atbt+/fr58+cL9aSDBkSjoUEKTQSNg2KX+XFJNYtF2y/T0tI+0NLJMAzDMAzDMAzDSsp7kJeXp6urq62tHRYWJq8So/r4asmSJYsXL05PT0cY6Mxq/wDV+u+//w4ICIC+bWJiUuhOKOjS0NV79eoVHx9/6NAhwSokf/a5/CHohRYvKyurWrVqQ4cOvXbt2po1axBXR0dHKImmpiZK4uvru27duqZNm3bp0oU2dglxUbxGjRrdvHnz3r17V69ebdasGTlILqo1yDyBomZmZpL3GXNzc1RBS0srIiICOSL32AKQNQVGHeUzFaAjpcjQgL8o54ULF0JCQjw8PNTV1WkBDrJAxRGMqoNcaEFT1apVq1evjhRMTU0bNmyIut+/fx8pCMESEhKOHz9eo0YNR0fHdzokFjYfCeut3sOgg5KgJdGG6HShJKgIks3Jyfm3Nh08X23atBk4cOD27duRJhn7isp6yJAh1tbWS5cuRdb6+voITLkja8gt/m7btm3r1q0KpiXaJob2tLS0ZIPOx4dEqihDGsMwDMMwDMMwDCsppQ0UZhMTE3t7+ydPnkD7lVf4yRnwgQMHxowZc+nSJTqJiaLcvHnT29sbd4YPH17MNpyMjIymTZvWr1//5MmTL1++LMpNT/FkZWV98803/fv3h/I/fvx4f39/5JuXl5ednf306dMFCxbMnDnT1tZ22rRpyuuM0JWdOnWKj49fvXp1VFRUhw4diulZ8ny8fPnyrVu3pqSk0N4xXBw+fBixnJ2d0SANGzZMTU3dtGkTUkPFpVLplStXDh48qGCS0NTUPHTo0O7duzMzM5EsIh49ehRFrVu3LspDHnwQNzo6esmSJSEhIWSMePPmDeoSGBj43XffVahQAYVBxIEDB+rp6eH+nTt3SETfvn07e/bsx48fI5iBgUExLmzI/oVmiYyMRCy0Blmp3qMX0Nqenp5GRkZTp069fPkyZZqYmLhu3TqUpBiLjPBkKRQMtRs7dqyDg8OtW7eK2XVFB5bNnTsXURB+7dq1ECTcRAEgBhCGiRMnrly5Em2oYFdCsz948MDU1BTRBS/RZRQpD80MwzAMwzAMwzBMobRo0WLRokVPnz51dXWl9SZQmKGlz5w5s27dulu2bPnxxx8tLCxsbW2lUmlUVBRCWllZLV26tGHDhunp6To6OrTQBpq2vFJNTnB69eoFrfv333+fNGlSSXy+pKamyn9Essh06tSp9vb2v/zyy8iRI1ESa2vrxMTEFy9eQFdv3779+PHjzc3NlVfKZGVlubu7Q6U/d+4cueAtfj0LbRbbtGnT4cOHa9WqhXxRU+Ty008/1axZMykpqWnTpt9+++2uXbsePnzo4uJCB4S7ubndv38f5RTqLpPJEH3fvn179uxBQ9E+vjp16syaNUtPT48MOgiPiqipqY0ZMwYNK5FIkCaqg7zatWtHdUFpK1euvGzZsgULFnz33XfVq1fX1NQMCQlB3BkzZrRu3ZqCIV9coDDKO+DQiS1btly5ciXaDU2kra09Z84cfX19ITydt5WcnKywzRDX1BF0Ex1nZ2eHHp87d+73339ftWpVIyOj169fV6tWDX1RlLNqwfkOnT6uYKmpUKECBAPVT0hIEPag4b6CIEHAGjRosLEAiOLOnTvRXIaGhsg9MjISAjZ27NhvvvkGNRUMN3QC/bVr16h4Zd2gI4FMqFqZ0MRoffSrpaWl8t7LD4cWX/HQzDDMlw1exvKzB4bhlyDDMPwSVGUl5f1AHaHTlt4bH8lCOT9+/DhUeg8PD0H7perXrFmzffv2zs7OWlpaKAZuQp3u3bv3uHHjatWqhTtCSGNj43r16uGv/JoRFLtSpUpmZmbQ3h0cHEqy5Qcq+ldffQVVXAiMBHGNxFE8GxsbTU1NMge0atUKyvyAAQP09PQKtdTQaU0WFhb29vbdunWrUqVKMbo9eQtq2bJl/fr11dXVY2NjUTtUfPz48W3atBHWtjRs2LBGjRp4z6Jq1atX/89//oN6oTB169bV1dVFYyKir69v165dp0yZIirYXmRtbd2vXz8UFSUhaw7Sv3TpUkREhI+Pj7u7e0JCAu40btwYqaG15Q+cwjUavHXr1ubm5sgR1WnSpMmPP/7YvHlzJEXBqOROTk5khJKXW0RBFaysrFJSUlA2Nzc3FxcXUcH6IApPEwb0GoqBbhL6joxBCIBGo5tCSZAausPAwABNigL7+fklJSV1795dIWt5wUA68u6NBJsOWsbOzq5q1apUcupo1FRBkJA1bqIXUEg6yAx1cXR0RAEghx06dFA4Vx4idP369V9++WX48OGob+m5ji4JaASUuahFTNHR0TTgFOr6Gt/mnxkHQVE5I5NEEhgYiPJBpGg52cdtMqT5znVfDMMwZZ34+Hh2Lc/wS5BhGH4Jlgkl5UMMLrGxsaX6xocCvHr16h07dmzZsqVBgwa08ES+WaBt4v1CRg06xArlkTf94I6uri6UT+XTiMj1DO2RKUlhkI5IaZ0OgaxpIQat4NDS0sL1O7cRaWtr02HbhTq7UW5t2ktF5hJUHGIgf8w55UtmJrQMbapCFigwCoPwT548GTZs2Lfffjt27Fhan0LOjxFSkCiEnz17tr+/P9qcVrjQ8U90lJhyqfAVlYSaGtWXN2CR3Qr3UQblpiC3O5QsefxBXkJ4qgXanNpHfpGR0BHCTVzQTjSqFG1RRE1jYmJ27tyJXBRMNsULhiB7tKCGztVCCVG2QsPjI7klQjkFOUQwBXsN3fzuu+9wf9u2bUjt8z7IaJOqVasW6tEZBAcHo/Xq1KljYGBQ6LdxcXEquuWKXKDzq4hhGIZhGIZhGFZSPiNQgAcPHnz16tW5c+euX7/e1tZW3vgiv2WGXPkqGB1oZ01SUpJIyVsKKbQKFqLiKdSUQ2QXQKYEJFtMSHnSCyi5AGQWQBVRNkIhQP6iiYJvBadCZFNQqHtOTo5CyEKzo7VmooLjn4oqVU4BlJRyMNpyVYxBQeg+agf58MKWK5HS8VVUd3lrDrkuIqfOdJ56RETE69evbWxsdHV1lVc/FS8YhHwL05arQhtTaCvRP76rleVQVGDyU1NTW758+ePHj9etW2doaFjyrldZpKo5UJqbm0ulUj09vbI1YpJZlF91DMOUHHYAzzAMwzBlgrKrpHwgUMWNjIwWLFgwroB58+ZVq1ZNYV2DsLtHFbrpExSj+CyK/1ZeZywqJPnrKUlqJcy09OISWlpaO3bs8PPz69q1a/Xq1Q0NDV+9erVr1663b996eXlhuvvJdjYVJQAoQ2xs7Jo1a06cOOHt7d24ceOSrMlSfVTRoAPZNS9ARQaFkpOUlFTUajGGYZhCXznGxsa8/4X5AnjvozEYhim30K/lZajAZVdJ+XCg+larVg3K8OTJk/fs2TN//ny0Bg/77wFURdrQVHwwTA7p7POyUi9yhwSRWLlyJR5tWiNjYGAwe/ZsDw+PYpYXfTLQ5g8ePLh+/fqcOXN69OhBO7O+BIlSQR86gqyXRhOXqvsA9ljBMAyPSEw5FDkkGxcXp3B8CcMwzOd6A5bqS7CUlJQPKU9p+9AR0NLSioyMJDeuKuJCqIzp3mIxeurt27dGRkbGxsZFCRKCkTfcSpUqKfsSVlnIHXVYWFh4eDgKjwo6OjpCVAT3zJ+98SG0mK6gVVXnV6gv1ocOwzAMwzAMwzAMozpkZGRAPycPKdwa7wH5UXZyciJ3yMUEs7CwEIvF8gdaqT7kAdrBwaFq1arkUgflV51tTWhJiUQiHCX2xaCiBh2yfKua/ZthGIZhGIZhmHILKynFHOzNlAQ6DuxLbWdy/fN5DwIvvvG/PAFWxW2rampqERERwcHBvHibYRiGYRiGYRhWUhiGYQoZl1SwTBgfo6KiMFympqaWLU9pDMMwDMMwDMN8kbCSwjCMqqGiIxGGSx4lGYZhGIZhGIZhJYVhGKZQeDxiGIZhGIZhGIZhGIYpY7BBh2EYhmEYhmEYhmEYpozBBh2GYRiGYRiGYRiGYZgyhooadGQyWV5eHncPwzAMwzAMwzCspDAMwygjVc2B0tzcXCKR6Onp8YjJMAzDMAzDMAwrKQzDMAqookEH46N5ATRucicxDMMwDMMwDMNKCsMwjDyqu+WKB0qGYRiGYRiGYVhJYRiGKRR2iswwDMMwDMMwDMMwDFPGUFGDjlgslslk+Ms9xDAMwzAMwzAMKykMwzAKqKJBR01NLTIy8uHDhzk5OTxcMgzDMAzDMAzDSgrDMIziuKSCZcL4iLEyPDw8JSUF4yZ3EsMwDMMwDMMwrKQwDMPII1XNYmG45FGSYQh1iViNfwRSbbJzZXnsHpFhGIZhvnRYSWEYRqWQchMwjCqjJhY9j8lJzcrjhb0qi0wmsq0g1dMQs02HYRiGYRiGYZhPBht0GEal0VYX/3Q8/uaTDLEGW3RUFFmWbP+Iiq2raqVmsUWHYRiGYRiGYZhPBBt0GEbVycyRZbGlQJXJkuVy/zAMwzAMwzAM82lRUYOOTCbLy8vj7mEYUcGuq3z35bRfO08mYtuB6nQMrZpSE/HqKYZhGIYpD7CSwjCMSqGKBh0MlGZmZhKJRFdXl0dMhpFHV1siZQ/JqkFqZl4Oe81hGIZhmHIDKykMw6gaqmjQwfhoYWFhbm4uFosxbnInMcz/kZm39z+OTavocUuoAl3WPb0WnCTS5KMuGIZhGKZcwEoKwzCqhupuueKBkmGUMdKWGOlIuB1UAXUJL5ViGIZhmPIFKykMw6gU/Nsyw5QleI+PKk3puA0YhmEYhmEYhvlsqKhBRywWC38ZhmEYhmEYhmFYSWEYhpFHFQ06ampqkZGRwcHBOTk5PFwyDMMwDMMwDMNKCsMwjOK4pIJlwviIsTI8PDwlJQXjJncSwzAMwzAMwzCspDAMw8ijuluueJRkGIZhGIZhGIaVFIZhmELh8YhhGIZhGIZhGIZhGKaMwQYdhmEYhmEYhmEYhmGYMgYbdBiGYRiGYRiGYRiGYcoYKmrQkclkeXl53D0MwzAMwzAMw7CSwjAMo4xUBcuEUdLOzs7ExERPT49HTIZhGIZhGIZhWElhGIZRQBUNOjKZzMjIqEKFCrm5ubjmTmIYhmEYhmEYhpUUhmEYeaSqWay8Arh7GIZhGIZhGIZhJYVhGEYZ1XWKLBaLuXsYhmEYhmEYhmElhWEYRhnVNejk5eXxcMkwDMMwDMMwDCspDMMwyqiiQUdNTe3Fixe3b99OS0vDNXcSwzAMwzAMwzCspDAMw/zPuKSCZRKLxUkFZGZmsv2bYRiGYRiGYRhWUhiGYRRQUdOyWgE8UDIMwzAMwzAMw0oKwzBMIYMSNwHDMAzDMAzDMAzDMEzZgg06zBcL/3jCMAzDMAzDMAzDfKlIVbNYsn/gHvqUiAsQFXjvL+ZbFe8aNTU1LS0tiUSSkZGRnZ3N3cowDMMwDMOwksIwzJeHihp0NDQ0pFKpuro6D5efEsFkU4igSKX4igw9WVlZEolENde/qKmppaam+vn5BQUFWVpa9uvXD6XlnmUYhmEYhmFYSWEY5gtDFQ06eXl59vb2ZmZmenp6hS4VYUoDTU1NHx+foKAgXV3diRMn2tnZCctb8FVCQsLSpUujo6MzMzM7d+7cq1cvdI0Kvsnwfn3z5s348ePDw8OHDBkyaNAgNuh8RF69ejVnzhwIRvFHdebk5JiamiKkkZGR/P3Q0NDZs2eLxWJI0YABA7p161Zo9CVLlty7d09LS0vhfm5urrW1dZcuXRo3bsx9wXxiILc8d2cYhinnqKySIv7nH1PW4akG829RRYMOJs3Q5XR0dKC/cQ99OlGQSm/cuHHx4sUKFSqMHj1a0Ng1NDRSUlK8vLxOnDgBTb579+5t2rRRcd0GxdPW1oYUsQL2cUlMTNy9e7f8RjaJREKWl/T0dPmZjZWV1dSpUxWi79mzB9HRNQgcExPToUMHSJdyLpcvXz5z5gwFU+hWZLdp06Zhw4YtWrSo0LiM6oAeRH8V9S2Gd4X+VfHhEfKGMmdmZnLPMgzDlF9lW1WVFHVJvlbH3iO/ACRqojyZKCNHxEoMU9JpqsoOl2zN+SyvKOhgeEsJ26nU1dWhvU+bNu3UqVPQzfr06bNixQoEU/FlL8WvH2HemwoVKowZMwY6LbUwtNygoKB79+7hunnz5o6Ojjk5OaSrm5qaQpbk4yIWpEhfXx9Cha/u3r2LiPXr11fOheTQ0NCwZ8+exsbGSI0E8uXLl/7+/khn9erVJiYmygYjRoVeLVLpxYsXIyMjC30YISfm5uYtWrQggVHNAUQwUKIuYWFh27Zta9KkSfv27dkzF8MwTDmfMKuakqIhEW2/m/fkbZ6alC06ZV26RPoaoiZ24obWYpFYlM07VZiSzLpVs1jkzIX3W31eoHhD3YLafODAAXyEdl2UNUcikZCTHbzhEEVhXQzuk4KE++hTBKaNx0gHf/GV4IkZH+lbfITWVNT7ElEkBSA8smPb3yfDyspq9erV8nfWrl3r7++Pi2HDhvXu3buYuFeuXAkKCkLn9uvX7/jx49HR0ZCrQg06JAyQqHnz5jk4OAg30dGnTp0aM2YM+n3z5s2enp62trbcKaqJhobG+vXrL126pK+vr7ygLy0trWXLlm3btlVBgw6VNjMzU1gCpqmpefbsWVTnr7/+Qpl57xXDMEx5RgWVFHU10eknsruP80QabNAp+8hEO+6I2lcTz24lMdAUZbGWw7wLVTTokIuNjIwMQ0NDnjd/NsmQStEFU6dO3bNnD3qhKGuORCKBthMTExMWFgYlDQo/dGw6YUpeD8dXSARpQrtLTU29ffs2YlWrVo1ygVJHm6R0dXWjoqJCQkKg9letWtXY2BjfKsgAgmVnZyO78PBwHR2dypUrm5iYIBibdT4LQrO/UzOHIEEM0OnTpk17/vy5n5/f6dOnvb29TU1Ni4qisBQCctWlSxeo1jt27IiMjAwMDGSDjiqDyW6VKlVWr16NcUNh4guxwVAgP0qoCGpqapDkWbNmJSUlbd68mUqI91HHjh1fvXrVokULCCGv0GEYhim3qKaSgnJoq4tEGgX/mLIPJOt0kCwlK3d1R4m6RJTLKxyY4tV2FSwTptQvXryAwubu7s5+kT8LtOJm+fLlgjXHx8dH2ZpD7nXWrFlz5MgR9BeUNB0dnUaNGo0cObJevXrkIENTU/Px48cjRoyIi4sbPHiwp6fnuHHj7t69a2Rk9Pvvv7u5uU2ZMmX//v0mJibbtm3z9/ffuHFjREQEcreysho7dmyfPn3w4qRXJhl9rl69ijBIAemjnNbW1giDlMnQw333yV85MoWLQgkLC7t06RJ6sHnz5uiyr7/++vLly8+fPz979ixE4p2Jy+Ps7EwXCQkJ3P4qDp5KV1dXZV8DtJqPHlgM+Mrnv9Lvnwr35Y/hK/S9IAQo9EBZIaNigpExGoOMhYUFRiGKkpOTA6FdsWIFCqxshBL2lBVaC0GMhWD8RmMYhim7sJLCfAowfdAUXX0i21Axz7upWgqf78IUPy6pZrGgw2PqnJWVJWbvXp/jXQWtZunSpf/973/xoirKmqOurg6N+vvvv1+yZMmTJ08QC2pbYmLioUOHhgwZcu7cOXykkFCHYmJiYmNjo6Kipk6d6ufnB00JqeE+YiUnJ+M+IiIdfItgSDk1NfXvv/+eOHHi4cOHBVcsSPDAgQPDhg07deoUYuEjogcFBc2aNeunn36CzBTjgZX5vJw4cSIiIgJd2atXL3zs3LmzqakpFN2DBw8WYwkq9PEPCAggVb9ixYrcsCoO7V1SJiMjAyM8mXUABgT5hxf3NTQ0FJwUYAjS1NTEoEEDka6uLmLJ5wXpIp9fANGVT0kjcdIsIKcASlMhDPn5RlJq/0CDWHp6uoJHZITEbB4XNJqhAAqOumm3KY2NGEup5PJOyhiGYZgyByspzCdCXfTr3bwHkSJNKbcFUxwq7UOHB8rPIxNS6apVq86cOYOLvn37Lly4sCi/OUuXLkUwqDRDCjAwMICyPXfu3NDQ0OnTpzs5OVlbW1NvIikoYBcvXoQav337dgcHh6SkJAsLCyRLm7bw8fnz59u2bXNzc8P1pk2b9u3bh/fl1q1bv/76ayhX0JTu3r07a9ashISEr776ytvbm0Ju2LBh7969vr6+jo6OkydP5o1XKgi09/3790M/r169eqNGjXAHstGgQYOTJ0/evHkzODi4Vq1ahUZU8KcLedizZ8+pU6cgUZUrV3Z3d+e2LdOgfyEbixYtwvXMmTMxktDuSww469evv3PnzrRp0+zs7NDvOjo69+7d27VrV2BgIGbSGDratGnTp08fjDlkGNLW1r527RoCPH78GKnVrFlz2LBh9erVS0tLExVYn8PCwhYvXtyzZ09bW9stW7Y8ePAAI0+TJk369+/v7Oycnp6OMSo2NhbDXVRUFC4wtgwcOBDFQwEwpkVEROCrjh07du/encw6NGphNDt37lxkZCQK0KxZs8GDB0MyhcWJmzdvfvLkCcalY8eOHT16FOGtrKz69evXpUsXjFS8oZhhGKYswkoK86nmSSJMKH5/kLewjRofscmUPYMO8xlVrJSUlCNHjmgV0LVrV1NT0/j4eIVg+Oru3bu+vr5QiqAjQVMid8hQsSpUqDB8+PDnz58fOHDA29tb2AaFC8TasGGDi4sLFB5kBL2IlqqSe50lS5Z4eHhA5zEzM5s/fz4Us9u3b78poGrVqnhxbt26FYqTpaXlypUroYmhnNDrcE32gn379kE3s7e3505UNW7evAltHD3euXNnYd1W7969T58+nZCQAClSNuggMARm6tSphoaGwnpmCNX9+/dJ0iZOnMgrdMrEeGJgYKCrqytYWtGbeHLJloGbJiYm9erVGz16tJ6eHp569Cwk5MyZM7NmzcJNOzs73EH048eP//DDDxht2rZtiygPHjyYMWPG3r17MSbgkcf97du34w4GipYtWyKLs2fPQrrWrl0LkaPRJjU19Y8//sAAkpiYaG5u3rhx4/Dw8B07dmDcwKDUqlUrOrsNuWOYopU12traZF3C6IToKIOTkxOuyV9yRETE2LFjIdtt2rRp3749Uv7ll18OHz6MTJs2bUoWIoirn59fYgEtWrTASHXy5MkRI0YsWLAAccnYxDAMwzAMUzgS0flneaPqqlno8YlXDBt0mJIBRYv84Fy5cgV6y7Rp06D8uLi4QJ9R0NP8/f2Tk5Oha3Xr1g0XpJxAb3F1df3qq6+gUN24cQNaDR1ZJSrYswCVBqq7susTZErHVCMX2gqhr69fvXr1gIAAaPUoBhJ5+/YtGQWg/uGrN2/ekE6IAnTv3h26Fu5AzYNGx52oahw6dAiqLPRwqL6CEtuwYUNbW9uwsLBjx45NmDABPS4fhTbj+Pr6Kqxi0NTUtLS0nDhx4vDhw7lhVX0SIpHExsb+/PPPeH7JKoe/BgYGPXr0wGNLd/B0Dxo0KCgoaN26dRCJXr16PXnyZMqUKU2bNp06dSp6Hz1++/btH374wcnJ6b///S8ecKlUCik6ffq0n58f0tHQ0Lh8+TJGqj59+ixatAhihmTHjx8/duxY/K1SpUq1atVIorS0tDBS+fj4uLu7I1mMLYGBgQg2btw4DCCVKlVC2ZYuXYpRq3379qampjt37iRv7rTFDwMjHc9Hh5vMmTMHY+DmzZsx/qAMEFek9t1330GYIdK0oxBR0ALOzs5eXl5kykQAT09PVKRdu3Z2dnbKKx8ZhmEYhmEEg05ckijgjaxnDTEbdJgyZtCR/QP30Kdveegq0I4cHR2hYr169Wr06NFQWmrWrKnwe/Lz58/p7HBoRPI+4ejHcKTz+vXruLg4KysreS29qLOQFPxlCPsRaFErcomKikJqenp6t27dcnNzE2SDlCvoZigeisQrYFWNN2/e/PHHH+RDZOjQofLCkJiYiPshISHQzLt06aIgD9DbBwwYYGxsTIKBO+h96PPQhHkdVtl4u0ilMTExP//8s3AHz6mtrS160MDAQFidR6fpBQYGTpkyxcnJacWKFRhAli9frqurS4trMBAh2KpVq5ydnWl1D25CYDp16gTZyMrK2rRpk7W19cKFCyEtNEzZ2NgghdatW+/Zswf3adhB7t27d2/WrBkELzMzExJYv379xYsX9+nTB8FmzJhB/neQIL19sgoQFXh/l6+XpqbmzZs3Dx8+PHHixL59+yYlJSFTpFanTp0FCxZAaH19ff/zn/9QjpaWlkOGDEGByZAN0fX09EREDK1VqlRhgw7DlBCyqwrXond54i/VknzG3BlWUphyyIXQfIMOtwNTxgw6mEBDGRAWdzCfElK0oN68ffv2yJEjz549Gzly5NatW6tXry5v06HzX9BNDRs2VDjFRiKR4CsoVwo+UD7k5UeWHTpupkaNGvIHWpGPHmhotEGDe1ClOHnyJHRXKOfQXSMjI+Vn5OQvFvK2b98+BYMObqJP58+f7+DgwG1YRkGPo/t+++03bW1tYXygTVjyzy+tyFu2bNmgQYM8PT3j4+OXL19OthvIQFRU1F9//dWmTZtatWolJycL4pGRkUGmXghVcHCwm5tbdHT0ixcvBOnS1NSsUqXKjRs3UlNTBcfqooI1QYItKSkpqVGjRq6urn5+fl5eXgrnahU1X0cV/vzzT6QJoUUxhNRQ4AYNGqDkV65c+f7770nrQwlRQaH6qDhKxc4XvkhzQ1GK33vEKiruB+ZSaDD5NFVQQcXjpqWlRcfPCefi0aI/2rj96WenaCWUB4Vhn33lFlZSmE87DooeRMoiUkQVtEU5vEiHKSsGHbyn7e3tzczM9PT0+H35WaBjYnx8fDCFOn369LNnz6DtbN261crKivx9Ajs7O/QOplMjRozw8PCAriXMC0lLx6QH6XwUCwsyMjU1NTIygvJma2u7YcMG4Sxz+rmeLpDXp5/eMcWr9AcOHMCFoaHhkiVLTExMhMVckBba0wfpggIcGhpauXJlZTnkNiy7kMEXT668Dx16ThVCpqWlubm59ezZc/ny5Z07d+7Vqxft8YTWFB8fn5SUVKNGDWVVk9Sq2NhYDFN//vln//79Fc44T0lJqVKlCr4VPDcpJAJpxFd43QQFBSFHOrKqJEBc8YaqUKGCwrpCyDnuv337NjExkTZ/KVuFFA7nYr6Q+baaWqHWFk1NTYiZYEYsYSzabEjr1+Tl50NyUVgGK0gjvqX7dFKkSpkaacHv5cuXg4ODLSws+vbti9EDbbJq1aonT554enqS96tSyl15JQ7mRTdu3Ni5cyfeVmPHjuU5avmkPCop8i8xcclCipUiFvmkFZEOHj1Zwbd4Esv5LyASUVSS7GWizFxPzAYdpswYdPD61NLSUlj0wXx6VVxbW9vHxyc9PR369t27d0ePHr1x40ZLS0tMp9A1zZo1gz6TkJCAm+7u7ugy3Md0EBNEKGDoPmjjH+vnPtq50LBhw5CQkKtXr548eZIc9+C1inxp3RCypvOPue9Uh8DAwL/++gsXTZs27dOnj3KAmzdvrlixIiYm5vDhw15eXspDAbdhWbfpQAF750/ZGC5u3bp14MABJycnf3//EydOdOrUKSUlBQ84RiE84xEREQrL/YT0dXV1oXch/KRJkxBFXh1FFAwIiF5M7sgiNjZWXV2d9OcSarMmJibQM2mVkLz6hztkGBKcBBVaZhaMLwwIz8qVK4ODg3GhYI+wsbFpVAC9IksSi8TSysqqXbt29evXzy3gA3MJCgqCWE6YMIGOjRO+wht8+fLl0dHRmZmZHTt27NWrF/0YoyINiwfzzZs348aNCw8PHzJkiKenJ55oTACWLFmCx+3Zs2eurq76+voffa5I/tHRUPLPOJ3Kt3DhQgxW+FipUqVhw4axa/Py+V4rb0qKWE0ky5X9n51FUvRbMu+foUOtwAST949RpnhTjsJrF4lky0SaavraUl0NtcT03PSMXBFy11Arz1KXly16FCWqX4mfP6bsGHRESh5VmM8CZnjQW9asWTN06FBo5gEBAaNHj962bZupqSmmNbVr18bkb/PmzefOnRszZsyoUaOqVq0K1ejChQu+vr4//vhj69atP+IGKMgDJk9nzpzB1HPy5MmvX7/GZBfzUah/27dvx1R15syZhoaG3Gsqxd69ezHflUgkvXv3LjRA9+7dN2zYAHGCzIwdOxaTJG608gZ0NmiVU6ZMgWK2e/durwIwmDg4OGAIsrS0xMXly5djYmIQQHA6g1i00RJ6r62t7e3bt/FthQoV6BRzWrxDZ6XJj0KIhfvCR21t7dDQ0Pv372MwwRhCskovoOJ3Rbm5uUFJ/vPPP6tVqyYUCak9fPjw0aNHAwYMoH0Z3LnlZSIllV6/fv3ixYu6urrya2poYylEq0mTJpMmTYLYyB8vQLEuXboEyUlPT5cXGPJP98svvwwcOHDGjBnCzxXvnQti4ekYMWKEYBiFiKakpEycOPH48eN4TLp27dqmTRt5PzUqpEyKxWTYpfVuRkZGqGxycrKZmRnZYT+6NQeJ79u3Dw+4k5PTf/7zH1oEREsOkSn5OyfH5yz85damU46UlGxZj/oVvmlkkiuTXfk7ZdXpcJG6WqHB6lXVm9bBApcBL1IXHX5Ts7Legu5WeXnFPNqisLgsb9/XWdmy/zPu5MjEUvHw1hUH1KvgYq2tIRUnpeddf5by34tR1x4m5dt0yu1SHbHoWbxMJOLN2kyZMujQZDovjxeWfVLQ4MKPgQRmmebm5uvXrx85cmRwcPDNmzcnTJiwdu1a6E6YAv7000+vXr06ffr00aNH/fz8jI2NER56V3oBLi4uwsHSlGyhHaqcaaH3MaOqWbPmwoULJ0+ejEynT5/+888/Y3YVXwBervh21KhRlEUx2TGlNK1Rntq+ffsWgoH7lStXbtq0aaHRISRQP65evXrv3r1r165BoyhGJJgyh3BsuYJtl04xowU1UFYXLVp0//79vXv31qpVC894586dp0yZsmvXLnwFLW7o0KHDhw/38fGZO3cuRh4kpa6u/vTp0wcPHnh4eEC1GzJkyNixY9etW4cRifaPYGRITEzEyIDhS74wd+7cSUpKIic+SAR675IlS1AMT09PYbig/SlZWVn0K73ynimMRc2aNXN1dUWRGjVq5OjoSCfxITUMSkinf//+KKS85Yj54odB+sUe0giRoPVZkJ+0tDS8NxMSEs6fPx8YGLh8+fJOnToJ1haKpa2tDanu0KGDoaEhRJfMiG/evLl79y6EcPPmzUZGRpMmTSKLz4fkgoiCNQfiChHFa/TkyZMQ1F69ekGYEUY1vXTLr87LyMjA2+S///1vUFAQHrTSKDOdqjl79uy4uLhvv/2WDMeCQWfevHnVq1fHS61du3YKi6GYcqRcly8lRfYsJrPLV/m/mDaorLvzekx8Sk4h63RyZaOam3Z3NcLlHw+TRJl5Fobq9LEYIpOzpx15I5Ll5Vt3cmQG2pLtw+x7uRkLAQy0JP3qGvdyM5p7LHzBsbciafndfhUazxZkpkwZdGgyjekL5jf8A8inBNM+2iwgP39CR0BjWbVq1ZgxY2JjY6F1Yxa4ePFiBIZehHnVtm3b9u/fH1EA+s7KyqpFixZQwExMTEirQWpIE1Mi5YXlooJV38qZFnofJenevbuZmRkyhWJGdhwEa9KkSb9+/bp27YrZlYaGRvHZMR8XNDidOK7sHfDq1avQMUhXMTY2Lmrq3KdPH6gu6MpTp06RQYc0HPR+obtsmDI05Y2Kilq9erVwbPn/n/jl5lasWBGPMwZ5jB7QWufMmePh4RETE+Pi4oLhZeTIkdBLoVPhqe/WrRvU1DVr1jx//rx3794YAfARww702GPHjlWpUqVnz54Yl+bOnfv333/36NEDkhMZGblr1y4MEXv37hVkD0PW9evX+/btO3jwYHt7e4xXv/3229mzZ2fOnNmwYUPSzcgPDrQ1Pz+/7du3V61aFYpxs2bNyAJF7yMKgwJjlIP0/vDDDygDSr57925o1IsWLXJ1dUXZ6GQ3ZbskH4/yBZt1IOoQjJo1a9Ixarjz5MmTn3/++dy5cxgMf/rpJ1NT03r16gmu6IRYkydPrl27tuAOBmJz8uTJqVOn4vrXX3+FhAtH+71fLgqjLl7N06ZNw6MnKlgmWRJrDq0DEnzuKNvcBf8+dJ8WGZHFX+Hxp6RE/5yqSVZdSvadG74oCsaBAQMGKG97FP2z0ZLWNKGayip38RWhwgA8v2hAmlGQcZbO1LOxsZk3bx5STk5OVigqxaV93+QKXTmAQsVpzWBOATwmlKFXW/lSUtTVAp+nnnyQ2Km2oaWh+tc1DfZdi1U06OTKKppqdKqVb/R5FZ+1NyBepC7O/WcH1vPozOvPUqRqYuWmfBWfmZMry7fm5Ik0pOIdwyv3rJNvA/J7krLXP/ZVfHZde53RLSoi3/ndraJSsjefjxJplsuZoVgUly5KzBBpSv//zjaGUWmDDl54L168wGzb3d0dU3NeZ/FpwMsJGhRtWDAwMJCf22HaVKNGjaNHj5LOg69oEkl+dry8vDw9PZ8+fZqYmAiVCSpQpUqV8C3NTRHGzs7u+PHjZHxRmGLiI6LTiTDymRZ6HylATWrUqJGbm1toaOjLly8hG+bm5k5OTtD/EQUfi8+O+ehAp+3fvz8uyKwjT8eOHR89ekQ9WEwKw4YNgxIukvsZFuo9yZiRkRG3cNkFIoEHdtWqVcpTXgwOUF+hpj58+HDx4sXdunUbOXIkeaNISUnp27fvnTt3duzY0bhxYw8PD6g6M2fOhB61adOm8ePHY8xBdOiriIKbuIYGtWzZMkdHR0SBGkz6Kj6OGTOGVjGQPobhC+KKYWHp0qXIi5Yfrl27duDAgYKTdVLbRo0aBdGdMmUKksLQ16RJE2SBl5FgtUTcVq1a7du3b8mSJSgb0kTiKMzGjRv79Okj/G6P++TiR77upCvy+p0vFbV/IMXP1dUVA5q3t/fevXtjY2Mhe7t376ZzA+RjQWKzChAS6devn5+f3/79+6OiooKCgiDPH56LqGAHFuRz+vTpv/32G2QeY+87rTmQVQRArPj4+NevX2M+YGxsDGnH+Cyc8kYPNWqBwkC8MRNAYMzi8AhYWlqScUR4xBCFPqIwtOYuPDwcD76ZmZmJiQkewOLd4SN6dHQ0RZf/IQHlRHZJSUl///13XFycqampra0t0kfBBBvTOytCDr+EmQPKhoJhuEBjknEHsTDVoXP05B9t8tWFKiNllM3e3h7DC02T5EtOFUdJUDBcoKioi5WVFcLTORL8BJWJZ7zcKSm5sl/94zrVzrfXDKxfYd/NOMUA2bIOtQwtDPOfx2OBifFxWSLJ/ze7XHicPHLjM5GmRNlIUTAqFSy6yczr3cKUrDk7b8Z+t+NFbnquSCI+9Wfcvj/jzk5wsjPRWNbL+tzD5NDIjPwo5U7sREmZsqRMkYWGKI/XrzNlwqBDM2+82Eip4076NNDWdJogKv9YhL6AWk5Oaug3NwpAP0NhVtSoUSM6yJyOmpI/+pe2nYv+2UqjkCmSVc60qPukSuF+1apVnZ2d6WdzBJBfXl5MdsxHR7uAovR5ZStPodoCZt7yd4o3ADFlAjyny5YtIwNxoaMN/UKOrj948CD+4iNtyyIVaM6cOd9//z10JFzTSXajRo3q1atXWFgYhpeKFStCVRMstrQJy8vLa8CAAU+ePMFoYG1tXaVKFXKLI8y2cYE7U6dORbBXr14hCpQoKJDySinppQ0bNjx27FhgYCCyrlatGnJHgufOnSNfJxQMKWM2D604NDQU+iG+cnBwwAgpKK64mDJlClpA/ph23Pzqq68CAgIoJMvJl0fePwhyAkGdPn36vXv3oL37+/vfvHnTw8NDofcV1m3Rew2vOfqYlJT0UXLBYAuxX7hw4b+y5kRHR1+4cMHPz+/+/fsoCcqmoaFhZWWF52jQoEFkNkIiS5cu3b9/P57N1atXI/d9+/ZFRkYiupOT07ffftu5c2fkgpCIGxISMnLkyLi4OETv1KnTqlWraH8ZHoq2bduOHj0aiRe1m0mIjoeuT58+GCiojqgXUvj1119RBijbdFKnnZ1d165dBw4cSKcRvbMiaMNNmzatWbMG95Garq7umTNnrly5gtQqVaq0ZcsWJDhjxowDBw5gzrN582bBhZaOjg4eagRAy2P8QdsiQPPmzceOHYuBiEooX/HBgwd7enqi8Ddu3EDiiN6iRYtp06aZm5ur5q43prwrKeriUw8Sw+Ky7CpotKqm72Cl9Tz8f60qUrFngwr5ykKObNetWJHa/5xvlT+Xl6oVZ4WRiTR1JBNa52+RfhGbOWHfq9wcmUinwACkKQp5keZ18PWhUQ6G2pJvGpvMPvC6PBp0xKLUrPx/rBYzZcmgI/4H7qFPSfGOS4rycExGnGL8Hxf/u1NRmRZTGFqJ837ZMUxpoCbO/zlK8u8XAkODk6iV1kCHlFGkUh1Hc/OKfAyh0hQzhtO4AUWLXIfIDyC0pgYalLBZA3+hshoYGLi6upLnAoSXP1+GflQ3MTGh7VEUQN41rHww6JyWlpZkmC70kBryB9+uXTsa9zCeSKVS6FoKm0cwpyfjsmDLlk+NrNIojHzVaL+MhYVFMTss8o8HKc0uKyWR4xd2UUCc0OM9e/ZcuHAhPl65coX2lhYz56HtS4GBgSTMFSpU+PBcaJ/RsmXL1q5dC0lGyJLstNLU1AwICBg3bhzJM604S0xMJEfm0dHRU6dOxTOFm0lJSVFRUbjAfX9/fzzayA5PBMLgIzk7pz1iEH7cTE5Ovnjx4q+//hoREWFkZISvYmNjN27ceO3atU2bNpFrqkLFjKLHxMQgR2oxZISH3dvb+/Dhw2QsRr2QPkp++/btCxcu0AGdp0+fLr4iuIO6oBjkbwgfUQZS3RGefKUjUxSY5jyUOwKfOHFi0qRJqD4GLlQcN8PCwn755RfUZc2aNQ0aNKAmopIj07t37545c+bJkyeoOG7S5tDIyMitW7ei5OXthyi10hw4SuMliASl+cmKpZL8xEWqsf9FUqr+giXipITsI3cTxrc209eS9HA18nn5ViT9Z8VNtqyajXYTx3zJv/0y9faz1HyvyVl5crYIOn286PSz82rY6X1lnf/r4N6A+IS4LJG23HIebbUT9xIehadXt9Tu5GK44ER4dp6sHHrSycjFP5mY/SIzZcigwzAMU4ZIz5alZMpSs/71zC5fw8/I1dAolQ04KZl5mZmy0tOzkbKmtMjkS3LInfwqg3fef6fhuPgA/yqYQpiizMTFG5cLVczeaXHOypVll6ZCV0oil28g4439RWkr2dn16tXT1NSEtDx69EhwfixvbSHXLYLk7Nix4+LFiwhmY2Pj4uJCbrw/JBepVLpq1arTp0+TF+TFixeXxKNwZmZmq1atunfvbmVlhQtHR0fkcvny5bVr18bHx//22299+vRxcHAQFazl0dDQSE1NDQsLmzFjRoMGDXDz2rVru3fvTkhI+Pnnn2vXrt2uXTsqFQqDcqKQTZo0WbJkiYWFxZs3b/bs2XPjxo3g4OA5c+Zs3769KB9qFF3+xDrku3DhwoMHDyLNatWqjRgxAkWKjIw8dOjQmTNncE07rd5ZEXLI1bJly9DQ0OnTp6PYnTp1Gj9+PDnTIdMzrXJCAahtkeODBw+mTJkSFxeHWnz33XfNmjXDsIB2RsWRzrRp037//Xfy5EUl19LSun37dv/+/bdu3WpgYBAQEDB//vyIiIgrV66cP3++d+/e5eoodDRidq4sS1Zau5ZK4yUokcjScsQZueLULJFGpixXNQY+mUxUugVRE+3yjx3ToqKGVNy3rvHac5FZwplLOXl93Ix1C44V33kjNi8rT6T1Pw9vZo5MlJojypX8T8drSf6/aUImqmuno17gl+fS42RFI5+aOCst9/KTlOqW2pVNNKwqaISVy11XOdmitGwRu5Zk2KDDMAxTCmiIR++Pg4L8HrMpWf5cJaqUbC75DkZFstKa9eTKzAyle4eaVjKUZqu8Kg8VC6pmUVvAVAcdDfGKS8nrLyZBqEpr3l8aIpcnUtcQ7x1kUstKPTOb7TqFiJ+enp6+vn5sbGxiYmJSUpKwUxUCCbFcvHix/ClXL168CA4OpoVmo0aNsrW1hZL/ToNOMbmoqamlpKQcPnxYq4AePXqYmprGxcW983FAkZDI2rVrDQwMJBIJPUF16tRB4j4+PjExMY8fPxa2htHuyJUrV/bs2ZP2GbVu3bpWrVpeXl4oz7Zt25o3b47cKTBZWHbs2KGrq4tkmzRp0rZt27Fjx164cOHKlSt+fn7t27cviXcSMgwdOHBAQ0OjevXqO3furFKlChJHcyH9s2fPIh3aQlWSilhaWjo6OiIkrY0yMTGpV68eGp+2gio7OQbbt2+PjIxELebOnTto0CAExs2mTZuiI5DygwcPDh069P333wsGYpStU6dOy5cvR4Jo3j59+qCtJkyYgKYLDAzs3bt3uXo0dDTURv768o/7qaU04pXOS1Cck2OQJ9OTBqSoidNUZIkO6piQISu9F0e+a+QXabdfpjZ20Ktjo+NWWfdWSHL+OeIykbaetH+9fJNldHL2icBEZVNLXTudSX2s5f0oJ2fm7b4Zm5qZJ9h0LAzyx7fM7Lw3CYUZLcSiZzH5S/YMtSUWBtKw8PJ3gDeqmyPKzuMtV0yZMujwOSAMw5QhEtPyRO8/XpXNBfa5+dpbmThtAYoZtDgoTtD3SrJu6PPO2ZIzZTFJuaU4Ly8NkcMsU0OcnSvjqWbh3VpwLA40ecxqdHR0oPwLckie4E6ePKlw1pKmpqaZmdmoUaOGDBlSwuOxi8mF7jRo0ODatWuZmZnkrqV27drK2xILfXyMjIyQckJCAvmd0dbWrlKlCplvcFN+5oZcKleunJaWRmXG327dup05c+bgwYNBQUHPnj1zdXUVAtvZ2aGQycnJFNLQ0HD8+PH+/v5I89KlSx06dChJrSUSyeXLl2NiYqRSKa3NoSIhQbQhOSknS1lJKoIWQ3hh4RKCZRRQVNbh4eG3b9/Gtbu7O2qKRMgIhXQGDRp0+PDhR48e+fn5oWDyftArVqyIYJQsuqBWrVoYoOLi4krSHV/coyF6HJERBR1eQ1zGyi2WitJl+Uq26qBWmttxxKLcjLydN2IbO+ipS8QD6le49Sj/yRVl5TWpYVTTKt92fCQwMTw6U/kUqnr2uvgnfycrJ+/ovcTU9EzBykNzCZmoSINFXGqBa3M1sZ6mRFRetUN+wzJlzKCDFy2ta+UeYhQmrO8089FPjmwNZD75a/a9X7WyUi1W6aVdVo6Vz87OtrS0XLNmDdSzQh1zqBRq/6ctlOrMTfbxhUHMk82iZ1pSKRT7lJQUXFtbW2OGI2y7ozOPunXrBpWebAG4o6urW6VKlRYtWjg7Oys47X7vXJDI9OnT9+3bt2HDhpcvX44ePXrz5s01atQofoMPHa39xx9/HDhwICgoiDYW1a1bl+ZpSF9hYxTtKJQ/3wC4u7v7+vrGx8fHxsbK2zXoUAXhI2pqb2+PkiNYWFhYyZs3NDQU5TQ0NKxVq5a88UXeSda/rUgJGzwqKgqlRVw3NzdNTU1qfBpzzM3NUZeHDx9GRkYiDIYg+YLJ96ngjkdNrTxup5CJ3uVgRTVfgjLZh733y6C6LxWfCEyM7pZTUV/a9SvDGUbqyWm56D/P+vlOvnLyZLtvxhZahqSM3PCEbOGdpiYWRyRl5/7vsCbssirq5aRXYCfCt+lZfPYxw5QFgw7ec3ipV6xYkQ4m4E5iaMqF2RL9elaMsQbBaH5Mh49yuzGfSD7VxZL3nkuJS8spZOmaNXNFuuplxhFuCX2lQ0MjZ8mfsajqErG2prh0f6/+6CJXsOVKwgadwsD7CK+tw4cP4wKi1bhxY/kHk/xke3t7165dWzBGkIMYfJQ/7ftDcqGZFR7XmTNnvn379tixY0+fPh05cuTWrVudnZ2LseloaWlt2bJl/vz5KSkpNjY2KCSeo5MnTyYnJ+ONXMLzB8hOUZJl1yjhexg1KNniT9L4KBUptMD0O5NysYXC8Hrz4q0iLtbaj9/myNRKxR5Rrlo+M0dWumtmpeLw6MzD9xJGNjO1N9FsW93A91qMhaVWx1r5J5MGvk6/9TRFpF5ILx69lzBmxwth5Y64oN/Ts/MUNmHhr6a6mn6hC3BkImtjDfyflpkbm5ZTbh3J8DjClCWDDsZfvHp1dHRYIf+MlGQtzKecED98+DAwMPDFixeenp6YjRU6/dLQ0Lh58+Yvv/xSuXLl0aNHs0HwY/H69Ws0LNp/6NChgruEj8utW7fWr1/v6Ojo5eVFp4SUJbJlmwaatHDQSst+H6fIxkZG6hoapVGuxISEzNI8V1VNLDLSVssuI75wS6JMxsXFZWVlmZmZlXBNxEcHIjSykd4gd93S/F25dEQO6WYmZmTn8EKd/5ljSaWYzKxduxZDKFrIycnJw8ND2RVxTk4ObgrvNflFLh8xFySrqam5cuXKzMzMs2fPPn36dOLEiVu2bLG0tFQ44FywK7169Wrz5s34tmPHjkuXLjU1NaUj5zZs2LBx48ZCHyIURsFAc+/ePbyL8VjRViP5YsvbQfAGf10A3vjkaLmE2Nra4m9CQkJISIiLi4uwCg+Jk/ccJPhvK6JglCkUVArpGBsbR0ZGoo60zIcqiKbDzTdv3iAF1NrExIRnI0WMeHn/7WeztLeklOabpf0SVB101MX9dkUHPMss1KTyEdnzZ9yIpqZo0YH1jX0vR3WoZWhW4P5m983Y7IzcfFfHhVmaUtNyRYK1iRzg/O/PCndfppGtp35lnVsPExXMGGoaak0LTtGKSMoJT8h+nyNFvwC9TEI+iximjBh0aGbIL7/P1fLa2tp02ij9oKcKpcIcdNeuXZiNGRoadunSpdBf8HAT07iFCxdiRouPmKEOGzasXJ0WUXocPHgQ837IQ7t27UrDoIOH3dvb+8qVK7i2sbH59ttvy9pjIzLRkVQylKS81ylXJkbqIkmpDMU6MmlmZm6pPsU5uWX1B1A6a1xQm6H4PXv2zNPTc9CgQT/++OPnGjpQHH0tsaG2WmlmUVoiFxcnzsot7y4b9fT08J7KyMigY6oTExPx5vLx8SF5g2hZWFgou0r5t34D3y8XkJWVpaOjg5CQ8GvXrt25c2f06NEbN25EeGVPMZgJRERE0D6pnj17YvBPSEjAta2trYuLi/JZXXTs99u3b93d3ek3IeR15syZs2fP4ltHR0d7e3vBzIQAb968wUfUBX/xACLuhg0bUBdk0ahRo5K/Ppo1a2ZkZJSUlLR9+/aWLVuamZmRU2QkiPlAnTp1MKv5VxUR+gJvPS0tLdoSVaiBDO3m6uoaEhISEBBw+vTp3r17p6SkILCuru62bdswpJCDZFpfzHOJQkc8TXU1He3SUkY+wUtQVUYeDbGGVFzq6r662P9pSuDrNFcbndbOBlY2Or3djHA7IS338L0EkbTwN1e+6UYiLu6Aeqn43su0F7GZ9iaagxuabLgQlX8wuRA+M69ONX1Xm3w3PRdDkpMSs5Xd9JSDR0UkURdpq4vy2KLDlCGDDq1i/Vy/kZZnMAf6888/L126FBoa6uXlhRnYO481/WSWJsyr9PX1i1qPTTutTE1NySZFF9yhHwU8iZiP4pGUd3/wcZ93c3NzUcGqeHRcWWyinDxZwWnT72PQQcTSObU8/zjYfD+1vGBCCdqVKZJzWgEhhBIYHh7+2X9LyM0T5ZbmrLyURI63lZB7419//RVKPrR3iFZMTMy1a9cePHiApsG33t7ePXr0+EBb4YfnkpmZiWF27dq1Q4cORSy88UePHr1t2zYTExMFmw4yMjQ01NPTQ2qYFXz99de6urp4HYSFhV28eFEqlSo8LGRdmjRp0rNnz+rXr4+y3blzZ82aNQkJCRjbv/vuO0QXouAOEhk1atSAAQMsLS1RC1SKnEO3atXKw8MD5ZRf7FMUmKK4uLh069YNVbh79+633347cuRIOzs7JHjw4MGjR4+OGDFi2rRpxsbGJawI2aFQPJQ/ICAAAdBcqIKDgwNiKYs9mvHcuXOJiYkzZsyIjo5u1KgRbv7xxx8bNmzAIFO1atXevXujkOXTP07JRjyZpNQSL6WXoAoqKVm5ok8xAquJM1JzdvvHudroGOlIZnexauiQ/1CceJD4Mjzj/e0sEnFiQvav/nEzOlrWtdPxam+x9PCb/NOy1MSi7Dw9PemK3pW01fOXA2+7FlNu14BqSfFPzIoNU2YMOvRLSHp6OmYSrJN/YqC3//777zt27MDc7vvvv1ednzWK3x5P8ypMy+bNm+fs7Fy5cuV27dqV8GQQ5sMb/0NnCGpqq1atqlWrlqOjY5cuXbjBmdIe5W7dujV9+vT58+c3bdpU2GxCblPFbABj/j15BWRmZpLvbfmRUyKRWFlZ/fjjj9D8EUB+VoMouQV84lwg8xYWFuvXrx85cuSjR49u3Ljh5eWFNPX09OS3M+MaY3KHDh22bNly6NChv//+G6N0SkpKQEBAXFwcXrgKJ3mTO2dkNGnSJHNzcwzsiYmJ+Ign7qeffurUqRPy1fhnrx8CW1panjp16sSJE5hvpKWlpaam4madOnUWL16sra0tGHSo8PLKs/wdRMnJyUH6r1+/PnfuHOry119/6evrI8Hk5GSEwZ2YmBgnJ6cSVgS1trW1rV69+suXL1+8eDFkyBD6rWjPnj24UGhMTDPq1as3d+7cadOmvXr1iixHuB8bG4swqOCCBQtsbGxQGDRCoXVRrhGj+jOicq2kSNWO3E2Y3dnSQEsystn//QK32z/2Q5NVF/ucjezqYuRirb2kZyUzfemeW7FxGXmOJhreHS1bOukjyOarMf50Vnp5fMeI9DTy//EKHabMGHQwCcBLNCIiwt3dHdMLfsMV01Cke9Dcgs4Fo8lNURNE2t+OkIUGUysAiWgXIPkHdAGtf6GpofwLTPmm4NRQISTNOGl+RlkrvAiFiHQeB+1+z/8xueglQgpREBLzMMyfkD5mcpT++7USgiEiTbDI3yEtIGdpLCUqVao0a9Ysbgem+Gk0PeyChbGYXSpFhSGrzdOnT6H14XHGk16oBackWTCMgJaWlq6uLt6bOjo68tYNBweHxo0bd+3atUqVKtAAFd4gFAtRSmhG/Ii5IFjVqlVXrVo1ZsyYmJiYy5cvT58+fdGiRUhceDPS5vcpU6Yg7pEjR4KCgu7evYuk+vTpY29vv3LlSlzLL6IhB8/Lly8/d+7cqVOn0tLS9PX1q1WrNmLEiM6dOyuYmTIyMlq1atW0adPVq1c/f/4cZbO2tm7fvv3YsWPxOhB+j8F95E5nkBd1Jzs728TEZP369Vu3bvX19Q0PD09KSkLBnJ2dO3bsOHz4cFp8VMKK0I9DkydPxiziwYMHKDZmC2ZmZjRxQqYKjYmW7N+/PwJs2rQJydIp7MixUaNG48aNc3FxkT9pS6Hkxd9nVHbuXa6VFHXx87fpZ4KT+rob043gt+lXHxfiDlnuWKsSJCsRJyRlf/vLi30jHRwranq1NR/X2iwjW6b3z6of37sJk/a/EpVb3/sykb6G2EBTxFoIU2YMOvSmxxs6q3x4Mntv0D60tZtmGJiTPXnyBNMpR0dH2l2voIdgVofJ2evXrzHdwewB8xhjY2MEo9kbAtMUSv6np9TUVMxm6Fdr+pa23gizEJo7ImX5KR3531EvgMqAALiD9x9yx0c6xUzBWIMAVGZMm2hpdGBgoIaGBqpTlMaFkJQX7cOnj5jJ4StEpFjv0UpIMCoqKj4+3rQABCDzkLSA8iBaJCeYtWBiTWa+YgJDBjAdR8sjsJWVlbwk4CvqJo3CPLAK3U2nxgrdpNzd6DU6xRbqipGR0b8qBvPFQMZlSAsEknQkPNHkTfZ/Zpvq6pAiSBfdxzV50xCOwkE6whZCJEXJyqeAb/EIkPSSfvveh+Aw5QGIyrJly5RnLHhfGBgY6Ovr4ytljzZCLAghXkbv3N380XNB4Jo1ax49epREnVJWeBbwfOHdOmvWrOHDh2MQxre2trY2NjaI0rlzZwRAvrjGYyKEt7OzW7Vq1Q8//IA3PuLiI/4WdVzXgAEDWrZsiZTxwFoVQDMBYZKD2cLx48dxE1nQYjrlO6KCfWSY1UycOHHw4MF4EeCVgTkG3hf4m12AqMDx0DsrIqTm4uLy22+/PXz4EEkhI2RaoUIFzAS8vLzGjBkj35g05/Hw8GjUqBH0/JcvX2JIQXikj64R0iy0LsXcZ1SZ8q6kyPJdIHdxMaRPO27EpqfmiLQUJ4q5eQVHWRU4RS5Rshpqfz1Nab0iZG73Sl1djCroSvQ085s3NCZz7aXoNRcic5FOOTbomOiIDDRFaTwZYcqQQUf8D9xDRYEX/9y5cw8cOGBiYrJly5aAgICNGze+ffsWEwhra+ux/4+9O4GSqyoTB15d3Z3e0unOQkgISgIhbMqOIIjAADo6ioAIsqgDZwTcGEFGxG3QGTcE8eg4CC6Dg+KGuCI6KDijMH+jRCAiAUzCEghZSLrT+/7/6Cs1ZVWn0xBI6oXf7+TkdL+679V997269b6v77vv7W8/8cQTi/8gFtc6t99++1VXXbVo0aK4+IgLjriUOfnkk0877bT6+vootmbNmre+9a2xhfiKijAp/o9f0+zIF154YVysvPnNb44ycZUWVzOxMNa6++67zz777LgovPjii88444xYGLW67bbb3vnOd8Y7fv7zn0+3M8Rb33HHHVdfffVvf/vbNKZ66tSpRxxxRGxn5513TpcvEaTdd99955xzzvr162NTp59++j/+4z9GVeOa6brrrjvggAPKWyAuv77+9a/HpWps4bWvfe0HP/jBWPLP//zP0Sax/djT3XbbLXbz6bbSwoULr7nmmqhq2p2jjz46WuljH/vYkiVL3vjGN8b2t+3rrWiNr3zlK9/+9rfjwjSaJS40L7roojQmovxyPK5pvvCFL3zzm9989NFHI+iNy+U4rHHg9t1335ShiwP661//OoKNb33rW3vuuWfxup8dFQfoq1/9aqz10Y9+9Gtf+1ocpjhY8+fPLxSL6+k4kW655Zb29iefetDa2hon1bnnnnvggQdOsBpsA2prayNM+tSnPnX88cfHOfnlL3958eLFEVPFyXDKKafsuuuuxbdNLV++/Je//OVvfvObiCfjfIiw6vWvf/3f/u3fpmTQDTfc8P3vf3/dunVxWl522WVxtscnPfq6KFDI5txzzz3x0v333x8dRQRpZ5111pw5cypkNjEq8Up7ZCSi/fIrljSos7Ozc5NrDQ4ObnIg2HPxLnFWx5dsIUs+ZjXSaNZZs2bFpyA3mu6PteKjMXv27PRrSQ4oPa5rhx12iGuMdIPSxib0SamQuJbYa6+90txAJaN40t9R0gxraVMpgVWypLie8e1/8MEHp6dNxZLiRNLT2pE0XibNBJSG9KZHj0W/kZqrpK1iR6Jk9EW777572loUKL7ve8x9GWc5lez5HqTU5W9c3D7v/X9Mv63tHBxj9pxJ+f+3rDOV6ekfnuh9UpPyD6/tP/NLy2bPqHvRDg2T6/KPtg/cu7K3o33gyRFA1c/rqHBeq6CYrCV0mMjXSYS4K1eujB8uvfTSm266qaGhIa4nOjo6lixZcv7558clQgQ/hb9jf+9733vf+963Zs2axsbG5ubmuDS566677hwVoUsalhJBzurVq+PnFL2vX78+N/pHvHijnXbaKVZcsWJFhElnn312bvSv5bfffnt6iMPNN9986qmn5kZHoi5cuDACqrisibgr3iXW+ulPf3rhhReuWrUqXk1PpH7wwQeXLVsWof7nPve5uGBKfx6Mq58oE28a/1988cURkqUBRGM+GyJ24Yc//OGHP/zhiNlOOOGEiy66KKWlUpsURuU8rVZKVb3gggvWrl2bUmax/KqrrvrFL34ROxItE5vatr+/IyR4xzve8c1vfjMd35TeesMb3rDHHnuk1iguHG34D//wD3FeRZtEwBAhd5xdX/va1+LAxf9HHXVUbOHII49MW4tixQmdOOLf/va3H3roof1H5UafOBtnV/GDe8N//dd/nXPOOenJr2mIe5w2f/7znyMg//znP3/aaadNpBr6im1A+szG5zc+73GqTJ8+PU6b+FzHx/Nb3/rWv//7v7/85S9P3UgUjm7hd7/7XRz6o48+OvqBOBPOPPPMj370o3Fup3usCrdhpns2C7/mRjPLse7Pf/7z6PFe9apXRScZG4+e6tprr505c6ZxOmzMM3uG0dNd67l4l4lsM75bC+NcirNIEy8/jvFnEUqbGn9J8UuDo56VHRmzYuPUNg0W3mQzTnw5VKyRkdyqdU+d7dVVY0xUXJXrHxz5S5n8BG+7SoFpVW6kauUT/SvX9P3lAeex/TpziucWzNAGSOhsi9KNAxHn3HfffVdffXVEOBs2bIgI5/rrr4+Lg1hyzDHH1NTURIgbYcmHPvSh9evXv/jFL37ve9+bSl555ZXf+c53vvvd7+6yyy7/9E//NGXKlAhdIraJUPmnP/1pS0vLpZdeuvPOO/f29s6ePTv9pTrC+6VLl0YcNWvWrLhwuf3222Pj8dK9994bUfcOO+wQF1J/+MMfIjraa6+95syZE5cpixcvvuiii5544olY5ayzzjr88MNjYQRmESBFcH7xxRdHwJ8mEUxzW0yePPnWW29tbW2N+kfFop7bb799yfVZc3NzVPv8889fvXr1ySef/JnPfCai/fTc0zRFTvHMphNvpbvvvjvaob29Pfb9hBNOeOUrXxmVWbRo0TXXXLN27drYyHP0jKfKcckll1x33XX19fUvetGLzj777DhbVq1aFSfJD37wg/J7+z/ykY9873vfi2Px1lFxyP73f/83jvWf//znd73rXTfffHOcNieeeOLnPve5+++//yc/+cl73vOewrwPt91225/+9KfY5lve8pbYQjpMcfiKD9zy5cvf9ra3RQWiwJve9KbjjjsuCsRbfOELX4gyc+fOnXg19BXbRk4nzszoxKJfOuigg+Ln+MhHb/OOd7zjvPPO+/GPfxz9T/p7+4UXXhgf4V133TVOp1grToMzzjgjPvJxCsXJ8Hd/93ennnrqf/7nf8bZEp/3I488sru7O3qYvr6+FFlFvxR9YLxFinWjV4zTKTqBD3zgA4Iu2Jg0umSC84k8rcJAxakazbxsfpnxVjQgpahJanK7TqvSY5KxhI55KCfeUBEJf/KTnzzmmGM6OjoipPnYxz4W8fMdd9zx6KOPrlixIqKaCGm+/OUvpyzM5Zdf/vKXv7yzs3POnDlXXHFFb29vBMPf+ta3TjnllAh19tlnn6ampm9+85tpTuK99torQvo0I2BEMgcffHAEUbHZpUuXzps3b8mSJX/84x8jcIoKPPzww3ffffcuu+ySBlDEkpe+9KVpZoqvfvWrjz/+eGz2kksuibA83Rlx+OGHRwT+mc98ZvHixTfccMPb3/72QsomfoiQ7Morr9x3332jehG6RwWK/yAWK/7oRz+64IIL1qxZc9JJJxWyOc9KK61atSqqevHFF7/tbW+LmkT9jzrqqEMOOeTMM8+Mvdi2z6U//elPX//61ydNmhQtH2fFzJkz0/IIgN/97ndH4xQXvueee6699to4UhEbR4CdFkbAHGvFQYlzIzYV0fLUqVNf85rXxFl37733/upXv3r1q1+dSl5//fVxJuy4446ve93rNlafL37xi3Fo4pT7yEc+km7iCy8bFUfzJS95ycSroaPYNkQvdOKJJ8ZHsq2tLU2VFf3MJz7xiZNPPvkb3/jGBz7wgTQ0b7/99ktTgaTbN6LfO/744y+66KJHHnnkhS98YZx4USy6lDQqsOTP9fFznJMHHXRQvEVudMBOnEhx8i9cuFD7wzjiwxLfxQ0NDZscx5qmporCY86tBpm49haksOUM5Wa15l7YWjXojkw2okLHsKVBFuNPxUr6UokLowibu7q6IhRJD5XYc88903zDaT7jVatWLVq0KBozYuC99947PQBi3bp1EdJErBIBc4TNixcvjqg4yhfmSM6N3gnfOyqNYd5jjz3mzJkTbxFbi+uwWOWhhx6KDaYHhN92223xXsuWLYuoqbW19YADDoiLtnjr3//+97Gp/fffP8Kk9vb2nlGxkTPOOGPevHlRz1tvvbV4YrnYiyOPPDI2GwFVbLbkgR11dXU//OEPL7jggvXr17/qVa+67LLL0nQ/z1YrRTXird/0pjd1dnZG4Xj3jo6O2OuWlpZt/m+J//3f/53uKbvwwgsL2Zxk/vz5JdcuUTgOUDT+6aefXjhP0gNcDzzwwGirW265JbVYBNtp8sjrr78+rRvn2y9+8Yv44Zhjjtlpp53GrEzUJJXZZ599zjnnnOKXIoZP2ZynVQ22GXF8C48rjq7ssMMO22+//X71q1/F5zrdZRl9XfQPv/3tb+P0uOOOO+Jcmj59esrdFC7E0/k8UuT/vhTz+UKXEqtMmzZt1qxZrt1hHPFdGd/Lv/nNb370ox/NnTt3nC/lNAdwFIvCsYo5gMkiQQpb1HBu7+3zsybnBl3PshGVOEJnaGho11133WWXXWpqaswPN5GcTnErFX5OsU11dfXq1avXrVs3efLkiHBSlFsokGYNjEAoPTR0nHeJYnPmzNltt93uv//+RYsWxbvE1Vj8f8ghh7z4xS++5pprfve730UQddddd3V1daUJdNKzop544on4ztt///3r6+sLszbGJV3ESDvuuOO99967atWqKFN8X0yUH/Me+DSPxuWXX56eT/GpT31q6tSpsc2JzGszwVZKaa+GhobiCSYjqHs+JAXuu+++2M0XvOAFxfMNF1qgZEmaLzacfvrpJc+ETk8Ee/jhh+OHlpaWvffe+/DDD//JT35y6623xsI4cDfffPOKFSuampre/OY3b6wycTjSTEZx5sRl08aKTbwaOoptprv7q4uc4eH0wL4//vGP0fM0NzfHyfDd7343eon4dfvtt48Pcmtra3QUaWqwp/sWaXBfelyxxodxPjXRzaa7p8ef4DnNARwXADlzAJNNghS2eA+be9lO7kAjawmd3OhTDMofn8kzi3lSziK+dWbPnr3bbrsV50pieRqYE2H8+DMjpouwQw455MYbb1y2bNniUXV1dQcddND8+fMjSo/Q+k9/+lMsjJL77LPPdtttl25qSPMrlz/tO/0hPTfWyNWNXQvG8njHGTNmrFix4oknnvjOd75z/vnnlz9yeHNaKRY+b//kkp7lMcEHN6TC6ZRoaGgoPgSxMF6aPn16oWFPPfXUn/3sZ48//vhNN910zjnnRLw9MDBw6KGHlmeOigP1dIDGPxwTrwbbqjSbe21t7aRRP//5z88777wTTzwxOofW1tbo3B544IGrrrrqGX+bGFoPE4xyJxjcmgOYzMdOghS2XN+am96aO+yF+X7JQ8bplCo2JeEa+tm6xoqYNgKbVatWpcf99vb2Fto2he5p9EqaE7Qkx1ESOB100EEtLS2xqe9///tLly7deeed58+fP3v27D322OPmm2+OQH3ZsmXV1dUHH3xwSiHFW0+dOjXK33nnnXEBl54kmhsdrRoL09OLtttuu2nTpk3kQjDqGStecskln/3sZ//whz9cdtllU6ZMOfvss7u7uzfzbCm00urVq3//+9/39PTEXhSqFN/cz4csTxzN2OuVK1dG2+6www4l1y7lhdM5c+GFF46Tl0le+cpX7rbbbosXL/7pT3+6//77L1q0KDb4xje+sb6+fmOrzJw5M86KOElirXijjU1H/bSqwTYgeoDik6GhoeHBBx+8++67jz322DS79o033hhn77/+67/GJzr1aQsWLGhra4tzr6QzyW0qXQgAghS2aiCXO2bn/Atacl392oKNqtDL2aqnOEKbaWBgYPbs2WnOkV//+tc33XRTenD48PBwhEYRDKfR0cX5lPQtFUsi6q6rq0vPHkqbivh57ty5vb291113XWdn59577x0bj6DopS99aRT+8Y9//PDDD2+//faxPE27kyZajuP4u9/97mc/+1lra2tsLbYZodcNN9yQHnn+spe9LD1xfCK7ExHarrvu+tnPfnbHHXeMVSJs++53v5v2aPNb6cADD4z63HHHHddff/2UKVMiVoyKxcbXrFkzwRu7Mu2II46I4xLH/Yorrii+4yw89thjJbt/9NFHT5s2raurK45F+V0wJVuONnzta18b58kf/vCHD33oQ7HWvHnzjjvuuHEqM3Xq1MMPPzx++P3vfx+HuPilCOCXL1/+DKpB5r+uRk+hjo6OOFFTN9Lf3/+pT31qw4YNp512WjriacheGh6YJnePE2P16tUlJ3C6iyo++A2jxrmtDwAEKWwFw7mGxtzp+5gOmQwmdOISPELoJUuWDA4O6i6fhd5gePiss86aOXNmhD3vfe97r7rqqpShuO22297xjne8733va29vL/6jd5pwJILkH/zgB+lGqj//+c9pXpsZM2bss88+ESylR8AcdthhsTx+PfTQQyNoj+2nWH3u3LmF+Uff8pa3pNmIP/jBD8ZbL1269IEHHvj0pz99xRVXRDA2f/78k046aZOzGhd/icam9ttvvwjgo559fX2x2Ztuuin9cX5zpKq2trbGbn70ox+95JJLFi5cuGjRoi996UvnnHPO2rVry0epbGNe/OIXx7GIAxc7/oY3vOHGG2+Mg/Xb3/72wgsvvPrqqyPoLS68xx57nHHGGdFWP/zhD+PsuuOOO+JYrFix4stf/vLRRx/9y1/+siSfcvrpp2+33XYRisfGY61Xv/rVaQ6FcbztbW+L8y3OjajAxz/+8TvvvDNOxa997Wuvec1rjj/++MWLFz+DapBp9fX1//M//3PKKad8+9vfjs9mHPT4zH7jG99497vfHV1QHPo43HFqrVq16uKLL77rrru6u7uj7/rEJz7xH//xH+kWvMKHPfqo2trar3/967feeustt9wSnVL6gBfu9SvpQp1IAAhS2KIGcmcdkN9ju6o+CR3GVYkxavSPK1euXL16dYR8E7wZ5/kpjawpjzRKlkecE7H6v/zLv1x00UUPPfRQ/H/FFVdE9LJu3bonnngiCi9YsODcc89ND5uIXyM0uvLKK+MoxP8RLHV2dr7rXe96z3vekx4ic+CBB1533XWx8ZaWlgMOOCDeaGBgYNddd503b94999wTv8bC5ubmNMSjt7f3JS95ySWXXPLBD37wkUceed/73jd9+vR4i3jf+CKM4xu1esELXhBbrquryz01ReKYo3WKdyo2fsQRR3z6058+//zzYy8uuOCCpqamww47bMw2mWArRVX322+/VNXYZjTRV77ylSizdu3aaJ+odpyT2/wZFYdjxYoVN910U4S4t99+e2tra3t7exzf3Xffffny5SWHJhpq2bJlP/7xjyMq/tnPfhYf1TiFopWiJTs6OmIj2223XaFwnCGHH374DTfc0NDQEAfrjW98Y3nMXDIFw5577hlH4bzzzouuICr2b//2b9XV1XHm9Pf3Ryi+cOHCOKufbjXItDimZ555Zhz9OB/i5+g34uDGSfKmN70pPaE8/v+bv/mb6Bkuu+yyk046KTqi6LKiZ4jz7dJLLy2kraPY3nvv/fd///fRlcWpHn3RJz/5yfSw8zg/y1O3qXcCAEEKWyTGy+X6c8fsWfXWA/K9g5qDDCZ0ckUz5jKOCGwaGxvLn95SvjxC3Ne//vUzZ86MqHjRokXxPZQmGD744INPOeWUE044IaKjQsgU8c/5559/zTXXdHZ2trW1RTxfuB8hIp/9999/xx13jLh6r7322nnnnSO6jlB86tSpsakHHnggjlqsXvz1Fm992mmnbb/99l/84hfvvPPONLQnyh9yyCERq++7774RlRUOetQ5aj7m7Q8lO9XV1XX88ce3t7d//OMfj7j94osv/tKXvhRVKt/3ibdS7Huq6tVXX3333XfHr1HPU089NSLDd7/73StWrNjmz6jp06dfe+210aQ/+tGP1qxZEw27YMGC97///Y899tiHP/zhaK6SkVxR+HOf+1z8/+ijjz700ENx9OfMmXP00Ue/853vnDFjRsnGzzjjjF/84hdxtrz85S8vn+9m0qRJjaOKD9PJJ58cG4zgfOHChSlFGEfkoIMOevvb3/6KV7zimVWD7IqTZ8qUKfFhP/300+NAxzkzb9687bbbrvhB5tEjxavHHnvskiVL4pzZZZdd5s+fHwWiu4iTJ6Wto3BNTU2c59H7xec6OsY999wzOpO5c+fefPPNcRIWP0o5fv785z+ffnAIAKjAICWunLoHcrm+0UQA24BJ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" alt="DPDK and TAP plugin" />
<figcaption>DPDK and TAP example configuration</figcaption>
</figure>

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have installed the SR-IOV Network Operator.

- You are logged in as a user with `cluster-admin` privileges.

- Ensure that `setsebools container_use_devices=on` is set as root on all nodes.

  > [!NOTE]
  > Use the Machine Config Operator to set this SELinux boolean.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file, such as `test-namespace.yaml`, with content such as the following example:

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: test-namespace
      labels:
        pod-security.kubernetes.io/enforce: privileged
        pod-security.kubernetes.io/audit: privileged
        pod-security.kubernetes.io/warn: privileged
        security.openshift.io/scc.podSecurityLabelSync: "false"
    ```

2.  Create the new `Namespace` object by running the following command:

    ``` terminal
    $ oc apply -f test-namespace.yaml
    ```

3.  Create a file, such as `sriov-node-network-policy.yaml`, with content such as the following example:

    ``` yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetworkNodePolicy
    metadata:
     name: sriovnic
     namespace: openshift-sriov-network-operator
    spec:
     deviceType: netdevice
     isRdma: true
     needVhostNet: true
     nicSelector:
       vendor: "15b3"
       deviceID: "101b"
       rootDevices: ["00:05.0"]
     numVfs: 10
     priority: 99
     resourceName: sriovnic
     nodeSelector:
        feature.node.kubernetes.io/network-sriov.capable: "true"
    ```

    where:

    `spec.deviceType`
    Specifies that the profile is tailored specifically for Mellanox Network Interface Controllers (NICs). Set to `netdevice`.

    `spec.isRdma`
    Setting to `true` is only required for a Mellanox NIC.

    `spec.needVhostNet`
    Setting to `true` mounts the `/dev/net/tun` and `/dev/vhost-net` devices into the container so the application can create a tap device and connect the tap device to the DPDK workload.

    `spec.nicSelector.vendor`
    Specifies the vendor hexadecimal code of the SR-IOV network device. The value `"15b3"` is associated with a Mellanox NIC.

    `spec.nicSelector.deviceID`
    Specifies the device hexadecimal code of the SR-IOV network device.

4.  Create the `SriovNetworkNodePolicy` object by running the following command:

    ``` terminal
    $ oc create -f sriov-node-network-policy.yaml
    ```

5.  Create the following `SriovNetwork` object, and then save the YAML in the `sriov-network-attachment.yaml` file:

    ``` yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetwork
    metadata:
     name: sriov-network
     namespace: openshift-sriov-network-operator
    spec:
     networkNamespace: test-namespace
     resourceName: sriovnic
     spoofChk: "off"
     trust: "on"
    ```

    > [!NOTE]
    > See the "Configuring SR-IOV additional network" section for a detailed explanation on each option in `SriovNetwork`.

    An optional library, `app-netutil`, provides several API methods for gathering network information about a container’s parent pod.

6.  Create the `SriovNetwork` object by running the following command:

    ``` terminal
    $ oc create -f sriov-network-attachment.yaml
    ```

7.  Create a file, such as `tap-example.yaml`, that defines a network attachment definition, with content such as the following example:

    ``` yaml
    apiVersion: "k8s.cni.cncf.io/v1"
    kind: NetworkAttachmentDefinition
    metadata:
     name: tap-one
     namespace: test-namespace
    spec:
     config: '{
       "cniVersion": "0.4.0",
       "name": "tap",
       "plugins": [
         {
            "type": "tap",
            "multiQueue": true,
            "selinuxcontext": "system_u:system_r:container_t:s0"
         },
         {
           "type":"tuning",
           "capabilities":{
             "mac":true
           }
         }
       ]
     }'
    ```

    where:

    `metadata.namespace`
    Specifies the same `target_namespace` where the `SriovNetwork` object is created.

8.  Create the `NetworkAttachmentDefinition` object by running the following command:

    ``` terminal
    $ oc apply -f tap-example.yaml
    ```

9.  Create a file, such as `dpdk-pod-rootless.yaml`, with content such as the following example:

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: dpdk-app
      namespace: test-namespace
      annotations:
        k8s.v1.cni.cncf.io/networks: '[
          {"name": "sriov-network", "namespace": "test-namespace"},
          {"name": "tap-one", "interface": "ext0", "namespace": "test-namespace"}]'
    spec:
      nodeSelector:
        kubernetes.io/hostname: "worker-0"
      securityContext:
          fsGroup: 1001
          runAsGroup: 1001
          seccompProfile:
            type: RuntimeDefault
      containers:
      - name: testpmd
        image: <DPDK_image>
        securityContext:
          capabilities:
            drop: ["ALL"]
            add:
              - IPC_LOCK
              - NET_RAW #for mlx only
          runAsUser: 1001
          privileged: false
          allowPrivilegeEscalation: true
          runAsNonRoot: true
        volumeMounts:
        - mountPath: /mnt/huge
          name: hugepages
        resources:
          limits:
            openshift.io/sriovnic: "1"
            memory: "1Gi"
            cpu: "4"
            hugepages-1Gi: "4Gi"
          requests:
            openshift.io/sriovnic: "1"
            memory: "1Gi"
            cpu: "4"
            hugepages-1Gi: "4Gi"
        command: ["sleep", "infinity"]
      runtimeClassName: performance-cnf-performanceprofile
      volumes:
      - name: hugepages
        emptyDir:
          medium: HugePages
    ```

    where:

    `metadata.namespace`
    Specifies the same `target_namespace` in which the `SriovNetwork` object is created. If you want to create the pod in a different namespace, change `target_namespace` in both the `Pod` spec and the `SriovNetwork` object.

    `spec.securityContext.fsGroup`
    Sets the group ownership of volume-mounted directories and files created in those volumes.

    `spec.securityContext.runAsGroup`
    Specifies the primary group ID used for running the container.

    `spec.containers.image`
    Specifies the DPDK image that contains your application and the DPDK library used by application.

    `spec.containers.securityContext.capabilities.drop`
    Removing all capabilities (`ALL`) from the container’s `securityContext` means that the container has no special privileges beyond what is necessary for normal operation.

    `spec.containers.securityContext.capabilities.add`
    Specifies additional capabilities required by the application inside the container for hugepage allocation, system resource allocation, and network interface access. These capabilities must also be set in the binary file by using the `setcap` command. Mellanox network interface controller (NIC) requires the `NET_RAW` capability.

    `spec.containers.securityContext.runAsUser`
    Specifies the user ID used for running the container.

    `spec.containers.securityContext.privileged`
    Setting to `false` indicates that the container or containers within the pod should not be granted privileged access to the host system.

    `spec.containers.securityContext.allowPrivilegeEscalation`
    Setting to `true` allows a container to escalate its privileges beyond the initial non-root privileges it might have been assigned.

    `spec.containers.securityContext.runAsNonRoot`
    Setting to `true` ensures that the container runs with a non-root user. This helps enforce the principle of least privilege, limiting the potential impact of compromising the container and reducing the attack surface.

    `spec.containers.volumeMounts.mountPath`
    Specifies the path where a hugepage volume is mounted in the DPDK pod. The hugepage volume is backed by the `emptyDir` volume type with the medium being `Hugepages`.

    `spec.containers.resources.limits.openshift.io/sriovnic`
    Optional: Specifies the number of DPDK devices allocated for the DPDK pod. If not explicitly specified, this resource request and limit is automatically added by the SR-IOV network resource injector. The SR-IOV network resource injector is an admission controller component managed by SR-IOV Operator. It is enabled by default and can be disabled by setting the `enableInjector` option to `false` in the default `SriovOperatorConfig` CR.

    `spec.containers.resources.limits.cpu`
    Specifies the number of CPUs. The DPDK pod usually requires exclusive CPUs to be allocated from the kubelet. This is achieved by setting CPU Manager policy to `static` and creating a pod with `Guaranteed` QoS.

    `spec.containers.resources.limits.hugepages-1Gi`
    Specifies the hugepage size `hugepages-1Gi` or `hugepages-2Mi` and the quantity of hugepages that will be allocated to the DPDK pod. Configure `2Mi` and `1Gi` hugepages separately. Configuring `1Gi` hugepage requires adding kernel arguments to Nodes. For example, adding kernel arguments `default_hugepagesz=1GB`, `hugepagesz=1G` and `hugepages=16` will result in `16*1Gi` hugepages be allocated during system boot.

    `spec.runtimeClassName`
    Specifies the performance profile runtime class. If your performance profile is not named `cnf-performance profile`, replace that string with the correct performance profile name.

10. Create the DPDK pod by running the following command:

    ``` terminal
    $ oc create -f dpdk-pod-rootless.yaml
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating a performance profile](../../scalability_and_performance/cnf-tuning-low-latency-nodes-with-perf-profile.md#cnf-create-performance-profiles_cnf-tuning-low-latency-nodes-with-perf-profile)

- [Configuring an SR-IOV network device](configuring-sriov-device.md#configuring-sriov-device)

</div>

# Overview of achieving a specific DPDK line rate

To achieve a specific Data Plane Development Kit (DPDK) line rate, deploy a Node Tuning Operator and configure Single Root I/O Virtualization (SR-IOV). You must also tune the DPDK settings for the following resources:

- Isolated CPUs

- Hugepages

- The topology scheduler

> [!NOTE]
> In previous versions of OpenShift Container Platform, the Performance Addon Operator was used to implement automatic tuning to achieve low latency performance for OpenShift Container Platform applications. In OpenShift Container Platform 4.11 and later, this functionality is part of the Node Tuning Operator.

The following diagram shows the components of a DPDK test environment:

<figure>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABfAAAAJwCAIAAABJT9d2AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyhpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDcuMi1jMDAwIDc5LjU2NmViYzViNCwgMjAyMi8wNS8wOS0wODoyNTo1NSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIDIzLjQgKE1hY2ludG9zaCkiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6NDU5OURFNkVGQjA1MTFFQ0I4RkNCRDdEMzMwRjQ5ODYiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6NDU5OURFNkZGQjA1MTFFQ0I4RkNCRDdEMzMwRjQ5ODYiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDo0NTk5REU2Q0ZCMDUxMUVDQjhGQ0JEN0QzMzBGNDk4NiIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDo0NTk5REU2REZCMDUxMUVDQjhGQ0JEN0QzMzBGNDk4NiIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PuMA/3UAAOdKSURBVHja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uIEDBx44cECn02V7D4TLonfrmGuJzhHHHmm1Ws0DmffFbrdPmjSJwoOEhISXX365UaNGhw8fbtGixQ8//JB5hbdv3+7YsePSpUtr1arVrl27xo0b37p1a8CAAaNHj3amujiOc6zfMSaIDmDHz87tOofM3L9/f82aNVOnTh0xYoQoii1btqQa/vjjj9u0aUPV7twoFVu+fPmqVauaNWtWvnz5sWPHDho0qFSpUj169Fi3bt3bb7/t3HRqaioFOfRhxcXFtW7d2tvbe/r06VSezYCmMjOM0AGZoUZEjrNh6VUsp0qlE06jM+gNKtbKaHUMtYjM474cYFmtNn2Y6Oa/Vx/av6tXv8F9B40MCPQ3mWxipqndqRpO3DZevJpyO8FSobg6//eLWtgKFSpQvEWtMAVejs/FarWuX7+eupO6detWr149S6B26dKlIUOGOCeot1gsvXv3fuWVVwrqo9l/LfXClZRYM48pScDl2g29PodXNRlzb23dunXfvn39+vV76623goODUWmQBR0k8rpogUKCLvYeNz7CeacMXfXt3Llz2LBho0aNynYEuqMHv51grVC8AO7PcoMQaN+11Gs30hKsvFcRdZo1jz5ZFcOp9Axv1+j0BoOWtebfKBiqYTpyci5AR93u3buPHj3ao0ePESNGlC1b1mw20+fl+qfMO++84/jh5s2bL774Yq9evajfz7bkjz/+OGfOnFmzZk2cONFxWCYkJEyZMmXMmDEhISHO2wDnzp2blJR05MgR5/gyOun27NlDFeK8zqpUqRKdho6fx44dSyHHkiVLsr1NRKFQ8DxP12grVqwoV66cY+GGDRsoPhk5ciT94LiJ0jG+5v3332/YsCFt6PDhw/7+/tOnT6eFKSkpP//8c1RUVEBAAP363nvvrVy58ocffqCTy3G/Fb00bdo0+vhw4xUSOiBv1LVHRETIbg4gjZJNOpOsjLAc2FQ8/pTWahOVatW1SxcV2Y27caIGS6/3MBmNi+bODN24fsDwcR26vkp/mDmno+ZZRsXxBTRe1sPDo3379ufPnz927BiFKY4nbtLPp0+fpkuInj17Zkm9UUNPzTH1NJkvNqpWrVqA0YxGyVH0EbptS5R3mshgGCe4Cjp37t6967itPYcyjol1vv32240bNzq+6co5DQSFDbW6oaGh8fHxGKYOroPCmytXriifFAJRjGE0Gj/99NO1a9eOHz/+tddey5KdTO/BEQL9xxBIqzq4OzTpdKpVyJuLZJWSSz5zXxlh3LPJK/6U0mzLv4QO1fCdO3ee2G/qdDrqN5cuXUpt4+DBg+m4cvSkcjl9HPM6P+4NJyYmfvXVV3379p00aZJzobe395IlS+jInD17dosWLRz1c+3aNX9//8x3C9JJl8Ncy1SxdMTm8Bxeu90+cOBAZzaHdOzYce7cubRwy5YtXbp0ybwhJuN7qaCgIGcOjs6gtLS0pKSkgICAy5cvL1682BHVOP+K3u177723bt06PLYcCR2Qtzlz5uzcuVN2gSm1gF5azptnF+0XrIJEDakkpXc8RTy9nngHL8/zBg+P27duThk7ZO+ubf/35Xd6vcF12jIKWb7//vvY2Nj169c7opk1a9YkJydXrly5Q4cOWQpbLJZatWoNHz7cOR0dtf4vvvhiAe+DRvPhBx+ykccljOEEV0INHQVhT/wmyjHxRHR09Lhx4zZs2PDbb7/lPIMbFCoUMX/44YcHDhzAGHVwKRQCeXk9VQhE7duNGzcGDBiwdetWusYzGAyusxduEQKpF8z+P/bucUaRN00EfaSeWgVFvHP3ixkRb/61PHQ4OQ6YJ27UMSFdTEzMtGnTtm3btnDhQj8/P1mM02EezMT0uHPn6tWrdL706dPnyJEjmS8W6IyrVKnSnj17nENgOnfuTEcjlezatWuZMmWCgoIoeMjhCivn7TqTPlmWdOzYMSQkZOPGjZkTOs5i9K6ynaB679699OYHDhyYZbnNZsPwHCR0QPZat25Nba6LP/sgmzONY3ZdN99PFJpUNBTzUAqipFDwMTFRRw/soR+e+Odmk4nnFd1e7ddv8Ci1WuNSk/NXq1aNwpEtW7Zs2rRpypQpqamp1DVSc9+2bdtHp/q2Wq2BgYEUlrnWx2OzdezUsZT0gp1V4hQDF0EhS0JCwq5duyimeWJsajab6aR75ZVXxo8fn8Ns+lAIUfhL8XT58uUd0y4AuAK6aKSrSmrfnmbAtSk9BOJff/31MWPGuFr45x4hULM27QOFqnkVAik4dv/11JhEW8uKGn8PhV3M1+MqMTHxwIEDT9lv0n/bt28/cuRILy8vtxn0ERkZSfXw008/LVu2LHPyhSrE8Wjm5ORkR0Jn0KBBKSkpixcvpqNXq9VSAVr+8ssvDxs2LPPMxM/k0XSPp6dn0aJFw8LCnlg+889xcXElSpQoXrz4E9cPDBI6IDvUnVN4Ksc5dJovjL55xjhwQrkWFQ1pVkmnY/fvOrB/5zatjs+xn6UAwFr7xf8NGTOpWeuXWY41m8yZmzO7KDGiJBZc+0bdRu/evXfs2HH+/PmzZ8/eu3fvxo0b1DU+OhegsztxqY/GLkiM0Tz5/bcbl9Hg/AKXQqdS06ZNqcXL4RszepWi0ho1akyaNKl79+4YhQFZWCyWqVOnoh7A1Rw/fnzLli05J3SsGRo2bDh58uRsn3iV3oMjBPqPIZDZMnjyxFaVi6Tl0WQ3FPF2Wngz7EzyiAkBbStq0vJ3Dp1z585169bN8azux+613U4NY5UqVUaOHNm5c2f6K6PR6DaZAm9vb4oKPv3002bNmmVJhXAZnE9eo5/Hjx8/YsSI8PDwu3fv3rp16+TJk/Pmzdu1a9eGDRtyeJTzM6FT2GQyPescf3RmJSUlpaamFitWDK3lEyGhAzJDrTA1DbK7aFEyrCTYGNFmT0/Q2GxW0cqrcx7bSb2+2WQsGVy635Ax3Xq/7untYTRapUfG5vgZeEaj8NIV5D1oFGaFhIRQEPPrr7/Gx8dTN0m9SO3atWXx0fh7KqkCDSqk/MHlOO6TfxxRFCkGDQgIGD58OEWlzoeMAjx6IOU8WQmAq7VvFAJR+1amTJk333yzf//+jxtf5ujBEQLlWoCXklFxel4yW+gDyZuxNFaGyxTxctZ8TOjQ1cET+02TyVSsWDE6qAYMGODn52fMIK9zR8rwuG96ypUr5+/vf+DAgV69ej3N2rRabeUM9PPgwYNfeumlPn36XLhwgX54tPYcKaEc1vboHPxnz569evXqsGHDnmkfa9asSWfTnj17qBHIvJyaAnxx9SgkdNyW2Ww+ffr0tWvXqKdxp+ymoxWT4dt+8L9/PXbcIC03GY0GD48efUb1Hz4upHSwyWxPS83mqZxWuzSljf+Ql4rWCtIV4N7RAda+ffsFCxasWLHC0dr27t1bLtcPs3sG9WvgWzNQi0YDXLC5e9xyCkApCHvjjTcmTZqUeQJCuXCp+0bzlgve3o8x6iCv9i0tLc3T03PQoEHjx4/PPGPr43pwhEC5D4F6BLWpWqSyv9pkFfLyk3044nWFa4T00Npkok+nV69eo0ePrlSpktVqTU1NleO5Q0cXdTQxMTHZvhoYGEj7uGTJko4dO7Zu3dq5PCUl5ejRo02bNnUOi7t69SqtJ0sIQaEFkzH52qNrpoVJSUkWi+Vxb4xl2UOHDnXv3t25JDk5efr06b6+vs8683ejRo1eeuml999/v0GDBvRhOZfT+ulTwzQ6WSCh47Y2btzYv39/lUq1b98+DFeTEYvZTD1hi7Ydh4yeULt+fbtNSs0uleNgF6VgX1WLSgX/zTw13z/88AMFYXa7vWTJkm3atMn2Es7BpSo82EdF/3DggWyaCIuFzrJmzZpNnjw5y4BqWdi1a9fu3btpF9wyIKP2ja4/e/bsiW4XIBfokpvJmKt10qRJTzNbsIv04PINgUr5qLrX8opOtnNuPejBarXSR9OgQYMxY8Y4+k36sOS7O9TLVKlSZcmSJY6RNUaj8dixY+XLl6cTx1Hggw8+uHz5crdu3SZOnNi6dWu6GAwLC5s/f/6lS5d27txZvXp1JiPDNWPGjK1bt1KdtGzZMjAwMDEx8eDBgx999FGvXr2qVav26HZfeumluXPnTp06dfDgwXq9Pjw8/Nq1a8OGDfP19XUU0Gg0K1euvHv37quvvkorvHHjxpw5cy5cuPDLL784J+XJMrNy5pOCFjrvSaT109+2b9++bdu21BrUqVMnOTn577//3rt3r1KpxLcUWSCh486NF8X9Xl5ejw5+A9dkt9ksFnPlajWHjJnYpkMXpYo3GS1PbLNsgmSyilpVAV8a1a5du1GjRtSj8DzfoUOHbL9S02q11EDLbkJrAFdpIux2itsqVqw4efLkPn36yDEhEhMTQ4EdRY3UULhlQEYfyunTpz09Pfv164cjFuDpOaYDq1Wr1pQpUzI/DUcWZB0CpVlENz6uqN+k46pMmTKjR4/u1q0bfQRuMF2OTqebP3/+uHHjRo4cSXvkGJc0d+5cZwFvb+9Vq1Z99NFHixYtWrBggUKhSJ+Os3bt3377zXFrFZMxmuadd96hP//++++pGF0tOiYe6t+//4wZM7I9ULt27frJJ598/fXXGzduVCqVJpOpQYMGVLGZrz3p/L1y5cqoUaPoV6rqKlWq/Pnnn61atXKWoTdD54LzfjH62bmt9Kf6GgzO2KZevXqbN2+mNzN9+nQqRsubNGkyZ86c4cOHy+5hx88bEjr/EATh7t27dCQ5WmGLxSKKIv366JjJqKgoKunl5UWtQ5a7+Og4pvXQAee41zcsLCw+Pr5cuXLO2aeyoK1QGTofSpcuTSvM/BJt3TGkzTHyLSIigrZbrVo1x6+OApGRkdHR0bSkVKlSmR/iSCekLQO9f3qHdDo5HoBC7yrzBQAVoK0nJycHBQX5+/tneW9PfAOQh0RRMBmNxQMC+w4a2avfYJ+iXiaj1WQ0P9U5zLEFns1hHmTl09LS6JDL9oCnroIK0FGHJ60APHsTkT5dTtGiRSmAGzNmjHyfSk79He0LNRdPvA9fjhxRNfWSMh3GD1BQETi1bxSL0pXhsGHD6GJVdrsg6xCIYshUd8zpOO5N9vb2Hjp06KBBg+gAow5I1gNzMqtRo8aOHTtOnz5NV2cUEtDFZpbAoEiRIrNnz54yZcq5c+foFAsJCSlfvnyW69bq1at///33dK16/fp1uqKkP6lUqdKjD5bKnIt55513+vfvf+HCBfo1ODiYVpv5kKYN0RUlRSlTp069c+cOnQu00SzJlzp16oSHhztnXP7ll1+cBbp27dqqVavMj4erW7fupk2bbty4ERsbS2+MNkcLjx49qtfr0XIioZM1UKaj+ddffw0LC6P4slatWnQgLlq0aP/+/UOGDPn444+dJenwnTVr1p49e5KSkqhpfuGFFyZNmpR5XCX1Q5s3b6bDcdq0aRR2Hzx4kM4cPz8/WuHIkSMf3eiPP/548+ZNu91OZbp16zZ58mTnQXzixImePXvSn69fv/7w4cP/93//FxcX9/PPP/fo0YPOzA0bNoSGhl69etVsNiuVSl9fX/pzOmkdaZ3FixdTeVpOv1osFno/tF/UqNGq6tWr51j/0qVLaet0AlPvQsUaNGjgGM/mfIc5vAEcM3nb35iMaVqdvkffgYNHTihXqZzZJKSlmp/yzxUcG5VsC4+3tnKBu670GR73Kh1LeTVhft66n2K/HG1uUs6AoxFcNglCPQ61vW+//XbVqlVlvS9sBup3SpUqRd2iO33JRvty/Pjx5cuXMy45jQ6Aa4ZAdIFNkcPgwYMnTpxYunRp+fbg8g2B9lxLqRWkE91ryKSj3+zUqdObb75J12vynS4np2t4nn/ibYnFihVr2bJlzmXo2tN5efg0AjM87lXHpNQ5lKHr08y3JGce0KDJ8OiflM3g/JWumtF4IqGT9bCbMmXK/PnzmYxcplqt3r59+/79+7VabUxMTGJiorPkkSNH+vXrd/369RIlStSuXfvOnTuhoaHHjh37+uuv+/fv7ygTFxd3//59Culee+212NjY8uXLX7t2LSwsbMKECXTWDR061FHMbrdPnjx53rx5tJBaGTp2z549+/nnn586dernn392HOXU9Ny9e1en061cuXLhwoXUDRQtWtQxZGbfvn3vvPMOvUN6J0FBQffu3aN39cknn0RFRS1YsIDOE1otlRcEgbpJCisNBgM1arTcETrTLtNVAZWkArQGOitu3769YsUKWu3333/frl07x5vM4Q1AHl3YOJ6baG7RpsOwcZPrNWoiCkxqivmZVqLm2ZlbozefTDj+YdUXMK1vrkxafeeP/bEnPkIFgsuhVppiUIq0qNF++eWX3ekqjnpbOc7lnDPqNN14smeAPI/A6aq7c+fOFIc3atQIPXhBhUC/7Yv9a3y5aoFai80dcjqOy59atWqNGzeuTZs2LMtiyCS4vcL+JdLy5cu//fZblUrVvXv3TZs2nTlzZt++fV26dKGTn8JN55eHiYmJo0ePvn79evv27UNDQzdv3rx79+4xY8ZQV0Rx9vnz5x3FeJ7XaDQRERF9+/Y9derUzp0716xZExgYSMGrY7I0R7Eff/xx3rx5Pj4+8+fPp/XQCleuXFmpUqWtW7c6BwRRA0Tvila4YsWKmTNnnjhxglbYtm1beqlHjx4zZsz4+++/jx07RpvYu3dvt27dtFot7cu5c+eowIABA44ePTp16lTaIq3kp59+ojLHjx+vWbOmY5cXLFhAa6Y9ouUHDhygVdWvXz86OvrNN9+kePSJbwDyhN0m+Pj6fjznu/nLVtdv1MRsslgs5lys506C1ZZij0mxoUpz52aMxZ5iQwWCC/Lw8Jg9ezb1OO6UzXGgbtFut7tbq+52ewTw/Pj5+VFsvH79+lxnc9CD50kIJBrtcWmCwi0eBS2Kol6vf//993///fcOHTo4JmbCp5w/HPMZ5/zYeHhOCnVCx2QyLVq0iI6/Zs2aLVu2rH79+tS71KpV69tvv61QoULm0SgbNmw4ffp0mTJlFi9eXKVKFaVS6e/v/80337Ro0SI6Ovrnn392lqSGo27duqNHj3bMfNakSZMBAwZQ5ErFoqKimIwJomhbtGTIkCFDhw51FGvbtu2cOXMMBsO6devCwsIyr23s2LFUzNvb29fX13F7ZLFixT744IOWLVvSQp1OFxwc/N5779F66A1fvXqVybhTl37VarWOSb9otVSMligUCtq6Y5c7duw4d+7ckJAQumBo3Lgx9amO2ch/++23zFWU7RuAPGG12spXqtp30DA2/YY4c65naOMVLKNgFe79fILnSYkKBFdFzTv1FJi5DADcD4XTgwYNYv9bHgE9eB6EQBzrNvXnuJ+X+k266klNTcWQyfxUvHjx3r17u9/YW1ko1Ldc3bhx49q1azzPDx48OMs9e/Rr5gvsQ4cO0X+LFi164sSJI0eO/FN3PF+sWDGO444fPy4IgnM4T5anStGR7ZgywGq1MhkzJYeHh+t0OtrE+vXrHW0NFUhOTqb1R0REnDt3LvNdxNl+cUGbo41SYdo6Rfy0Kor4k5KSMrdczp+dT4BzbJ32mt75a6+9lqVbbdy48a+//rp3794pU6Zkfum/fHMCOaPP6ClnPgYAAAAAgBw45kJGPeS/ChUqOGaRg/xXqBM6SUlJKSkpHMeVLFkyy2V2luESkZGRarX61q1bgwYNypwfUSqVHh4e9gzOhE6Wv3WmbBzfQiRl0Ov1CxcutNlszsKOW5wefTqGIw2U2YkTJyZMmHDq1Cl6if6E3lhAQACtinbkiV900KaTk5PprT76SEVaCa0hMTHRsdoc3gAAAMBzYjKZtm3bRn1r8+bNs3Rqp0+fvnLlStOmTbM8mZG6ttDQUFrYqFGjLH9y/PjxGzdutGnTxjVnJAUAAAD4Lwp1QscrQ3x8fGRkZOblzuSLU0BAgNlsrl279vz58zPfJE/FJEnS6XSPPt38cTwzUPQ5c+bMxo0bZ77VkOM4QRBynuSf3u3w4cNPnDjRunXrIUOGUPwaFRW1adOmDRs2PM2wVcfWaSUxMTFZXoqNjRVFkWLop98XcAU2QWJsbvZ0gnxltaMCAVwIdWfLli1zPMCxRo0azuXUbS1YsOD27dthYWFvv/125i5v5cqVa9eupf4rKCjI8VhTh/Dw8NmzZycmJsbFxY0aNQp1C4AeHB6qQMSQAPJXqBM6wcHBJUuWpBjxp59+6tChA8//UxsKhcJms2UOFuvWrbtkyRIKDemlzPFlrjcaHR198eLF0aNHP+ufX7p06fTp07SSxYsXO8PWxo0b79ixI8vQHufYn8zDbRxbv3///urVq2mXncspPt67dy/HcQ0bNmRZ3IosG6LEdHrBs4iaq1oCs2zkUr//+agULCoQwEXExv4/e3cCH0V5P358jr03N0K471MQlENQVAQ5i6IFRK3yt/pDrfqv1gNr//RXryregCJVq6KigiBSUYqcSqGCHAJyCigQjoQz52bPmfk/2dElbkIIAZJM8nnX5rXMPjs7893j+c53n3nmqDkHXPELTUrRkTuhUCgxMfH48eOapsW6bCEzM9Pr9UYikbiR9uKf4iEJCQlinQQWoAdHiQDW0SJ6u3RXUWkMgDXV6kmRRZI3ZswYRVEWLFhw7733btmyJRAI7Nq1a+zYsdu3by9eB7n22mu7du168ODB22+/fdWqVSKV1HV9586d48aN+/7770/3Se+44w5VVadNm/bEE0+IxFSkreJ5P/jgg1deeeWU18gwz7ESee2ePXtiCzdu3Chy1rhCjLn9+fn55gYXFBQEg0Hx7LfddpvY5dmzZ5vPLu7avHnznXfeuXfv3iZNmtx88818KiwkENZv6Vln3h/b1Eu0EY2KubtP3cUPtSWAQDVhnr8sejTRVRVfHlsSO8E57iElzzsu4yEA6MFx9xXnffyHVmleW0SnoANYVW3/Bvz973+/cuXK999/f+rUqfPmzUtMTDxy5IjI/1JTU4ufh5WWlvbSSy+NHj167dq111xzTadOnUSbnTt37tu3b/HixV988UXdunWlX6bLiZtT3TAMLSq25LbbbluzZo14xqeffvqTTz5p3LixeNLNmzcHg0G3233HHXfEHiWVmJHn/PPP79Onz/z588eMGTNy5MiGDRt+8803K1asMKfjKd64S5cuYi/y8/MffPDBKVOmmDWj9u3b33777eLZ33vvvfHjx8+aNatOnTpiRw4dOiQaP/fccy1btiy+2SU3ANWNbhhFFynAmRxAEj8AAOjBax+HKvtDOhcKA6xLqeX7b7fb33jjjRdffPH8888PBoPZ2dm9e/f++OOPW7RoETcZ8GWXXfbZZ5/dcMMNqqquXr165cqV4XB45MiRzz77bGyqRdcvij/QZrN5vV6PxxP75VCsYcqUKRMnTuzQocPevXu//vrrHTt2tGvXTqzq2muvjbXxRsX9riiWTJ48edSoUbm5uWINY8eOPXjw4KOPPlq/fn3xvMWHoLdp0+bxxx9PT0/3+/3r1q3LzMw0N8DhcLz++uvjx48XDfbt27d27Vqxp/37958xY4bYuxMd5Ek2ANWOIXH2MwCca6LHFF2/6HwJBYAagxwSsDrGKBbVdP70pz+NGTPm2LFjDoejQYMGYuETTzwhlRic0rlz5+nTp//0008//vijFL08W7NmzYo3eOONNyZNmhRX0Bk2bFifPn3MUT+xhaqq3nPPPbfccsv27dsPHz5cv3799u3bJyQkxBp069Zt69atUnRwUNwGt2zZ8uOPP961a1d2drbb7RYPtNlsN9xwg67rycnJxVveddddv/3tbzds2CDLstjU2Ogbsctjx4698847xbOL3LRp06Zt2rSJK9yUsQGoXp9hVVb5YQUAzqUtW7a89NJLOTk5rVu3/stf/sI1swDUDKpclEYyHh+w8MEgIRBfYbIsJ0SZS/ZHiYUlr+0tRespscpInJSUlJILS47ZiUlKSrr44otLvctut6enp5ex2SKnLP5P85yvkurVqzdw4MBS70pOTu7Zs+fJ1n/KDUB14LTLn6zLWflTwT9HN0/1MJaqIqavOT5nfc4btzQjgABOZsWKFcePHxd5wrZt27Zs2XLZZZcRE4Ae3OpmrM1+/5ujT1/XKMmtakyjA1iTQghmzZo1dOjQDz/8cMOGDT/99NPChQvvv//+AwcOJCcn9+vXj/igOlNl+aM1x2cvPrxxfyHRqJgpXx2ZtTCLAAIoQ/PmzQ3DKCgoSEhIqF+/PgEB6MFrgNe+Ojx/+dEtmX6njbHegFXV9hE6mqbNmDHj31FpaWlOpzM7OzsQCKSmpj722GM9evTgLYJqruh8K7vCryoEEMC5079//2AwuGvXrksvvTRuhCwAenCrBlAmgIDl1faCjqIoL7/88tChQ//73/9mZmYWFBSkpqa2aNFi+PDhffr04f2B6k8u9hcVCaBMAAGc6rBHVYcNG0YcAHpwAgigWqntBR1Zlps3b/4/UZqmhcNhp9MZuxwVAAAAAABANcSkyCeoUcQB1sJAWQII1PZPMddnAejBUZEvT2IAWB4FHcDC5KJ5oAwpqBOKCosQQKA60TRN13XDMMTfXx94GOZdkUik5KP0X8QtFI0VRSn1IQDowWt7AHVDChFAwNoo6AAWFtKMe66se7BLykVNPESjYv52dYN1nZIJIFBNXHTRRStWrEhISGjRokXx5XXq1GnZsuWmTZtEA5vtV9lLz549xfL09PR69eoVX96wYcM2bdpkZGR07dqVwAL04Ijz2DUNFrfydqjvDkYYqwNYFQUdwMJCmnFV+6TmdRyEosIGnp8k/iMOQDXRq1evpk2but3u1NTU4su9Xu/YsWOPHj3arFmzuIcMGDCgffv2ycnJSUm/+iybF6zMyclp3LgxgQXowRH/5dkhqWcLb1ZuWNMp6ABWRUEHsDBZkgJh3R/S3Q6FaACoGRo2bFjqcm9UqXc1adKk1OUJUYQUAEqV5y8q5ihcDwawLA4CAWuzqzLVHAAAAJwuj4NiDmBtHAcCFqYq8k9Hg198n8tY2Qr76Uhw4dY8AggAAD147Qrg0eD8zbmaIckUdQDLoqADWJjTJo//MuuaF35Yl1FINCrmTzP3DXpm27q9BBCoxORDUeImNq4B7HY7ryxAD26lAH68/5bJP27N9LtsHBICVsUcOoC15fk1Kazz61SF5Qd0EcACLtsJVBZFUQoKClauXKmqak3ar+3bt4s90jSNlxioHNmF0RSIQFQ8BSoKYGFIZ4QOYF0UdACLHxqJTtgmf7klL+NYKM2r9mufFDsZ+rgvMnNtdjBsnBiKpxkXNPX0a5cYe3ipbS5vl9i16YmLgH6XUbj8h3xJ/WW9uuS0y6O6p6Z5T3yBLP0hf1NG4blok+RRf3dxmtP285JgxPho9fE8kcP9eqf6tk2MpSPHfJFZYqcihiSftM3eY6Fvd/sURTpSEJFsCqkMUAkMw9B13W63Hz16dOLEibIsiyU1Y9fkKLFrmqbpHGAClUItSoGUWArUt12i+ksOVJ5MoNQ2VkyBTpnXxbX5dQokkwIBFHQAVNEhhDhAEv/TpSc+3idFr1Kw9K8dLm3pDeuGXZGfnp/18gcZkiqdODc6orubeNaN69A8zaEZJ2kT0AYMSP/83lZhrehAy67Kj845sGjRIcmlxo7JJE3aeUvTZ65tKJ5IpFN7joeunrzLv69Qig3ZPVttxE7Z5VZ/73Rxc29EN2yKvHqP7/ZJO6SQIbnVoqQnoElB3dXUvf3JTs3Sfr58+4sLDz377p6iazbEcpSIEdfmDx/u/XLZUcmlFK3EOJE+ATh33G633W7Pyckxz7eqMdWcWE2n6Bs0EIi7ejqAc0QX/bdmPDEjQ9ySFGnVU516tvCWPxM40cbMKIKaVGiFFChc7KpU5cnrSrS584O9C1cclZyKmf0wKzJAQQdA1RBJwJje59VzqxFZNnQj1Wtz2ZUDOWGRiIgsZEjHpLzhjUIR/USnrhkdm7hF970vOyRyiZO1uaJ9YmZOuOg3q+g0PTd0S23gtZ2oeRiGw6aIB5pPJB4n7nn86gZb9vnPfhvdSPSoXodyIDtsZjPi9r3XNfIH9Xlb8g4dDY7oX69Ror1bS2+j5BOzV9xx+XmabhT9PFXsN7e4Nrf0rONVZcMmiyywaR1Hl8Ye3k7AuVa3bt3f//73a9asqWEnW504vNT1xMTEIUOG8FoDlWDswPoNvbaIIuu6cV6Crfl5ztPKBGJtPl2fs/9wYGD38xon2i5tW91ToPyiETqnl9cVb+O0y/07JMqaYahFKVCDVHuH+m5zfwFYkZyVlVX5z2oYRlpamsPh4AXA6crOzg4Gg5YbHup1yIPeOPzNpsJp97W6sm1i4dmbscVlV0QnbEQn0VFVORQxRK8fHblT1K97465GKUsib/AFf372k7UJhA3/LydUi77f7VBc9qJhLCc+wpLkC+lFKUhsB52KXT0HbeSiH6gKAppmmMORivKcBJea4FQGTdr1zfqcdc9dUHxoNICTfWfS8/K6AyjVwIk7F317fM6f2/bvkHTcp1XzFEgx/3E6eV1cG7dd0c0BkoZkU+VgxDiLVwrzOJQRb/y0elPep/fVH9DW5QtZrFTEdyYsd5TKCB3A2gLhn9MOOTpgx/jltyjxN6IZuf6ypucso03su0guqu/ogXDpD4+JJQrntI0cHYCc59fEZkf0ol3NCzD/KAAAqLhwtGRSENRzCrVYWlVtU6CK5XXF2/wqddQMBucAlkZBB7C8X35lAQAAAEgdgdpCIQQAAAAAAADWQkEHAAAAAADAYijoAAAAAAAAWAxz6AAW/wwrstNeNLWdXHRhyqKJ7mKz26mK7HEocVOthyOGP3xi1r1S2wTDeiDy82UXxMpcNvEUvyr+iqcoDOnFr4ngtit2m3yO2hQET0zZJzY1wVl0lSux42LjElwq7wEAAFDxVCp6bSmvQ0l2qyInqeYpUAXyurg2dlV22H5JHXWp+F0ArPcNRggA61IVKSsv/F1GoejsRUqQ4lG7N/PYFNmI3nW0ILJwa144op+4ZpVmtGng6tXSq+k/P7zUNhc191zQyBOJJhlibWL96/cUFl0t85f8wm5TBp6flOZVY+v5ekf+zszA2W+jGwludVDHpOglNiVFLsp+5qzPCYaNAzkhyalMW3ls1Y6CTk3dfdokxvbgmC8y+7vsUNg4cfUITYprk3E89O1un0h5RKLUMNl+WesE3k4AAFjIobzwil2+aOZinOe19WmboP5ywe7yZAKxNnuPFWUU/9qQs3m/v1NjdzVPgQr8mqScXl4X12bPsdCmA35xv65L9ZJs3Zp6eC8BFHQAVAGnTRn/ZdYX3x4v+hVJE7299O9H2/dq4Q3rhkNVXv3qyKvT90lqsYuQR3RnY8/KP7drmubQTtYmoPW9qt6cP7QKRnTzKV79+shXSw5LsbEwhiGyoiM3NXnymoYhTRfJU8bx0B0fZAT3F4rc5yy3ESmMQ77wbx17NPeGNd2uKmv2+P48dbcUNCSPKpKeVz7ZLwV1dzPPtic6NktzmA96ceGhZ9/dU5TuxNK4iBHX5q4PM75cdkQkcJJNdrjVb8d1uLAJCQ0AAJbxwMz900VXHu3lRSaz6qlOPVt4y58JnGjjVkUy8P78LKnQCilQyDhR0ClPXleizV0fZHy18pjkUCS7Yncps+5udVETT4BxOgAFHQCV72BOWPy9rHNyeqItxWPr3tyb6v35c/2nq+o5FDlY/FeaiNG9lbdzY0/s559S2wy9KCVZJDfSz+nLIwPrd6zrkmwnflYSKc49feumeH5uI573jZubrv3Rd/bb6EaK13ZJq4REp2K2Ebf/elOzHF+kWDZjdGvlbZhsj8VkzGXnhSNG3E7FtfldjzSPLCkO5asf8o9lBY4XaryXAACwkIzjIcmQLusSTYHcavM6jtPKBEptY7kUqDx5XVyb/+l9XqpD+TkFOhzI9WuKzLsJsCo5Kyur8p/VMIy0tDSHw8ELgNOVnZ0dDAZl2WI9j9chD3rj8DebCqfd1+rKtomFobPzM4jHoYx446fV3+eueKpj71acNFQR/V7e8dWa41890VG8LkQDNfg7k56X1x2oYfq+tOPrtcdX/L0TKVDFU6C12dPub332U9NNeZ/eV39AW5cvZFgrJnxnwnJHqVzlCrAw8YURihhSQA9rBtGomEBYBPDEjIMAAMASgkUpkEYKdEYpUFAnBQIsjVOuAAuL6MZNPVI7N3R1bOAmGhVzd5+67dKdnRoSQAAArNeDkwJV2L1X1m2UbGtTz1n06yAAa6KgA1hYMGJc3z31kUH1CUWFje6VJv4jDgAA0IPXKjf3TBvSKemYT4voFHQAq+KUK8DagmGDCxMAAADgdPnDukY1B7AyCjqAtamK7LLxQQZgbYZhHDp0aO/eveKvrp+FIvWcOXOGDx8+e/bss7J5+fn5n3322ZNPPvnjjz/yYgGoMZzkkIDFccoVYGGqIh3Jj2TlhS9vzfUdKuiYL7LrSKhncw+hAKrE4cOHp06dOn/+/P379+u6rihKvXr1unbtet111/Xv379i6zx+/Pi4ceO2bdu2adOmyy+/XKyw+L3hcNhut5/WCjdv3jxixAhN0/r27duqVSteNYAevAY47tO++ang/PpuJkYGrIuiLGBhTpvywsKsgS/8sPmgn2hUzNhP9vd5ZhsBBKrE3r17hw8f/uijjy5fvvzYsWMFBQVHjx5ds2bNa6+9NmLEiKFDh65fv74i341OZ4cOHRRFad26tcvlMhdqmjZlypSBAwc+/fTTp7tCXdftdrvH41FVlVcNoAevGR6evX/kK7t2Hg44bTLRACyKgg5gbbuPhQI54UN5YUJRMT8cCgZzQgQQqHyhUOiRRx5ZuXJlo0aNHn/88SVLlmzYsGHBggWvvPLKoEGDwuHw0qVLs7OzK7Bmr9f7z3/+81//+te0adOSkpLMhZFI5O233160aNHRo0dPd4WyLCsKKRNAD16zApgZCOdHDudHbAoFHcCqOOUKsDa7KkuqrNITV5SDAAJV5Kefflq2bJndbv/LX/5y7733mgsbNmzYs2fPO+6449133/X5fP369avYytPS0q655priS5xOZ1JSkizLHg8naAD04JAcNjOAEidcAdZFQQcAAFSBY8eO5eXlqaravXv3+OzEZhszZkzsn4sXL96xY0eHDh369u1rLjl06NCcOXNSUlKuvfZat9stRQfgfP7555mZmaKNaDl//vzdu3e3aNFiyJAhfr9/7ty52dnZR48eFY03b978zjvviPZNmjQR98aeJRwOL1iwYM2aNTk5OeKunj17Xn755XEb5nK5CgsLZ8yYsXHjxsTERPHw3r1781ICAIAqQUEHAABUgbS0tKSkpPz8/Ndee61x48aNGjU6Wctly5b9/e9/79mz53/+8x+HwyGWfPrpp/fcc4+qqsuXL7/kkkvEkgMHDtx1111Hjhz5+uuvO3To8PLLLy9evLh///5DhgzJzc29//77Dx06lJKSkpiYKFYyf/588ZDLLrssVtDZunXr2LFjly5dGggEzCXJycmDBg168skn27VrZy6x2+1btmx56KGHxFNI0fOwxJY//vjjYuW8mgAAoPJR0AGsLawZUsTQdEbLVlAoQgCBqtG6det+/frNmjVrzpw53377befOnTt27NiqVasWLVq0adMmPT091nLw4METJ048ePBgRkaGeJQULfF4PB5d18UNs6CzadOm48ePd+/evWvXruKfCQkJxf+OHz8+Ozv7nXfe2bNnT+/evYcNGxYKhZo3b26uX6z5pptu2rJlS0pKirhLLBdPtGjRopkzZ4otLF7QeeKJJ6644opbb731wIED7733nnigWHLppZf26NGDFxSgB7deADVDI36AlVHQASxMdMEtz3MeTHfWS7QTjYrp0MD1Y30XAQQqn91unzBhgrixYMGCPXv27Nix45NPPlEUJS2qX79+Dz74YJs2bYo+px06tGrVavPmzRs2bGjdunVmZqa4IR6u6/rXX3/98MMP22y2lStXaprWtWvXxMTEuCdKSEi47bbbxI25c+du3bq1c+fOsSl7TOPHj9+yZUvdunVfffXVkSNHmgs/++yz3bt333nnnbFmfr//z3/+s3g6858XXnjhrbfemp+fv2TJEgo6AD249QLY0PVDhrOOV9V1ggFYFQUdwMICYf1vQxukjWrSOJVspoJe+13T8SMa1fXyZQhUgfT09I8++mj9+vXffPPNzp07f/zxxz179uzfv1/8feutt5YtWzZr1qyOHTumpaV16dJl48aNq1atGjly5Lp163bt2nXdddcdPHhww4YNGRkZLVu2XLNmjRQ9i+pkzxUMBnVdl2U5HP7VNXGysrIWLVqkKMqoUaNi1Rzh2muvjVuDYRhXXnll7J9XXXVV69at165dK9bASwnQg1svgDc1/WO/ei6bHIhQ0QGsim9AwMIMQ3I7lAZJfJArzmmT69oIIFCVLooSNzRNy83N3blz57Rp02bMmLFjx44XX3xx6tSp4q7LL7/8/fffX7dunbi9fPly0XL06NErVqxYuXLld999l5ycLBrXq1evAiNl9u/ff/jwYZvNdvXVV5+ycSgUit1WFMXpdBoGpysA9OBWDWD9RFt2oSZzoTDAshRCAFiaphthzh4HUCOoqpqWltazZ8/Jkydfcsklsixv2rSpoKBA3CX+Wbdu3d27d2/ZsuXbb7+tV69er169zPE4S5cu3bBhw759+9q3b9+yZcvT/haNkqLXNT+tBxpRvGoArCtCDglY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" alt="DPDK test environment" />
</figure>

- **Traffic generator**: An application that can generate high-volume packet traffic.

- **SR-IOV-supporting NIC**: A network interface controller (NIC) compatible with SR-IOV. The card runs several virtual functions on a physical interface.

- **Physical Function (PF)**: A PCI Express (PCIe) function of a network adapter that supports the SR-IOV interface.

- **Virtual Function (VF)**: A lightweight PCIe function on a network adapter that supports SR-IOV. The VF is associated with the PCIe PF on the network adapter. The VF represents a virtualized instance of the network adapter.

- **Switch**: A network switch. Nodes can also be connected back-to-back.

- **`testpmd`**: An example application included with DPDK. The `testpmd` application can be used to test the DPDK in a packet-forwarding mode. The `testpmd` application is also an example of how to build a fully-fledged application using the DPDK Software Development Kit (SDK).

- **worker 0** and **worker 1**: OpenShift Container Platform nodes.

# Using SR-IOV and the Node Tuning Operator to achieve a DPDK line rate

You can use the Node Tuning Operator to configure isolated CPUs, hugepages, and a topology scheduler. You can then use the Node Tuning Operator with Single Root I/O Virtualization (SR-IOV) to achieve a specific Data Plane Development Kit (DPDK) line rate.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have installed the SR-IOV Network Operator.

- You have logged in as a user with `cluster-admin` privileges.

- You have deployed a standalone Node Tuning Operator.

  > [!NOTE]
  > In previous versions of OpenShift Container Platform, the Performance Addon Operator was used to implement automatic tuning to achieve low latency performance for OpenShift applications. In OpenShift Container Platform 4.11 and later, this functionality is part of the Node Tuning Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `PerformanceProfile` object based on the following example:

    ``` yaml
    apiVersion: performance.openshift.io/v2
    kind: PerformanceProfile
    metadata:
      name: performance
    spec:
      globallyDisableIrqLoadBalancing: true
      cpu:
        isolated: 21-51,73-103
        reserved: 0-20,52-72
      hugepages:
        defaultHugepagesSize: 1G
        pages:
          - count: 32
            size: 1G
      net:
        userLevelNetworking: true
      numa:
        topologyPolicy: "single-numa-node"
      nodeSelector:
        node-role.kubernetes.io/worker-cnf: ""
    ```

    where:

    `metadata.name`
    Specifies the name of the performance profile.

    `spec.cpu.isolated`
    Specifies the CPUs that are isolated for the application workloads. If Hyper-Threading is enabled on the system, allocate the relevant symbolic links to the `isolated` and `reserved` CPU groups. If the system has multiple non-uniform memory access (NUMA) nodes, allocate CPUs from both NUMAs to both groups. You can also use the Performance Profile Creator for this task. For more information, see *Creating a performance profile*.

    `spec.cpu.reserved`
    Specifies the CPUs that are reserved for the operating system and Kubernetes system daemons. You can also specify a list of devices that will have their queues set to the reserved CPU count. For more information, see *Reducing NIC queues using the Node Tuning Operator*.

    `spec.hugepages.defaultHugepagesSize`
    Specifies the default size of hugepages.

    `spec.hugepages.pages`
    Specifies the number and size of hugepages to allocate. You can specify the NUMA configuration for the hugepages. By default, the system allocates an even number to every NUMA node on the system.

    `spec.net.userLevelNetworking`
    Specifies whether to enable user-level networking. Set to `true` for DPDK workloads.

    `spec.numa.topologyPolicy`
    Specifies the NUMA topology policy. Set to `single-numa-node` to ensure that all resources are allocated from the same NUMA node.

    `spec.nodeSelector`
    Specifies the node selector label for nodes that this performance profile applies to.

2.  Save the `yaml` file as `mlx-dpdk-perfprofile-policy.yaml`.

3.  Apply the performance profile using the following command:

    ``` terminal
    $ oc create -f mlx-dpdk-perfprofile-policy.yaml
    ```

</div>

## DPDK library for use with container applications

An [optional library](https://github.com/openshift/app-netutil), `app-netutil`, provides several API methods for gathering network information about a pod from within a container running within that pod.

This library can assist with integrating SR-IOV virtual functions (VFs) in Data Plane Development Kit (DPDK) mode into the container. The library provides both a Golang API and a C API.

Currently there are three API methods implemented:

`GetCPUInfo()`
This function determines which CPUs are available to the container and returns the list.

`GetHugepages()`
This function determines the amount of huge page memory requested in the `Pod` spec for each container and returns the values.

`GetInterfaces()`
This function determines the set of interfaces in the container and returns the list. The return value includes the interface type and type-specific data for each interface.

The repository for the library includes a sample Dockerfile to build a container image, `dpdk-app-centos`. The container image can run one of the following DPDK sample applications, depending on an environment variable in the pod specification: `l2fwd`, `l3wd` or `testpmd`. The container image provides an example of integrating the `app-netutil` library into the container image itself. The library can also integrate into an init container. The init container can collect the required data and pass the data to an existing DPDK workload.

## Example SR-IOV Network Operator for virtual functions

You can use the Single Root I/O Virtualization (SR-IOV) Network Operator to allocate and configure Virtual Functions (VFs) from SR-IOV-supporting Physical Function NICs on the nodes.

For more information on deploying the Operator, see *Installing the SR-IOV Network Operator*. For more information on configuring an SR-IOV network device, see *Configuring an SR-IOV network device*.

There are some differences between running Data Plane Development Kit (DPDK) workloads on Intel VFs and Mellanox VFs. This section provides object configuration examples for both VF types. The following is an example of an `sriovNetworkNodePolicy` object used to run DPDK applications on Intel NICs:

``` yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: dpdk-nic-1
  namespace: openshift-sriov-network-operator
spec:
  deviceType: vfio-pci
  needVhostNet: true
  nicSelector:
    pfNames: ["ens3f0"]
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
  numVfs: 10
  priority: 99
  resourceName: dpdk_nic_1
---
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: dpdk-nic-1
  namespace: openshift-sriov-network-operator
spec:
  deviceType: vfio-pci
  needVhostNet: true
  nicSelector:
    pfNames: ["ens3f1"]
  nodeSelector:
  node-role.kubernetes.io/worker-cnf: ""
  numVfs: 10
  priority: 99
  resourceName: dpdk_nic_2
```

where:

`spec.deviceType`
For Intel NICs, `deviceType` must be `vfio-pci`.

`spec.needVhostNet`
If kernel communication with DPDK workloads is required, set to `true`. This mounts the `/dev/net/tun` and `/dev/vhost-net` devices into the container so the application can create a tap device and connect the tap device to the DPDK workload.

The following is an example of an `sriovNetworkNodePolicy` object for Mellanox NICs:

``` yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: dpdk-nic-1
  namespace: openshift-sriov-network-operator
spec:
  deviceType: netdevice
  isRdma: true
  nicSelector:
    rootDevices:
      - "0000:5e:00.1"
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
  numVfs: 5
  priority: 99
  resourceName: dpdk_nic_1
---
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: dpdk-nic-2
  namespace: openshift-sriov-network-operator
spec:
  deviceType: netdevice
  isRdma: true
  nicSelector:
    rootDevices:
      - "0000:5e:00.0"
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
  numVfs: 5
  priority: 99
  resourceName: dpdk_nic_2
```

where:

`spec.deviceType`
For Mellanox devices the `deviceType` must be `netdevice`.

`spec.isRdma`
For Mellanox devices `isRdma` must be `true`. Mellanox cards are connected to DPDK applications using Flow Bifurcation. This mechanism splits traffic between Linux user space and kernel space, and can enhance line rate processing capability.

## Example SR-IOV network operator

The following is an example definition of an `sriovNetwork` object. In this case, Intel and Mellanox configurations are identical:

``` yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: dpdk-network-1
  namespace: openshift-sriov-network-operator
spec:
  ipam: '{"type": "host-local","ranges": [[{"subnet": "10.0.1.0/24"}]],"dataDir":
   "/run/my-orchestrator/container-ipam-state-1"}'
  networkNamespace: dpdk-test
  spoofChk: "off"
  trust: "on"
  resourceName: dpdk_nic_1
---
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: dpdk-network-2
  namespace: openshift-sriov-network-operator
spec:
  ipam: '{"type": "host-local","ranges": [[{"subnet": "10.0.2.0/24"}]],"dataDir":
   "/run/my-orchestrator/container-ipam-state-1"}'
  networkNamespace: dpdk-test
  spoofChk: "off"
  trust: "on"
  resourceName: dpdk_nic_2
```

- You can use a different IP Address Management (IPAM) implementation, such as Whereabouts. For more information, see *Dynamic IP address assignment configuration with Whereabouts*.

- You must request the `networkNamespace` where the network attachment definition will be created. You must create the `sriovNetwork` CR under the `openshift-sriov-network-operator` namespace.

- The `resourceName` value must match that of the `resourceName` created under the `sriovNetworkNodePolicy`.

## Example DPDK base workload

The following is an example of a Data Plane Development Kit (DPDK) container:

``` yaml
apiVersion: v1
kind: Namespace
metadata:
  name: dpdk-test
---
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: '[
     {
      "name": "dpdk-network-1",
      "namespace": "dpdk-test"
     },
     {
      "name": "dpdk-network-2",
      "namespace": "dpdk-test"
     }
   ]'
    irq-load-balancing.crio.io: "disable"
    cpu-load-balancing.crio.io: "disable"
    cpu-quota.crio.io: "disable"
  labels:
    app: dpdk
  name: testpmd
  namespace: dpdk-test
spec:
  runtimeClassName: performance-performance
  containers:
    - command:
        - /bin/bash
        - -c
        - sleep INF
      image: registry.redhat.io/openshift4/dpdk-base-rhel8
      imagePullPolicy: Always
      name: dpdk
      resources:
        limits:
          cpu: "16"
          hugepages-1Gi: 8Gi
          memory: 2Gi
        requests:
          cpu: "16"
          hugepages-1Gi: 8Gi
          memory: 2Gi
      securityContext:
        capabilities:
          add:
            - IPC_LOCK
            - SYS_RESOURCE
            - NET_RAW
            - NET_ADMIN
        runAsUser: 0
      volumeMounts:
        - mountPath: /mnt/huge
          name: hugepages
  terminationGracePeriodSeconds: 5
  volumes:
    - emptyDir:
        medium: HugePages
      name: hugepages
```

- Request the SR-IOV networks you need. Resources for the devices are injected automatically.

- Disable the CPU and IRQ load balancing base. See *Disabling interrupt processing for individual pods* for more information.

- Set the `runtimeClass` to `performance-performance`. Do not set the `runtimeClass` to `HostNetwork` or `privileged`.

- Request an equal number of resources for requests and limits to start the pod with `Guaranteed` Quality of Service (QoS).

> [!NOTE]
> Do not start the pod with `SLEEP` and then exec into the pod to start the testpmd or the DPDK workload. This can add additional interrupts as the `exec` process is not pinned to any CPU.

## Example testpmd script

The following is an example script for running `testpmd`:

``` terminal
#!/bin/bash
set -ex
export CPU=$(cat /sys/fs/cgroup/cpuset/cpuset.cpus)
echo ${CPU}

dpdk-testpmd -l ${CPU} -a ${PCIDEVICE_OPENSHIFT_IO_DPDK_NIC_1} -a ${PCIDEVICE_OPENSHIFT_IO_DPDK_NIC_2} -n 4 -- -i --nb-cores=15 --rxd=4096 --txd=4096 --rxq=7 --txq=7 --forward-mode=mac --eth-peer=0,50:00:00:00:00:01 --eth-peer=1,50:00:00:00:00:02
```

This example uses two different `sriovNetwork` CRs. The environment variable contains the Virtual Function (VF) PCI address that was allocated for the pod. If you use the same network in the pod definition, you must split the `pciAddress`. It is important to configure the correct MAC addresses of the traffic generator. This example uses custom MAC addresses.

# Using a virtual function in RDMA mode with a Mellanox NIC

> [!IMPORTANT]
> RDMA over Converged Ethernet (RoCE) is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

RDMA over Converged Ethernet (RoCE) is the only supported mode when using RDMA on OpenShift Container Platform.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Install the SR-IOV Network Operator.

- Log in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the following `SriovNetworkNodePolicy` object, and then save the YAML in the `mlx-rdma-node-policy.yaml` file.

    ``` yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetworkNodePolicy
    metadata:
      name: mlx-rdma-node-policy
      namespace: openshift-sriov-network-operator
    spec:
      resourceName: mlxnics
      nodeSelector:
        feature.node.kubernetes.io/network-sriov.capable: "true"
      priority: <priority>
      numVfs: <num>
      nicSelector:
        vendor: "15b3"
        deviceID: "1015"
        pfNames: ["<pf_name>", ...]
        rootDevices: ["<pci_bus_id>", "..."]
      deviceType: netdevice
      isRdma: true
    ```

    where:

    `spec.nicSelector.deviceID`
    Specifies the device hex code of the SR-IOV network device.

    `spec.deviceType`
    Specifies the driver type for the virtual functions. Set to `netdevice` for Mellanox NICs.

    `spec.isRdma`
    Set to `true` to enable RDMA mode.

    > [!NOTE]
    > See the `Configuring SR-IOV network devices` section for a detailed explanation on each option in `SriovNetworkNodePolicy`.
    >
    > When applying the configuration specified in a `SriovNetworkNodePolicy` object, the SR-IOV Operator might drain the nodes, and in some cases, reboot nodes. It might take several minutes for a configuration change to apply. Ensure that there are enough available nodes in your cluster to handle the evicted workload beforehand.
    >
    > After the configuration update is applied, all the pods in the `openshift-sriov-network-operator` namespace will change to a `Running` status.

2.  Create the `SriovNetworkNodePolicy` object by running the following command:

    ``` terminal
    $ oc create -f mlx-rdma-node-policy.yaml
    ```

3.  Create the following `SriovNetwork` object, and then save the YAML in the `mlx-rdma-network.yaml` file.

    ``` yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetwork
    metadata:
      name: mlx-rdma-network
      namespace: openshift-sriov-network-operator
    spec:
      networkNamespace: <target_namespace>
      ipam: |-
    # ...
      vlan: <vlan>
      resourceName: mlxnics
    ```

    where:

    `spec.ipam`
    Specifies a configuration object for the IPAM CNI plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition.

    > [!NOTE]
    > See the "Configuring SR-IOV additional network" section for a detailed explanation on each option in `SriovNetwork`.

    An optional library, app-netutil, provides several API methods for gathering network information about a container’s parent pod.

4.  Create the `SriovNetworkNodePolicy` object by running the following command:

    ``` terminal
    $ oc create -f mlx-rdma-network.yaml
    ```

5.  Create the following `Pod` spec, and then save the YAML in the `mlx-rdma-pod.yaml` file.

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: rdma-app
      namespace: <target_namespace>
      annotations:
        k8s.v1.cni.cncf.io/networks: mlx-rdma-network
    spec:
      containers:
      - name: testpmd
        image: <RDMA_image>
        securityContext:
          runAsUser: 0
          capabilities:
            add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW"]
        volumeMounts:
        - mountPath: /mnt/huge
          name: hugepage
        resources:
          limits:
            memory: "1Gi"
            cpu: "4"
            hugepages-1Gi: "4Gi"
          requests:
            memory: "1Gi"
            cpu: "4"
            hugepages-1Gi: "4Gi"
        command: ["sleep", "infinity"]
      volumes:
      - name: hugepage
        emptyDir:
          medium: HugePages
    ```

    where:

    `metadata.namespace`
    Specifies the same namespace where `SriovNetwork` object `mlx-rdma-network` is created. If you want to create the pod in a different namespace, change `target_namespace` in both the `Pod` spec and the `SriovNetwork` object.

    `spec.containers.image`
    Specifies the RDMA image which includes your application and the RDMA library used by the application.

    `spec.containers.securityContext.capabilities.add`
    Specifies additional capabilities required by the application inside the container for hugepage allocation, system resource allocation, and network interface access.

    `spec.containers.volumeMounts.mountPath`
    Specifies the path where the hugepage volume is mounted in the RDMA pod. The hugepage volume is backed by the `emptyDir` volume type with the medium being `HugePages`.

    `spec.containers.resources.limits.cpu`
    Specifies the number of CPUs. The RDMA pod usually requires exclusive CPUs be allocated from the kubelet. This is achieved by setting CPU Manager policy to `static` and creating a pod with `Guaranteed` QoS.

    `spec.containers.resources.limits.hugepages-1Gi`
    Specifies the hugepage size (`hugepages-1Gi` or `hugepages-2Mi`) and the quantity of hugepages that will be allocated to the RDMA pod. Configure `2Mi` and `1Gi` hugepages separately. Configuring `1Gi` hugepage requires adding kernel arguments to Nodes.

6.  Create the RDMA pod by running the following command:

    ``` terminal
    $ oc create -f mlx-rdma-pod.yaml
    ```

</div>

# A test pod template for clusters that use OVS-DPDK on OpenStack

The following `testpmd` pod demonstrates container creation with huge pages, reserved CPUs, and the SR-IOV port.

<div class="formalpara">

<div class="title">

An example `testpmd` pod

</div>

``` yaml
apiVersion: v1
kind: Pod
metadata:
  name: testpmd-dpdk
  namespace: mynamespace
  annotations:
    cpu-load-balancing.crio.io: "disable"
    cpu-quota.crio.io: "disable"
# ...
spec:
  containers:
  - name: testpmd
    command: ["sleep", "99999"]
    image: registry.redhat.io/openshift4/dpdk-base-rhel8:v4.9
    securityContext:
      capabilities:
        add: ["IPC_LOCK","SYS_ADMIN"]
      privileged: true
      runAsUser: 0
    resources:
      requests:
        memory: 1000Mi
        hugepages-1Gi: 1Gi
        cpu: '2'
        openshift.io/dpdk1: 1
      limits:
        hugepages-1Gi: 1Gi
        cpu: '2'
        memory: 1000Mi
        openshift.io/dpdk1: 1
    volumeMounts:
      - mountPath: /mnt/huge
        name: hugepage
        readOnly: False
  runtimeClassName: performance-cnf-performanceprofile
  volumes:
  - name: hugepage
    emptyDir:
      medium: HugePages
```

</div>

- The name `dpdk1` in this example is a user-created `SriovNetworkNodePolicy` resource. You can substitute this name for that of a resource that you create.

- If your performance profile is not named `cnf-performance profile`, replace that string with the correct performance profile name.

# Additional resources

- [Red Hat certified hardware (Red Hat Ecosystem Catalog)](https://catalog.redhat.com/en/hardware)

- [Configuring a cluster for RDMA in Red Hat OpenShift AI](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/latest/html/managing_openshift_ai/managing-distributed-workloads_managing-rhoai#configuring-a-cluster-for-rdma_managing-rhoai)

- [Creating a performance profile](../../scalability_and_performance/cnf-tuning-low-latency-nodes-with-perf-profile.md#cnf-create-performance-profiles_cnf-tuning-low-latency-nodes-with-perf-profile)

- [Adjusting the NIC queues with the performance profile](../../scalability_and_performance/cnf-tuning-low-latency-nodes-with-perf-profile.md#adjusting-nic-queues-with-the-performance-profile_cnf-tuning-low-latency-nodes-with-perf-profile)

- [Provisioning real-time and low latency workloads](../../scalability_and_performance/cnf-provisioning-low-latency-workloads.md#cnf-provisioning-low-latency-workloads)

- [Installing the SR-IOV Network Operator](../networking_operators/sr-iov-operator/installing-sriov-operator.md#installing-sriov-operator)

- [Configuring an SR-IOV network device](configuring-sriov-device.md#nw-sriov-networknodepolicy-object_configuring-sriov-device)

- [Dynamic IP address assignment configuration with Whereabouts](../multiple_networks/secondary_networks/configuring-ip-secondary-nwt.md#nw-multus-whereabouts_configuring-additional-network)

- [Disabling interrupt processing for individual pods](../../scalability_and_performance/cnf-provisioning-low-latency-workloads.md#disabling-interrupt-processing-for-individual-pods_cnf-provisioning-low-latency)

- [Configuring an SR-IOV Ethernet network attachment](configuring-sriov-net-attach.md#configuring-sriov-net-attach)
