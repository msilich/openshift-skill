<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As a cluster administrator, you can configure hardware offloading on compatible nodes to increase data processing performance and reduce load on host CPUs.

Before you perform any tasks in the following documentation, ensure that you [installed the SR-IOV Network Operator](../networking_operators/sr-iov-operator/installing-sriov-operator.md#installing-sriov-operator).

# About hardware offloading

Open vSwitch hardware offloading is a method of processing network tasks by diverting them away from the CPU and offloading them to a dedicated processor on a network interface controller. As a result, clusters can benefit from faster data transfer speeds, reduced CPU workloads, and lower computing costs.

The key element for this feature is a modern class of network interface controllers known as SmartNICs. A SmartNIC is a network interface controller that is able to handle computationally-heavy network processing tasks. In the same way that a dedicated graphics card can improve graphics performance, a SmartNIC can improve network performance. In each case, a dedicated processor improves performance for a specific type of processing task.

In OpenShift Container Platform, you can configure hardware offloading for bare-metal nodes that have a compatible SmartNIC. Hardware offloading is configured and enabled by the SR-IOV Network Operator.

Hardware offloading is not compatible with all workloads or application types. Only the following two communication types are supported:

- pod-to-pod

- pod-to-service, where the service is a ClusterIP service backed by a regular pod

In all cases, hardware offloading takes place only when those pods and services are assigned to nodes that have a compatible SmartNIC. Suppose, for example, that a pod on a node with hardware offloading tries to communicate with a service on a regular node. On the regular node, all the processing takes place in the kernel, so the overall performance of the pod-to-service communication is limited to the maximum performance of that regular node. Hardware offloading is not compatible with DPDK applications.

Enabling hardware offloading on a node, but not configuring pods to use, it can result in decreased throughput performance for pod traffic. You cannot configure hardware offloading for pods that are managed by OpenShift Container Platform.

# Supported devices

Hardware offloading is supported on the following network interface controllers:

| Manufacturer | Model                                      | Vendor ID | Device ID |
|--------------|--------------------------------------------|-----------|-----------|
| Mellanox     | MT27800 Family \[ConnectX‑5\]              | 15b3      | 1017      |
| Mellanox     | MT28880 Family \[ConnectX‑5 Ex\]           | 15b3      | 1019      |
| Mellanox     | MT2892 Family \[ConnectX‑6 Dx\]            | 15b3      | 101d      |
| Mellanox     | MT2894 Family \[ConnectX-6 Lx\]            | 15b3      | 101f      |
| Mellanox     | MT42822 BlueField-2 in ConnectX-6 NIC mode | 15b3      | a2d6      |

Supported network interface controllers

# Prerequisites

Before you configure hardware offloading, ensure that the following conditions are met.

- Your cluster has at least one bare-metal machine with a network interface controller that is supported for hardware offloading.

- You installed the SR-IOV Network Operator.

- Your cluster uses the OVN-Kubernetes network plugin.

- In your OVN-Kubernetes network plugin configuration, the `gatewayConfig.routingViaHost` field is set to `false`.

<div>

<div class="title">

Additional resources

</div>

- [Installing the SR-IOV Network Operator](../networking_operators/sr-iov-operator/installing-sriov-operator.md#installing-sriov-operator)

- [About the OVN-Kubernetes network plugin](../ovn_kubernetes_network_provider/about-ovn-kubernetes.md#about-ovn-kubernetes)

- [OVN-Kubernetes network plugin configuration](../networking_operators/cluster-network-operator.md#gatewayConfig-object_cluster-network-operator)

</div>

# Setting the SR-IOV Network Operator into systemd mode

To support hardware offloading, you must first set the SR-IOV Network Operator into `systemd` mode.

<div>

<div class="title">

Prerequisites

</div>

- You installed the OpenShift CLI (`oc`).

- You have access to the cluster as a user that has the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `SriovOperatorConfig` custom resource (CR) to deploy all the SR-IOV Operator components:

    1.  Create a file named `sriovOperatorConfig.yaml` that contains the following YAML:

        ``` yaml
        apiVersion: sriovnetwork.openshift.io/v1
        kind: SriovOperatorConfig
        metadata:
          name: default
          namespace: openshift-sriov-network-operator
        spec:
          enableInjector: true
          enableOperatorWebhook: true
          configurationMode: "systemd"
          logLevel: 2
        ```

        - The only valid name for the `SriovOperatorConfig` resource is `default` and it must be in the namespace where the Operator is deployed.

        - Setting the SR-IOV Network Operator into `systemd` mode is only relevant for Open vSwitch hardware offloading.

    2.  Create the resource by running the following command:

        ``` terminal
        $ oc apply -f sriovOperatorConfig.yaml
        ```

</div>

# Configuring a machine config pool for hardware offloading

To enable hardware offloading, you now create a dedicated machine config pool and configure it to work with the SR-IOV Network Operator.

<div>

<div class="title">

Prerequisites

</div>

- SR-IOV Network Operator installed and set into `systemd` mode.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a machine config pool for machines you want to use hardware offloading on.

    1.  Create a file, such as `mcp-offloading.yaml`, with content such as the following example:

        ``` yaml
        apiVersion: machineconfiguration.openshift.io/v1
        kind: MachineConfigPool
        metadata:
          name: <mcp_name>
        spec:
          machineConfigSelector:
            matchExpressions:
              - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker,<mcp_name>]}
          nodeSelector:
            matchLabels:
              node-role.kubernetes.io/<mcp_name>: ""
        ```

        - `<mcp_name>` specifies the name of your machine config pool for hardware offloading. This value is used as the machine config pool name, the machine config selector value, and the node role label.

    2.  Apply the configuration for the machine config pool:

        ``` terminal
        $ oc create -f mcp-offloading.yaml
        ```

2.  Add nodes to the machine config pool. Label each node with the node role label of your pool:

    ``` terminal
    $ oc label node worker-2 node-role.kubernetes.io/mcp-offloading=""
    ```

3.  Optional: To verify that the new pool is created, run the following command:

    ``` terminal
    $ oc get nodes
    ```

    The following is example output:

    ``` terminal
    NAME       STATUS   ROLES                   AGE   VERSION
    master-0   Ready    master                  2d    v1.33.4
    master-1   Ready    master                  2d    v1.33.4
    worker-0   Ready    worker                  2d    v1.33.4
    worker-1   Ready    worker                  2d    v1.33.4
    worker-2   Ready    mcp-offloading,worker   47h   v1.33.4
    ```

4.  Add this machine config pool to the `SriovNetworkPoolConfig` custom resource:

    1.  Create a file, such as `sriov-pool-config.yaml`, with content such as the following example:

        ``` yaml
        apiVersion: sriovnetwork.openshift.io/v1
        kind: SriovNetworkPoolConfig
        metadata:
          name: sriovnetworkpoolconfig-offload
          namespace: openshift-sriov-network-operator
        spec:
          ovsHardwareOffloadConfig:
            name: <mcp_name>
        ```

        - `<mcp_name>` specifies the name of your machine config pool for hardware offloading.

    2.  Apply the configuration:

        ``` terminal
        $ oc create -f <SriovNetworkPoolConfig_name>.yaml
        ```

        > [!NOTE]
        > When you apply the configuration specified in a `SriovNetworkPoolConfig` object, the SR-IOV Operator drains and restarts the nodes in the machine config pool.
        >
        > It might take several minutes for a configuration changes to apply.

</div>

# Configuring the SR-IOV network node policy

You can create an SR-IOV network device configuration for a node by creating an SR-IOV network node policy. To enable hardware offloading, you must define the `.spec.eSwitchMode` field with the value `"switchdev"`.

The following procedure creates an SR-IOV interface for a network interface controller with hardware offloading.

<div>

<div class="title">

Prerequisites

</div>

- You installed the OpenShift CLI (`oc`).

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file, such as `sriov-node-policy.yaml`, with content such as the following example:

    ``` yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetworkNodePolicy
    metadata:
      name: <name>
      namespace: openshift-sriov-network-operator
    spec:
      deviceType: netdevice
      eSwitchMode: "switchdev"
      nicSelector:
        deviceID: "1019"
        rootDevices:
        - 0000:d8:00.0
        vendor: "15b3"
        pfNames:
        - ens8f0
      nodeSelector:
        feature.node.kubernetes.io/network-sriov.capable: "true"
      numVfs: 6
      priority: 5
      resourceName: mlxnics
    ```

    - `<name>` specifies the name for the custom resource object.

    - The `deviceType` field must be set to `netdevice`. Hardware offloading is not supported with `vfio-pci`.

    - The `eSwitchMode` field must be set to `"switchdev"`.

2.  Apply the configuration for the policy:

    ``` terminal
    $ oc create -f sriov-node-policy.yaml
    ```

    > [!NOTE]
    > When you apply the configuration specified in a `SriovNetworkPoolConfig` object, the SR-IOV Operator drains and restarts the nodes in the machine config pool.
    >
    > It might take several minutes for a configuration change to apply.

</div>

## An example SR-IOV network node policy for OpenStack

The following example describes an SR-IOV interface for a network interface controller (NIC) with hardware offloading on Red Hat OpenStack Platform (RHOSP).

The following example shows an SR-IOV interface for a NIC with hardware offloading on RHOSP:

``` yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: ${name}
  namespace: openshift-sriov-network-operator
spec:
  deviceType: switchdev
  isRdma: true
  nicSelector:
    netFilter: openstack/NetworkID:${net_id}
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: 'true'
  numVfs: 1
  priority: 99
  resourceName: ${name}
```

# Improving network traffic performance using a virtual function

Follow this procedure to assign a virtual function to the OVN-Kubernetes management port and increase its network traffic performance.

This procedure results in the creation of two pools: the first has a virtual function used by OVN-Kubernetes, and the second comprises the remaining virtual functions.

<div>

<div class="title">

Prerequisites

</div>

- You installed the OpenShift CLI (`oc`).

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Add the `network.operator.openshift.io/smart-nic` label to each worker node with a SmartNIC present by running the following command:

    ``` terminal
    $ oc label node <node-name> network.operator.openshift.io/smart-nic=
    ```

    Use the `oc get nodes` command to get a list of the available nodes.

2.  Create a policy named `sriov-node-mgmt-vf-policy.yaml` for the management port with content such as the following example:

    ``` yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetworkNodePolicy
    metadata:
      name: sriov-node-mgmt-vf-policy
      namespace: openshift-sriov-network-operator
    spec:
      deviceType: netdevice
      eSwitchMode: "switchdev"
      nicSelector:
        deviceID: "1019"
        rootDevices:
        - 0000:d8:00.0
        vendor: "15b3"
        pfNames:
        - <pf_name>#0-0
      nodeSelector:
        network.operator.openshift.io/smart-nic: ""
      numVfs: <num_vfs>
      priority: 5
      resourceName: mgmtvf
    ```

    - `<pf_name>` specifies the network device for your use case. The `#0-0` part of the `pfNames` value reserves a single virtual function used by OVN-Kubernetes.

    - `<num_vfs>` specifies the number of virtual functions. Replace this value with one that meets your requirements. For more information, see *SR-IOV network node configuration object* in the *Additional resources* section.

3.  Create a policy named `sriov-node-policy.yaml` with content such as the following example:

    ``` yaml
    apiVersion: sriovnetwork.openshift.io/v1
    kind: SriovNetworkNodePolicy
    metadata:
      name: sriov-node-policy
      namespace: openshift-sriov-network-operator
    spec:
      deviceType: netdevice
      eSwitchMode: "switchdev"
      nicSelector:
        deviceID: "1019"
        rootDevices:
        - 0000:d8:00.0
        vendor: "15b3"
        pfNames:
        - <pf_name>#1-5
      nodeSelector:
        network.operator.openshift.io/smart-nic: ""
      numVfs: <num_vfs>
      priority: 5
      resourceName: mlxnics
    ```

    - `<pf_name>` specifies the network device for your use case.

    - `<num_vfs>` specifies the number of virtual functions. Replace this value with the value specified in the `sriov-node-mgmt-vf-policy.yaml` file. For more information, see *SR-IOV network node configuration object* in the *Additional resources* section.

    > [!NOTE]
    > The `sriov-node-mgmt-vf-policy.yaml` file has different values for the `pfNames` and `resourceName` keys than the `sriov-node-policy.yaml` file.

4.  Apply the configuration for both policies:

    ``` terminal
    $ oc create -f sriov-node-policy.yaml
    ```

    ``` terminal
    $ oc create -f sriov-node-mgmt-vf-policy.yaml
    ```

5.  Create a Cluster Network Operator (CNO) ConfigMap in the cluster for the management configuration:

    1.  Create a ConfigMap named `hardware-offload-config.yaml` with the following contents:

        ``` yaml
        apiVersion: v1
        kind: ConfigMap
        metadata:
            name: hardware-offload-config
            namespace: openshift-network-operator
        data:
            mgmt-port-resource-name: openshift.io/mgmtvf
        ```

    2.  Apply the configuration for the ConfigMap:

        ``` terminal
        $ oc create -f hardware-offload-config.yaml
        ```

</div>

<div id="additional-resources_using-vf-improve-network-traffic-performance">

<div class="title">

Additional resources

</div>

- [SR-IOV network node configuration object](configuring-sriov-device.md#nw-sriov-networknodepolicy-object_configuring-sriov-device)

</div>

# Creating a network attachment definition

After you define the machine config pool and the SR-IOV network node policy, you can create a network attachment definition for the network interface controller (NIC) you specified.

<div>

<div class="title">

Prerequisites

</div>

- You installed the OpenShift CLI (`oc`).

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file, such as `net-attach-def.yaml`, with content such as the following example:

    ``` yaml
    apiVersion: "k8s.cni.cncf.io/v1"
    kind: NetworkAttachmentDefinition
    metadata:
      name: <net_attach_def_name>
      namespace: <net_attach_def_namespace>
      annotations:
        k8s.v1.cni.cncf.io/resourceName: openshift.io/<resource_name>
    spec:
      config: '{"cniVersion":"0.3.1","name":"ovn-kubernetes","type":"ovn-k8s-cni-overlay","ipam":{},"dns":{}}'
    ```

    - `<net_attach_def_name>` specifies the name for your network attachment definition.

    - `<net_attach_def_namespace>` specifies the namespace for your network attachment definition.

    - `<resource_name>` specifies the value of the `spec.resourceName` field from the `SriovNetworkNodePolicy` object.

2.  Apply the configuration for the network attachment definition:

    ``` terminal
    $ oc create -f net-attach-def.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Run the following command to check that the new definition exists:

  ``` terminal
  $ oc get net-attach-def -A
  ```

  The output shows the namespace, name, and age of the new definition.

</div>

# Adding the network attachment definition to your pods

After you create the machine config pool, the `SriovNetworkPoolConfig` and `SriovNetworkNodePolicy` custom resources, and the network attachment definition, you can apply these configurations to your pods by adding the network attachment definition to your pod specifications.

<div>

<div class="title">

Procedure

</div>

- In the pod specification, add the `.metadata.annotations.k8s.v1.cni.cncf.io/networks` field and specify the network attachment definition you created for hardware offloading:

  ``` yaml
  ....
  metadata:
    annotations:
      v1.multus-cni.io/default-network: <namespace>/<net_attach_def_name>
  ```

  - `<namespace>/<net_attach_def_name>` specifies the namespace and name of the network attachment definition you created for hardware offloading.

</div>
