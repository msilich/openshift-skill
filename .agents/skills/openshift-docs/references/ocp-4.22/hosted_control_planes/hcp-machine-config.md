<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In a standalone OpenShift Container Platform cluster, a machine config pool manages a set of nodes. You can handle a machine configuration by using the `MachineConfigPool` custom resource (CR).

> [!TIP]
> You can reference any `machineconfiguration.openshift.io` resources in the `nodepool.spec.config` field of the `NodePool` CR.

In hosted control planes, the `MachineConfigPool` CR does not exist. A node pool contains a set of compute nodes. You can handle a machine configuration by using node pools.

You can manage your workloads in your hosted cluster by using the cluster autoscaler.

> [!NOTE]
> In OpenShift Container Platform 4.18 or later, the default container runtime for worker nodes is changed from runC to crun.

# Configuring node pools for hosted control planes

In hosted control planes, you can configure node pools by creating a `MachineConfig` object inside of a config map in the management cluster.

<div>

<div class="title">

Procedure

</div>

1.  To create a `MachineConfig` object inside of a config map in the management cluster, enter the following information:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: <configmap_name>
      namespace: clusters
    data:
      config: |
        apiVersion: machineconfiguration.openshift.io/v1
        kind: MachineConfig
        metadata:
          labels:
            machineconfiguration.openshift.io/role: worker
          name: <machineconfig_name>
        spec:
          config:
            ignition:
              version: 3.2.0
            storage:
              files:
              - contents:
                  source: data:...
                mode: 420
                overwrite: true
                path: ${PATH}
    ```

    The `path` field specifies the path on the node where the `MachineConfig` object is stored.

2.  After you add the object to the config map, you can apply the config map to the node pool as follows:

    ``` yaml
    $ oc edit nodepool <nodepool_name> --namespace <hosted_cluster_namespace>
    ```

3.  Edit the `NodePool` resource to include the config map:

    ``` yaml
    apiVersion: hypershift.openshift.io/v1alpha1
    kind: NodePool
    metadata:
    # ...
      name: nodepool-1
      namespace: clusters
    # ...
    spec:
      config:
      - name: <configmap_name>
    # ...
    ```

    Replace `<configmap_name>` with the name of your config map.

</div>

# Referencing the kubelet configuration in node pools

To reference your kubelet configuration in node pools, you add the kubelet configuration in a config map and then apply the config map in the `NodePool` resource.

<div>

<div class="title">

Procedure

</div>

1.  Add the kubelet configuration inside of a config map in the management cluster by entering the following information:

    <div class="formalpara">

    <div class="title">

    Example `ConfigMap` object with the kubelet configuration

    </div>

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: <configmap_name>
      namespace: clusters
    data:
      config: |
        apiVersion: machineconfiguration.openshift.io/v1
        kind: KubeletConfig
        metadata:
          name: <kubeletconfig_name>
        spec:
          kubeletConfig:
            registerWithTaints:
            - key: "example.sh/unregistered"
              value: "true"
              effect: "NoExecute"
    ```

    </div>

    - `<configmap_name>` specifies the name of your config map.

    - `<kubeletconfig_name>` specifies the name of the `KubeletConfig` resource.

2.  Apply the config map to the node pool by entering the following command:

    ``` yaml
    $ oc edit nodepool <nodepool_name> --namespace clusters
    ```

    Replace `<nodepool_name>` with the name of your node pool.

    <div class="formalpara">

    <div class="title">

    Example `NodePool` resource configuration

    </div>

    ``` yaml
    apiVersion: hypershift.openshift.io/v1alpha1
    kind: NodePool
    metadata:
    # ...
      name: nodepool-1
      namespace: clusters
    # ...
    spec:
      config:
      - name: example-configmap-1
    # ...
    ```

    </div>

</div>

# Configuring node tuning in a hosted cluster

To set node-level tuning on the nodes in your hosted cluster, you can use the Node Tuning Operator. In hosted control planes, you can configure node tuning by creating config maps that contain `Tuned` objects and referencing those config maps in your node pools.

<div>

<div class="title">

Procedure

</div>

1.  Create a config map that contains a valid tuned manifest, and reference the manifest in a node pool. In the following example, a `Tuned` manifest defines a profile that sets `vm.dirty_ratio` to 55 on nodes that contain the `tuned-1-node-label` node label with any value. Save the following `ConfigMap` manifest in a file named `tuned-1.yaml`:

    ``` yaml
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: tuned-1
          namespace: clusters
        data:
          tuning: |
            apiVersion: tuned.openshift.io/v1
            kind: Tuned
            metadata:
              name: tuned-1
              namespace: openshift-cluster-node-tuning-operator
            spec:
              profile:
              - data: |
                  [main]
                  summary=Custom OpenShift profile
                  include=openshift-node
                  [sysctl]
                  vm.dirty_ratio="55"
                name: tuned-1-profile
              recommend:
              - priority: 20
                profile: tuned-1-profile
    ```

    > [!NOTE]
    > If you do not add any labels to an entry in the `spec.recommend` section of the Tuned spec, node-pool-based matching is assumed, so the highest priority profile in the `spec.recommend` section is applied to nodes in the pool. Although you can achieve more fine-grained node-label-based matching by setting a label value in the Tuned `.spec.recommend.match` section, node labels will not persist during an upgrade unless you set the `.spec.management.upgradeType` value of the node pool to `InPlace`.

