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
    sriov-network-operator.4.17.0-202211021237   SR-IOV Network Operator   4.17.0-202211021237   sriov-network-operator.4.17.0-202210290517   Succeeded
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
    version: 4.17.0
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

- [Creating a host inventory (Red Hat Advanced Cluster Management documentation)](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.14/html-single/clusters/index#create-host-inventory-cli-steps)

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

2.  Remove the `spec.replicas` field from the `NodePool` resource to allow the cluster autoscaler to manage the node count. Run the following command:

    ``` terminal
    $ oc patch -n clusters nodepool <node_pool_name> --type=json  --patch='[{"op": "remove", "path": "/spec/replicas"}]'
    ```

3.  Enable cluster autoscaling to configure the minimum and maximum node counts for your node pools. Run the following command:

    ``` terminal
    $ oc patch -n <hosted_cluster_namespace> nodepool <nodepool_name> \
      --type=merge --patch='{"spec": {"autoScaling": {"max": 3, "min": 1}}}'
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