2.  Create the `ConfigMap` object in the management cluster:

    ``` terminal
    $ oc --kubeconfig="$MGMT_KUBECONFIG" create -f tuned-1.yaml
    ```

3.  Reference the `ConfigMap` object in the `spec.tuningConfig` field of the node pool, either by editing a node pool or creating one. In this example, assume that you have only one `NodePool`, named `nodepool-1`, which contains 2 nodes.

    ``` yaml
        apiVersion: hypershift.openshift.io/v1alpha1
        kind: NodePool
        metadata:
          ...
          name: nodepool-1
          namespace: clusters
        ...
        spec:
          ...
          tuningConfig:
          - name: tuned-1
        status:
        ...
    ```

    > [!NOTE]
    > You can reference the same config map in multiple node pools. In hosted control planes, the Node Tuning Operator appends a hash of the node pool name and namespace to the name of the Tuned CRs to distinguish them. Outside of this case, do not create multiple TuneD profiles of the same name in different Tuned CRs for the same hosted cluster.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

Now that you have created the `ConfigMap` object that contains a `Tuned` manifest and referenced it in a `NodePool`, the Node Tuning Operator syncs the `Tuned` objects into the hosted cluster. You can verify which `Tuned` objects are defined and which TuneD profiles are applied to each node.

</div>

1.  List the `Tuned` objects in the hosted cluster:

    ``` terminal
    $ oc --kubeconfig="$HC_KUBECONFIG" get tuned.tuned.openshift.io \
      -n openshift-cluster-node-tuning-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME       AGE
    default    7m36s
    rendered   7m36s
    tuned-1    65s
    ```

    </div>

2.  List the `Profile` objects in the hosted cluster:

    ``` terminal
    $ oc --kubeconfig="$HC_KUBECONFIG" get profile.tuned.openshift.io \
      -n openshift-cluster-node-tuning-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                           TUNED            APPLIED   DEGRADED   AGE
    nodepool-1-worker-1            tuned-1-profile  True      False      7m43s
    nodepool-1-worker-2            tuned-1-profile  True      False      7m14s
    ```

    </div>

    > [!NOTE]
    > If no custom profiles are created, the `openshift-node` profile is applied by default.

3.  To confirm that the tuning was applied correctly, start a debug shell on a node and check the sysctl values:

    ``` terminal
    $ oc --kubeconfig="$HC_KUBECONFIG" \
      debug node/nodepool-1-worker-1 -- chroot /host sysctl vm.dirty_ratio
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    vm.dirty_ratio = 55
    ```

    </div>

# Deploying the SR-IOV Operator for hosted control planes

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
    sriov-network-operator.4.22.0-202211021237   SR-IOV Network Operator   4.22.0-202211021237   sriov-network-operator.4.22.0-202210290517   Succeeded
    ```

    </div>

2.  To verify that the SR-IOV pods are deployed, run the following command:

    ``` terminal
    $ oc get pods -n openshift-sriov-network-operator
    ```

</div>

# Configuring the NTP server for hosted clusters

You can configure the Network Time Protocol (NTP) server for your hosted clusters by using Butane.

<div>

<div class="title">

Procedure

</div>

1.  Create a Butane config file, `99-worker-chrony.bu`, that includes the contents of the `chrony.conf` file. For more information about Butane, see "Creating machine configs with Butane".

    <div class="formalpara">

    <div class="title">

    Example `99-worker-chrony.bu` configuration

    </div>

    ``` yaml
    # ...
    variant: openshift
    version: 4.22.0
    metadata:
      name: 99-worker-chrony
      labels:
        machineconfiguration.openshift.io/role: worker
    storage:
      files:
      - path: /etc/chrony.conf
        mode: 0644
        overwrite: true
        contents:
          inline: |
            pool 0.rhel.pool.ntp.org iburst
            driftfile /var/lib/chrony/drift
            makestep 1.0 3
            rtcsync
            logdir /var/log/chrony
    # ...
    ```

    </div>

    - `storage.files.mode` specifies an octal value mode for the `mode` field in the machine config file. After you create the file and apply the changes, the `mode` field is converted to a decimal value.

    - `storage.files.contents.inline` specifies any valid, reachable time source, such as the one provided by your Dynamic Host Configuration Protocol (DHCP) server.

      > [!NOTE]
      > For machine-to-machine communication, the NTP on the User Datagram Protocol (UDP) port is `123`. If you configured an external NTP time server, you must open UDP port `123`.

2.  Use Butane to generate a `MachineConfig` object file, `99-worker-chrony.yaml`, that contains a configuration that Butane sends to the nodes. Run the following command:

    ``` terminal
    $ butane 99-worker-chrony.bu -o 99-worker-chrony.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example `99-worker-chrony.yaml` configuration

    </div>

    ``` yaml
    # Generated by Butane; do not edit
    apiVersion: machineconfiguration.openshift.io/v1
    kind: MachineConfig
    metadata:
      labels:
        machineconfiguration.openshift.io/role: worker
      name: <machineconfig_name>
    spec:
      config:
        ignition:
          version: 3.2.0
        storage:
          files:
            - contents:
                source: data:...
              mode: 420
              overwrite: true
              path: /example/path
    ```

    </div>

3.  Add the contents of the `99-worker-chrony.yaml` file inside of a config map in the management cluster:

    <div class="formalpara">

    <div class="title">

    Example config map

    </div>

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: <configmap_name>
      namespace: <namespace>
    data:
      config: |
        apiVersion: machineconfiguration.openshift.io/v1
        kind: MachineConfig
        metadata:
          labels:
            machineconfiguration.openshift.io/role: worker
          name: <machineconfig_name>
        spec:
          config:
            ignition:
              version: 3.2.0
            storage:
              files:
              - contents:
                  source: data:...
                mode: 420
                overwrite: true
                path: /example/path
    # ...
    ```

    </div>

    Replace `<namespace>` with the name of your namespace where you created the node pool, such as `clusters`.

4.  Apply the config map to your node pool by running the following command:

    ``` terminal
    $ oc edit nodepool <nodepool_name> --namespace <hosted_cluster_namespace>
    ```

    <div class="formalpara">

    <div class="title">

    Example `NodePool` configuration

    </div>

    ``` yaml
    apiVersion: hypershift.openshift.io/v1alpha1
    kind: NodePool
    metadata:
    # ...
      name: nodepool-1
      namespace: clusters
    # ...
    spec:
      config:
      - name: example-config-map
    # ...
    ```

    </div>

5.  Add the list of your NTP servers in the `infra-env.yaml` file, which defines the `InfraEnv` custom resource (CR):

    <div class="formalpara">

    <div class="title">

    Example `infra-env.yaml` file

    </div>

    ``` yaml
    apiVersion: agent-install.openshift.io/v1beta1
    kind: InfraEnv
    # ...
    spec:
      additionalNTPSources:
      - <ntp_server>
      - <ntp_server1>
      - <ntp_server2>
    # ...
    ```

    </div>

    Replace `<ntp_server>` with the name of your NTP server. For more details about creating a host inventory and the `InfraEnv` CR, see "Creating a host inventory".

6.  Apply the `InfraEnv` CR by running the following command:

    ``` terminal
    $ oc apply -f infra-env.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Check the following fields to know the status of your host inventory:

  - `conditions`: The standard Kubernetes conditions indicating if the image was created successfully.

  - `isoDownloadURL`: The URL to download the Discovery Image.

  - `createdTime`: The time at which the image was last created. If you modify the `InfraEnv` CR, ensure that you have updated the timestamp before downloading a new image.

    Verify that your host inventory is created by running the following command:

    ``` terminal
    $ oc describe infraenv <infraenv_resource_name> -n <infraenv_namespace>
    ```

    > [!NOTE]
    > If you modify the `InfraEnv` CR, confirm that the `InfraEnv` CR has created a new Discovery Image by looking at the `createdTime` field. If you already booted hosts, boot them again with the latest Discovery Image.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating machine configs with Butane](../installing/install_config/installing-customizing.md#installation-special-config-butane_installing-customizing)

- [Creating a host inventory by using the command line interface](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/latest/html-single/clusters/index#create-host-inventory-cli)

</div>

# Scaling down the data plane to zero

If you are not using the hosted control plane, to save the resources and cost you can scale down a data plane to zero.

> [!NOTE]
> Ensure you are prepared to scale down the data plane to zero. Because the workload from the worker nodes disappears after scaling down.

<div>

<div class="title">

Procedure

</div>

1.  Set the `kubeconfig` file to access the hosted cluster by running the following command:

    ``` terminal
    $ export KUBECONFIG=<install_directory>/auth/kubeconfig
    ```

2.  Get the name of the `NodePool` resource associated to your hosted cluster by running the following command:

    ``` terminal
    $ oc get nodepool --namespace <hosted_cluster_namespace>
    ```

3.  Optional: To prevent the pods from draining, add the `nodeDrainTimeout` field in the `NodePool` resource by running the following command:

    ``` terminal
    $ oc edit nodepool <nodepool_name>  --namespace <hosted_cluster_namespace>
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    apiVersion: hypershift.openshift.io/v1alpha1
    kind: NodePool
    metadata:
    # ...
      name: nodepool-1
      namespace: clusters
    # ...
    spec:
      arch: amd64
      clusterName: clustername
      management:
        autoRepair: false
        replace:
          rollingUpdate:
            maxSurge: 1
            maxUnavailable: 0
          strategy: RollingUpdate
        upgradeType: Replace
      nodeDrainTimeout: 0s
      nodeVolumeDetachTimeout: 0
    # ...
    ```

    </div>

    `spec.arch.clusterName`
    Defines the name of your hosted cluster.

    `spec.nodeDrainTimeout`
    Specifies the total amount of time that the controller spends to drain a node. By default, the `nodeDrainTimeout: 0s` setting blocks the node draining process. To allow the node draining process to continue for a certain period of time, you can set the value of the `nodeDrainTimeout` field; for example, `nodeDrainTimeout: 1m`.

    `spec.nodeVolumeDetachTimeout`
    Specifies the total amount of time that the controller spends detaching volumes from a node. By default, the `0` setting blocks the volume detachment process.

    > [!NOTE]
    > To prevent nodes from getting stuck when scaling down, set the `.spec.nodeDrainTimeout` and `.spec.nodeVolumeDetachTimeout` in the `NodePool` resource to a value greater than `0`. This setting forces nodes to be removed after the timeout specified in the field is reached, regardless of whether the node can be drained or the volumes can be detached.

4.  Scale down the `NodePool` resource associated to your hosted cluster by running the following command:

    ``` terminal
    $ oc scale nodepool/<nodepool_name> --namespace <hosted_cluster_namespace> \
      --replicas=0
    ```

    > [!NOTE]
    > After scaling down the data plan to zero, some pods in the control plane stay in the `Pending` status and the hosted control plane stays up and running. If necessary, you can scale up the `NodePool` resource.

5.  Optional: Scale up the `NodePool` resource associated to your hosted cluster by running the following command:

    ``` terminal
    $ oc scale nodepool/<nodepool_name> --namespace <hosted_cluster_namespace> --replicas=1
    ```

    After rescaling the `NodePool` resource, wait for couple of minutes for the `NodePool` resource to become available in a `Ready` state.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the value for the `nodeDrainTimeout` field is greater than `0s` by running the following command:

  ``` terminal
  $ oc get nodepool -n <hosted_cluster_namespace> <nodepool_name> -ojsonpath='{.spec.nodeDrainTimeout}'
  ```

</div>

# Scaling up and down workloads in a hosted cluster

To scale up and down the workloads in your hosted cluster, you can use the `ScaleUpAndScaleDown` behavior. The compute nodes scale up when you add workloads and scale down when you delete workloads.

<div>

<div class="title">

Prerequisites

</div>

- You have created the `HostedCluster` and `NodePool` resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enable cluster autoscaling for your hosted cluster by setting the scaling behavior to `ScaleUpAndScaleDown`. Run the following command:

    ``` terminal
    $ oc patch -n <hosted_cluster_namespace> \
      hostedcluster <hosted_cluster_name> \
      --type=merge \
      --patch='{"spec": {"autoscaling": {"scaling": "ScaleUpAndScaleDown", "maxPodGracePeriod": 60, "scaleDown": {"utilizationThresholdPercent": 50}}}}'
    ```

2.  Remove the `spec.replicas` field from the `NodePool` resource to allow cluster autoscaler to manage the node count. Run the following command:

    ``` terminal
    $ oc patch -n <hosted_cluster_namespace> \
      nodepool <node_pool_name> \
      --type=json  \
      --patch='[{"op": "remove", "path": "/spec/replicas"}]'
    ```

3.  Enable cluster autoscaling to configure the minimum and maximum node counts for your node pools. Run the following command:

    ``` terminal
    $ oc patch -n <hosted_cluster_namespace> \
      nodepool <nodepool_name> \
      --type=merge --patch='{"spec": {"autoScaling": {"max": 3, "min": 1}}}'
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that all compute nodes are in the `Ready` status, run the following command:

  ``` terminal
  $ oc --kubeconfig <hosted_cluster_name>.kubeconfig get nodes
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Scaling the NodePool object for a hosted cluster (bare-metal platforms)](hcp-manage/hcp-manage-bm.md#hcp-bm-scale-np_hcp-manage-bm)

- [Scaling the NodePool object for a hosted cluster (non-bare metal agent machines)](hcp-manage/hcp-manage-non-bm.md#hcp-bm-scale-np_hcp-manage-non-bm)

- [Scaling a node pool (OpenShift Virtualization)](hcp-deploy/hcp-deploy-virt.md#hcp-virt-scale-nodpool_hcp-deploy-virt)

</div>

# Scaling up workloads in a hosted cluster

To scale up the workloads in your hosted cluster, you can use the `ScaleUpOnly` behavior.

<div>

<div class="title">

Prerequisites

</div>

- You have created the `HostedCluster` and `NodePool` resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enable cluster autoscaling for your hosted cluster by setting the scaling behavior to `ScaleUpOnly`. Run the following command:

    ``` terminal
    $ oc patch -n <hosted_cluster_namespace> hostedcluster <hosted_cluster_name> --type=merge --patch='{"spec": {"autoscaling": {"scaling": "ScaleUpOnly", "maxPodGracePeriod": 60}}}'
    ```

2.  Remove the `spec.replicas` field from the `NodePool` resource to allow the cluster autoscaler to manage the node count. Additionally, enable cluster autoscaling to configure the minimum and maximum node counts for your node pools. Enter the following command:

    ``` terminal
    $ oc -n clusters patch nodepool yhe-hosted-ap-northeast-1a \
      --type=json \
      -p='[
        {"op":"remove","path":"/spec/replicas"},
        {"op":"add","path":"/spec/autoScaling","value":{"min":2,"max":4}}
      ]'
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that all compute nodes are in the `Ready` status by running the following command:

    ``` terminal
    $ oc --kubeconfig <hosted_cluster_name>.kubeconfig get nodes
    ```

2.  Verify that the compute nodes are scaled up successfully by checking the node count for your node pools. Run the following command:

    ``` terminal
    $ oc --kubeconfig nested.config get nodes -l 'hypershift.openshift.io/nodePool=<node_pool_name>'
    ```

</div>

# Autoscaling to and from zero on hosted control planes node pools

You can configure hosted control planes node pools to autoscale down to zero compute nodes when no schedulable workloads remain on the pool and to provision nodes on-demand when pending pods require capacity. This capability reduces idle compute costs for variable workloads while the hosted control plane stays available.

> [!NOTE]
> Scale-from-zero autoscaling is available on OpenShift Container Platform 4.18 and later for eligible hosted control planes deployments on Amazon Web Services (AWS) and Azure. Platform validation and HyperShift Operator configuration determine whether a node pool can use `spec.autoScaling.min: 0`.

When you enable autoscaling on a `NodePool` object, you set `spec.autoScaling.min` to `0` and omit `spec.replicas`. The cluster autoscaler then manages pool size instead of a fixed replica count.

The cluster autoscaler scales up from zero differently than it scales pools that already have nodes. When a pool has zero nodes, the autoscaler cannot observe utilization on existing compute nodes. Instead, it uses instance-type metadata from the cloud provider (CPU, memory, and GPU capacity for the `NodePool` platform configuration) to decide how many nodes to provision for pending pods.

This behavior contrasts with classic fixed-minimum autoscaling, where `spec.autoScaling.min` is at least `1`. With a minimum of one or more replicas, the pool always retains at least one node even when workloads are idle.

The hosted control plane remains operational when compute node pools scale to zero. Control plane pods continue running on the management cluster. Workloads that target a scale-to-zero pool remain unschedulable until the autoscaler provisions new nodes.

## Terminology

`AutoscalingEnabled` condition
A `NodePool` status condition that reports whether autoscaling is correctly configured and active on the pool. Verify that this condition is `True` after you enable autoscaling.

minimum replicas
The `spec.autoScaling.min` value on a `NodePool` object. When autoscaling is enabled, this value is the lowest number of nodes the autoscaler can scale the pool to.

non-tainted pools
Node pools without taints that can accept system and user workloads. These pools must keep baseline capacity for highly available platform Operators.

scale-from-zero
Provisioning the first node in a pool that currently has zero nodes because pending pods require capacity.

scale-to-zero
Reducing a pool to zero nodes when no schedulable workloads remain on that pool and autoscaling minimum is `0`.

tainted pools
Node pools with taints that restrict which pods can schedule on them. Tainted workload pools are typical candidates for `spec.autoScaling.min: 0`.

## Use cases for scale-to-zero autoscaling

Scale-to-zero autoscaling is appropriate for the following scenarios:

- Development and test node pools that are idle outside business hours

- Batch or burst workload pools that run jobs periodically

- GPU or specialized instance pools that are expensive when idle

- Tainted workload pools that isolate optional capacity from system workloads

In each case, keep separate baseline pools for platform Operators and confine scale-to-zero configuration to pools that tolerate cold-start latency.

Do not use scale-to-zero autoscaling in the following scenarios:

- Do not configure scale-to-zero on pools that must always accept system or highly available platform workloads.

- Scaling all non-tainted node pools to zero violates the cluster-level minimum replica constraint and can prevent system pods from scheduling.

- Do not use scale-to-zero as a substitute for full cluster hibernation.

- Data-plane node pool autoscaling removes compute nodes only; the hosted control plane and management infrastructure remain active.

## Best practices for scale-to-zero autoscaling

Base and burst pool architecture
Keep at least two non-tainted compute nodes across baseline pools for highly available platform Operators. Confine `spec.autoScaling.min: 0` to tainted burst pools that run dev, test, batch, or specialized workloads.

Do not scale all non-tainted pools to zero. Use taints and tolerations to isolate burst capacity from system scheduling requirements.

Platform and version eligibility
Configure scale-to-zero only on AWS or Azure hosted clusters running OpenShift Container Platform 4.18 or later with a HyperShift Operator release that includes the backport.

Drain timeout tuning
Set `nodeDrainTimeout` and `nodeVolumeDetachTimeout` to positive values when workloads use persistent storage or long termination grace periods. Zero values block drain and detach operations and can leave nodes stuck during scale-down.

Tune timeouts for cost-optimization patterns such as nightly scale-down of dev pools.

Scale-up latency planning
Expect cold-start delay when pools scale from zero. Nodes must provision, join the cluster, and pull images before pending pods schedule.

Plan batch jobs and interactive workloads to tolerate this latency, or keep a small nonzero minimum on latency-sensitive pools.

Distinguish autoscaling from hibernation
Data-plane node pool autoscaling removes compute nodes only. The hosted control plane remains active on the management cluster. Full cluster hibernation is a separate operational pattern.

Cluster-level minimum replica constraint
The sum of `spec.autoScaling.min` (or fixed `spec.replicas` when autoscaling is disabled) across all non-tainted node pools must be at least `2`.

This constraint ensures highly available platform Operators, such as ingress, console, monitoring, and image registry, can schedule second replicas that require anti-affinity across compute nodes.

Tainted workload pools might use `spec.autoScaling.min: 0` because taints prevent system pods from scheduling on those nodes. Baseline non-tainted pools must retain enough minimum capacity to satisfy the cluster-wide constraint.

## Configuring autoscaling to and from zero on hosted control planes node pools

Configure a `NodePool` object to autoscale between zero and a maximum replica count on supported Amazon Web Services (AWS) or Azure hosted clusters. After configuration, verify the `AutoscalingEnabled` condition and validate scale-down and scale-up behavior.

<div>

<div class="title">

Prerequisites

</div>

- A hosted cluster on AWS or Azure running OpenShift Container Platform 4.18 or later

- Permission to edit `NodePool` objects in the hosted cluster namespace

- Understanding of scale-to-zero use cases, platform support, and Operator implications

- For AWS and Azure, scale-from-zero provider credentials

</div>

<div>

<div class="title">

Procedure

</div>

1.  Confirm that your hosted cluster platform supports `spec.autoScaling.min: 0`.

    On AWS and Azure, the `NodePool` API accepts `min: 0`. On other platforms, `min` must be at least `1`.

2.  Confirm that the HyperShift Operator enables scale-from-zero.

    On AWS and Azure, confirm that `--scale-from-zero-provider` and `--scale-from-zero-creds` are configured so instance-type metadata is available.

3.  Enable autoscaling on the target `NodePool` object by removing fixed replicas and setting autoscaling bounds.

    Replace `<hosted_cluster_namespace>`, `<nodepool_name>`, and `<max_replicas>` with your values.

    ``` terminal
    $ oc -n <hosted_cluster_namespace> patch nodepool <nodepool_name> \
      --type=json \
      -p '[{"op": "remove", "path": "/spec/replicas"}, \
           {"op": "add", "path": "/spec/autoScaling", \
            "value": {"min": 0, "max": <max_replicas>}}]'
    ```

    > [!NOTE]
    > `spec.replicas` and `spec.autoScaling` are mutually exclusive. When autoscaling is enabled, omit `spec.replicas` so the cluster autoscaler manages pool size.

4.  Optional: Configure hosted cluster-level autoscaling behavior on the `HostedCluster` resource.

    For example, set scaling behavior to `ScaleUpAndScaleDown`:

    ``` terminal
    $ oc patch -n <hosted_cluster_namespace> \
      hostedcluster <hosted_cluster_name> \
      --type=merge \
      --patch='{"spec": {"autoscaling": {"scaling": "ScaleUpAndScaleDown"}}}'
    ```

    Hosted cluster autoscaling settings apply cluster-wide autoscaler behavior. Node pool autoscaling bounds are configured on each `NodePool` object.

5.  Verify that the `AutoscalingEnabled` condition on the `NodePool` is `True`.

    ``` terminal
    $ oc get nodepool -n <hosted_cluster_namespace> <nodepool_name> \
      -o jsonpath='{range .status.conditions[*]}\
    ={"\n"}{end}'
    ```

    The output must include `AutoscalingEnabled=True`.

6.  Verify scale-down to zero by removing schedulable workloads from the pool.

    Remove or reschedule deployments, jobs, or other workloads that schedule on the target pool. If the pool uses taints, only workloads with matching tolerations count toward pool utilization.

    Wait for the cluster autoscaler to scale the pool down. When no schedulable workloads remain, the pool can reach zero nodes if `spec.autoScaling.min` is `0`.

7.  Verify scale-up from zero by deploying a workload that creates pending pods on the pool.

    For example, create a deployment with resource requests that exceed available capacity:

    ``` yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: scale-from-zero-test
      namespace: default
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: scale-from-zero-test
      template:
        metadata:
          labels:
            app: scale-from-zero-test
        spec:
          tolerations:
          - key: "<taint_key>"
            operator: "Equal"
            value: "<taint_value>"
            effect: "NoSchedule"
          containers:
          - name: app
            image: registry.redhat.io/ubi9/ubi-minimal
            resources:
              requests:
                cpu: "1"
                memory: 1Gi
    ```

    Apply the manifest and wait for the cluster autoscaler to provision nodes from zero.

8.  Extract the hosted cluster kubeconfig and verify node count changes.

    ``` terminal
    $ oc extract -n <hosted_cluster_namespace> \
      secret/<hosted_cluster_name>-admin-kubeconfig \
      --to=./hostedcluster-secrets --confirm
    ```

    ``` terminal
    $ oc --kubeconfig ./hostedcluster-secrets/kubeconfig get nodes
    ```

</div>

<div>

<div class="title">

Verification

</div>

- The `AutoscalingEnabled` condition on the `NodePool` is `True`.

- After workloads are removed, the pool scales down and `CURRENT NODES` can reach `0` when `min` is `0`.

- After pending pods are created, new nodes appear and reach `Ready` status.

</div>

> [!NOTE]
> When pools are at zero nodes, platform Operators on non-tainted baseline pools can report degraded status if minimum replica constraints are not satisfied.

## NodePool autoscaling configuration reference

Get familiar with the `NodePool` fields and status conditions for autoscaling to and from zero on hosted control planes.

| Field or condition | Description |
|----|----|
| `spec.autoScaling.min` | Minimum nodes the cluster autoscaler can scale the pool to. Valid values include `0` on Amazon Web Services (AWS) and Azure. On other platforms, the minimum must be at least `1`. |
| `spec.autoScaling.max` | Maximum nodes the cluster autoscaler can scale the pool to. Must be greater than or equal to `spec.autoScaling.min`. |
| `spec.replicas` | Fixed replica count when autoscaling is disabled. Must be omitted when `spec.autoScaling` is configured. |
| `AutoscalingEnabled` condition | Reports whether autoscaling is active on the `NodePool`. Status `True` indicates the autoscaler manages pool size. |
| `--scale-from-zero-provider` and `--scale-from-zero-creds` | On AWS and Azure, credentials and provider configuration for instance-type metadata used during scale-from-zero. |
| Non-tainted pool minimum sum | Sum of minimum replicas across non-tainted pools must be at least `2` cluster-wide for HA platform operators. |

> [!NOTE]
> `spec.replicas` and `spec.autoScaling` are mutually exclusive. Patch or edit the `NodePool` to remove `spec.replicas` before adding `spec.autoScaling`.

## NodePool API reference for autoscaling

Get familiar with the `NodePool` specification fields related to autoscaling, including scaling to and from zero on supported platforms.

### spec.autoScaling

| Field | Type | Description |
|----|----|----|
| `min` | integer | Minimum number of nodes for the pool when autoscaling is enabled. `0` is valid on Amazon Web Services (AWS) and Azure. Other platforms require `min` to be at least `1`. |
| `max` | integer | Maximum number of nodes the cluster autoscaler can add to the pool. |

### spec.replicas

| Field | Type | Description |
|----|----|----|
| `replicas` | integer | Fixed number of nodes when autoscaling is disabled. Omit this field when `spec.autoScaling` is set. |

### Drain and detach timeouts

| Field | Type | Description |
|----|----|----|
| `nodeDrainTimeout` | duration | Time the controller spends draining a node during scale-down. A value of `0s` blocks draining until a positive timeout is set. |
| `nodeVolumeDetachTimeout` | duration | Time the controller spends detaching volumes from a node during scale-down. A value of `0` blocks detachment until a positive timeout is set. |

### status.conditions

| Condition | Description |
|----|----|
| `AutoscalingEnabled` | Reports `True` when autoscaling is correctly configured and the autoscaler manages the pool. |

### HyperShift Operator flags

| Flag | Description |
|----|----|
| `--scale-from-zero-provider` | Provider used to fetch instance-type metadata on AWS and Azure. |
| `--scale-from-zero-creds` | Credentials for the scale-from-zero provider on AWS and Azure. |

# Setting the priority expander in a hosted cluster

You can define the priority for your node pools and create high priority machines before low priority machines by using the priority expander in your hosted cluster.

<div>

<div class="title">

Prerequisites

</div>

- You have created the `HostedCluster` and `NodePool` resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To define the priority for your node pools, create a config map named `priority-expander-configmap.yaml` in your hosted cluster. Node pools with low numbers receive high priority. See the following example configuration:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: cluster-autoscaler-priority-expander
      namespace: kube-system
    # ...
    data:
      priorities: |-
        10:
          - ".*<node_pool_name1>.*"
        100:
          - ".*<node_pool_name2>.*"
    # ...
    ```

2.  Generate the `kubeconfig` file by running the following command:

    ``` terminal
    $ hcp create kubeconfig --name <hosted_cluster_name> --namespace <hosted_cluster_namespace> > nested.config
    ```

3.  Create the `ConfigMap` object by running the following command:

    ``` terminal
    $ oc --kubeconfig nested.config create -f priority-expander-configmap.yaml
    ```

4.  Enable cluster autoscaling by setting the priority expander for your hosted cluster. Run the following command:

    ``` terminal
    $ oc patch -n <hosted_cluster_namespace> \
      hostedcluster <hosted_cluster_name> \
      --type=merge \
      --patch='{"spec": {"autoscaling": {"scaling": "ScaleUpOnly", "maxPodGracePeriod": 60, "expanders": ["Priority"]}}}'
    ```

5.  Remove the `spec.replicas` field from the `NodePool` resource to allow the cluster autoscaler to manage the node count. Run the following command:

    ``` terminal
    $ oc patch -n <hosted_cluster_namespace> \
      nodepool <node_pool_name> \
      --type=json
      --patch='[{"op": "remove", "path": "/spec/replicas"}]'
    ```

6.  Enable cluster autoscaling to configure the minimum and maximum node counts for your node pools. Run the following command:

    ``` terminal
    $ oc patch -n <hosted_cluster_namespace> \
      nodepool <nodepool_name> \
      --type=merge --patch='{"spec": {"autoScaling": {"max": 3, "min": 1}}}'
    ```

</div>

<div>

<div class="title">

Verification

</div>

- After you apply new workloads, verify that the compute nodes associated with the priority node pool are scaled up first. Run the following command to check the status of the compute node:

  ``` terminal
  $ oc --kubeconfig nested.config get nodes -l 'hypershift.openshift.io/nodePool=<node_pool_name>'
  ```

</div>

# Balancing ignored labels in a hosted cluster

After you scale up your node pools, you can use `balancingIgnoredLabels` to evenly distribute the machines across node pools.

<div>

<div class="title">

Prerequisites

</div>

- You have created the `HostedCluster` and `NodePool` resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Add the `node.group.balancing.ignored` label to each of the relevant node pool by using the same label value. Run the following command:

    ``` terminal
    $ oc patch -n <hosted_cluster_namespace> \
      nodepool <node_pool_name> \
      --type=merge \
      --patch='{"spec": {"nodeLabels": {"node.group.balancing.ignored": "<label_name>"}}}'
    ```

2.  Enable cluster autoscaling for your hosted cluster by running the following command:

    ``` terminal
    $ oc patch -n <hosted_cluster_namespace> \
     hostedcluster <hosted_cluster_name> \
     --type=merge \
     --patch='{"spec": {"autoscaling": {"balancingIgnoredLabels": ["node.group.balancing.ignored"]}}}'
    ```

3.  Remove the `spec.replicas` field from the `NodePool` resource to allow the cluster autoscaler to manage the node count. Run the following command:

    ``` terminal
    $ oc patch -n <hosted_cluster_namespace> \
      nodepool <node_pool_name> \
      --type=json \
      --patch='[{"op": "remove", "path": "/spec/replicas"}]'
    ```

4.  Enable cluster autoscaling to configure the minimum and maximum node counts for your node pools. Run the following command:

    ``` terminal
    $ oc patch -n <hosted_cluster_namespace> \
      nodepool <nodepool_name> \
      --type=merge --patch='{"spec": {"autoScaling": {"max": 3, "min": 1}}}'
    ```

5.  Generate the `kubeconfig` file by running the following command:

    ``` terminal
    $ hcp create kubeconfig \
      --name <hosted_cluster_name> \
      --namespace <hosted_cluster_namespace> > nested.config
    ```

6.  After you scale up the node pools, check that all compute nodes are in the `Ready` status by running the following command:

    ``` terminal
    $ oc --kubeconfig nested.config get nodes -l 'hypershift.openshift.io/nodePool=<node_pool_name>'
    ```

7.  Confirm that the new nodes contain the `node.group.balancing.ignored` label by running the following command:

    ``` terminal
    $ oc --kubeconfig nested.config get nodes \
      -l 'hypershift.openshift.io/nodePool=<node_pool_name>' \
      -o jsonpath='{.items[*].metadata.labels}' | grep "node.group.balancing.ignored"
    ```

8.  Enable cluster autoscaling for your hosted cluster by running the following command:

    ``` terminal
    $ oc patch -n <hosted_cluster_namespace> \
      hostedcluster <hosted_cluster_name> \
      --type=merge \
      --patch='{"spec": {"autoscaling": {"balancingIgnoredLabels": ["node.group.balancing.ignored"]}}}'
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the number of nodes provisioned by each node pool is evenly distributed. For example, if you created three node pools with the same label value, the node counts might be 3, 2, and 3. Run the following command:

  ``` terminal
  $ oc --kubeconfig nested.config get nodes -l 'hypershift.openshift.io/nodePool=<node_pool_name>'
  ```

</div>
