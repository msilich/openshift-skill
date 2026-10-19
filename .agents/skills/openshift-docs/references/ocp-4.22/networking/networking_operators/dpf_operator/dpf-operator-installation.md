<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

After setting up the environment, install the NVIDIA DPF Operator and create the required DPF resources and DPU services.

> [!IMPORTANT]
> You must install the DPF Operator before the DPF HCP Provisioner Operator because that Operator requires DPF CRDs such as `DPUCluster`, `DPUFlavor`, `DPUDeployment`, and `DPFOperatorConfig`.

# DPF Operator installation environment variables

Set the following required environment variables before you install and configure the DPF Operator on OpenShift Container Platform. The values of these variables are used in multiple DPF Operator installation and configuration procedures.

| Variable | Description | Example value |
|----|----|----|
| `CLUSTER_NAME` | The name of the management cluster. | `<YOUR_CLUSTER_NAME>` |
| `BASE_DOMAIN` | The base domain for the management cluster. | `example.com` |
| `HOST_CLUSTER_API` | The API server hostname of the management cluster. Derived from `CLUSTER_NAME` and `BASE_DOMAIN`. | `api.mycluster.example.com` |
| `REGISTRY` | The Helm chart registry URL for the DPF Operator. | `https://helm.ngc.nvidia.com/nvidia/doca` |
| `TAG` | The version tag for the DPF Operator Helm chart. | `v26.4.1` |
| `TARGETCLUSTER_API_SERVER_PORT` | The port number of the hosted cluster API server. | `6443` |
| `VTEP_CIDR` | A dedicated IP range allocated from the DPU high-speed network for VTEP (tunnel endpoint) IPs. Used for DPU service IPs by HBN and OVN-Kubernetes tunnels. The management network and this VTEP CIDR network must be routable to each other in both directions. | `10.0.120.0/22` |
| `NUM_VFS` | Number of SR-IOV VFs per physical function. Sets `NUM_OF_VFS` in the DPUFlavor `nvconfig`. The `NodeSRIOVDevicePluginConfig` allocates these VFs as VF0 (DPF communication channel), VF1 (OVN-Kubernetes management), and the remainder (workload and RDMA). | `46` |
| `NODES_MTU` | The MTU value for the node network interfaces. Use `1500` for standard MTU environments or `9000` for jumbo frame environments. This value must be consistent across all DPF networking configuration. | `1500` (standard) or `9000` (jumbo frames) |
| `OVN_TEMPLATE_CHART_URL` | The OCI chart URL for the OVN-Kubernetes Helm chart. | `oci://ghcr.io/mellanox/charts` |
| `OVN_CHART_VERSION` | The version of the OVN-Kubernetes Helm chart. | `v26.4.1-ocp-release-v4.22` |
| `OVN_MTU` | The MTU value for OVN-Kubernetes overlay networking. Set to `1400` for standard MTU (1500 minus encapsulation overhead) or `8900` for jumbo frames (9000 minus encapsulation overhead). Must be kept consistent with `NODES_MTU`. | `1400` or `8900` |
| `DPU_HOST_CIDR` | The CIDR range of the subnet where the DPU host nodes reside. Used as the OVN `hostCIDR`. You must set this to your actual host subnet; the example value is illustrative only and is not a usable default. | `10.0.110.0/24` |
| `FLANNEL_POD_CIDR` | The pod CIDR for the Flannel network in the hosted cluster. Required for OpenShift Container Platform 4.22 and later. | `10.132.0.0/14` |
| `BFB_URL` | The download URL for the BlueField Bootstream File image used to provision DPUs. | `https://rhcos.mirror.openshift.com/art/storage/prod/streams/rhel-10.2/builds/10.2.20260715-0/aarch64/rhcos-10.2.20260715-0-nvidiabluefield.aarch64.bfb` |

DPF Operator environment variables

You must set the following environment variables in your terminal session before you proceed.

``` terminal
$ export CLUSTER_NAME="<YOUR_CLUSTER_NAME>"
$ export BASE_DOMAIN="example.com"
$ export HOST_CLUSTER_API="api.${CLUSTER_NAME}.${BASE_DOMAIN}"
$ export REGISTRY="https://helm.ngc.nvidia.com/nvidia/doca"
$ export TAG="v26.4.1"
$ export TARGETCLUSTER_API_SERVER_PORT="6443"
$ export VTEP_CIDR="10.0.120.0/22"
$ export NUM_VFS="46"
$ export NODES_MTU="1500"
$ export OVN_TEMPLATE_CHART_URL="oci://ghcr.io/mellanox/charts"
$ export OVN_CHART_VERSION="v26.4.1-ocp-release-v4.22"
$ export OVN_MTU=1400
$ export DPU_HOST_CIDR="10.0.110.0/24"
$ export FLANNEL_POD_CIDR="10.132.0.0/14"
$ export BFB_URL="https://rhcos.mirror.openshift.com/art/storage/prod/streams/rhel-10.2/builds/10.2.20260715-0/aarch64/rhcos-10.2.20260715-0-nvidiabluefield.aarch64.bfb"
```

# Install the DPF Operator

You can install the DPF Operator by using Helm to deploy the Operator into the `dpf-operator-system` namespace on your management cluster.

> [!IMPORTANT]
> You must install the DPF Operator before the DPF HCP Provisioner Operator because that Operator requires the following DPF custom resource definitions to be available: `DPUCluster`, `DPUFlavor`, `DPUDeployment`, and `DPFOperatorConfig`.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the management cluster as a user with the `cluster-admin` role.

- You have installed the `oc` CLI.

- You have installed the `helm` CLI.

- You have set the DPF Operator environment variables. For details, see "DPF Operator installation environment variables".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Add the DPF Helm repository and update the local cache:

    ``` terminal
    $ helm repo add --force-update dpf-repository ${REGISTRY}
    ```

    ``` terminal
    $ helm repo update
    ```

2.  Install the DPF Operator by using Helm:

    ``` terminal
    $ helm upgrade --install dpf-operator dpf-repository/dpf-operator \
        --namespace dpf-operator-system \
        --version "${TAG}" \
        --set kamajiEtcdDefrag.enabled=false \
        --set isOpenshift=true \
        --set enableNodeFeatureRules=false \
        --wait
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the Operator controller manager deployment has rolled out successfully:

    ``` terminal
    $ oc rollout status deployment --namespace dpf-operator-system dpf-operator-controller-manager
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    deployment "dpf-operator-controller-manager" successfully rolled out
    ```

    </div>

2.  Verify that all pods in the `dpf-operator-system` namespace are ready:

    ``` terminal
    $ oc wait --for=condition=ready --namespace dpf-operator-system pods --all
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    pod/argocd-application-controller-0 condition met
    pod/argocd-dex-server-6dd56c8469-bhsq4 condition met
    pod/argocd-redis-b4f94bb8d-wr86b condition met
    pod/argocd-repo-server-96765f997-79k9q condition met
    pod/argocd-server-648c7ff85f-7frtg condition met
    pod/dpf-operator-controller-manager-7bf9744c5f-cwrgc condition met
    pod/maintenance-operator-585767f779-8k2lx condition met
    ```

    </div>

</div>

# Create the DPFOperatorConfig custom resource

Create a `DPFOperatorConfig` custom resource to configure the DPF Operator components, including the provisioning controller, static cluster manager, and SR-IOV device plugin controller.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the DPF Operator.

- You have set the DPF Operator environment variables. For details, see "DPF Operator installation environment variables".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `dpfoperatorconfig.yaml` with the following content:

    > [!NOTE]
    > MTU Configuration: Set `NODES_MTU` to `1500` for standard MTU environments or `9000` for jumbo frame environments. This value must be consistent across:
    >
    > - Assisted Installer host configuration
    >
    > - DPFOperatorConfig networking section (this step)
    >
    > - DPUServiceNAD configuration
    >
    > Choose based on your network infrastructure capabilities.

    ``` yaml
    apiVersion: operator.dpu.nvidia.com/v1alpha1
    kind: DPFOperatorConfig
    metadata:
      name: dpfoperatorconfig
      namespace: dpf-operator-system
    spec:
      kamajiClusterManager:
        disable: true
      multus:
        disable: true
      cniInstaller:
        disable: true
      networking:
        controlPlaneMTU: $NODES_MTU      # management/OOB MTU (= NODES_MTU: 1500 standard, 9000 jumbo)
        highSpeedMTU: $NODES_MTU         # high-speed fabric MTU (= NODES_MTU; must match controlPlaneMTU)
        dpuNodeOOBBridgeName: br-ex      # OOB bridge for DPU provisioning; br-ex on OpenShift
      overrides:
        dpuCNIBinPath: /var/lib/cni/bin/
        dpuCNIPath: /run/multus/cni/net.d/
        dpuOpenvSwitchSystemSharedLib64Path: /lib64
        flannelSkipCNIConfigInstallation: false
        kubernetesAPIServerPort: $TARGETCLUSTER_API_SERVER_PORT
        kubernetesAPIServerVIP: $HOST_CLUSTER_API
        dpuLinkerCachePath: /etc/ld.so.cache
        dpuOptLibraryPath: /usr/opt
      provisioningController:
        enableDynamicBFCFGTemplates: true
        hostAgentDNSPolicy: Default
        dmsTimeout: 900
      nodeSRIOVDevicePluginController:
        devicePlugin:
          defaultResourcePrefix: openshift.io
        disable: false
        replicas: 1
      staticClusterManager:
        disable: false
      dpuServiceController:
        disableHostNetworkReadyNoExecuteTaints: false
      flannel:
        podCIDR: $FLANNEL_POD_CIDR
    ```

2.  Apply the resource file:

    ``` terminal
    $ envsubst < dpfoperatorconfig.yaml | oc apply -f -
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the provisioning controller manager deployment has rolled out:

    ``` terminal
    $ oc rollout status deployment --namespace dpf-operator-system dpf-provisioning-controller-manager
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    deployment "dpf-provisioning-controller-manager" successfully rolled out
    ```

    </div>

2.  Verify that the DPU service controller manager deployment has rolled out:

    ``` terminal
    $ oc rollout status deployment --namespace dpf-operator-system dpuservice-controller-manager
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    deployment "dpuservice-controller-manager" successfully rolled out
    ```

    </div>

3.  Verify that all Operator deployments in the `dpf-operator-system` namespace have rolled out:

    > [!NOTE]
    > You might need to run this command more than once, because the deployments become available at different times as the Operator reconciles its resources.

    ``` terminal
    $ oc rollout status deployment --namespace dpf-operator-system
    ```

4.  Optional: List the pods in the `dpf-operator-system` namespace to review their status:

    ``` terminal
    $ oc get pods -n dpf-operator-system
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                                    READY   STATUS    RESTARTS   AGE
    argocd-application-controller-0                          1/1     Running   0          64m
    argocd-dex-server-9dd99cc6c-pkl6j                       1/1     Running   0          64m
    argocd-redis-6749d85f98-mw9rc                           1/1     Running   0          64m
    argocd-repo-server-5fd79d655c-9rl26                     1/1     Running   0          64m
    argocd-server-5cc4f69c45-hzgm9                          1/1     Running   0          64m
    bfb-registry                                            1/1     Running   0          98s
    dpf-nodesriovdeviceplugin-controller-7c7bb889f6-xk6nm   1/1     Running   0          107s
    dpf-operator-controller-manager-6969c6d8bc-4njxd        1/1     Running   0          4m54s
    dpf-provisioning-controller-manager-54b6bdc57f-69lr7    1/1     Running   0          109s
    dpf-provisioning-controller-manager-54b6bdc57f-fg9f6    1/1     Running   0          109s
    dpuservice-controller-manager-5d9c4f6f67-wsdzt          1/1     Running   0          108s
    maintenance-operator-68c794b549-pp2dp                   1/1     Running   0          74m
    static-cm-controller-manager-745c8fd7d5-n8d2z           1/1     Running   0          110s
    ```

    </div>

</div>

# Create the NodeSRIOVDevicePluginConfig custom resource

You can create a `NodeSRIOVDevicePluginConfig` custom resource to define how SR-IOV virtual functions on the management cluster worker nodes are allocated to DPF components.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the DPF Operator.

- You have created the `DPFOperatorConfig` resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `nodesriovdevicepluginconfig.yaml` with the following content:

    ``` yaml
    apiVersion: noderesources.dpu.nvidia.com/v1alpha1
    kind: NodeSRIOVDevicePluginConfig
    metadata:
      name: bf3-vfs
      namespace: dpf-operator-system
    spec:
      devicePluginResources:
        - name: bf3-p0-vfs-mgmt
          type: vf
          ranges:
            - pfIndex: 0
              start: 1
              end: 1
        - name: bf3_vfs
          type: vf
          options:
            isRdma: true
          ranges:
            - pfIndex: 0
              start: 2
              end: 45
            - pfIndex: 1
              start: 0
              end: 45
    ```

    where:

    `bf3-p0-vfs-mgmt`
    Reserves VF index `1` on PF0 for DPU management connectivity.

    `bf3_vfs`
    Allocates VF indices `2-45` on PF0 and VF indices `0-45` on PF1 for workload traffic with RDMA enabled.

    `pfIndex`
    The `pfIndex` values refer to the first (`0`) and second (`1`) physical functions of the BlueField-3 DPU.

2.  Apply the resource file:

    ``` terminal
    $ oc apply -f nodesriovdevicepluginconfig.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the `NodeSRIOVDevicePluginConfig` resource is created:

  ``` terminal
  $ oc get nodesriovdevicepluginconfig -n dpf-operator-system
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  bf3-vfs    30s
  ```

  </div>

</div>

# Create the DPUFlavor custom resource

You can create a `DPUFlavor` custom resource to define the DPU configuration, including NVConfig parameters, kernel arguments, hugepages settings, and the OVS initialization script. The `DPUFlavor` also supports an optional `configFiles` field for custom DPU configuration files.

The `nvconfig` section contains BlueField-3 firmware parameters that the DPU agent applies by using `mlxconfig` during provisioning. If any parameter differs from the current firmware configuration, the provisioning controller triggers a system-level reset so that the changes take effect. The following parameters are required for DPF operation:

| Parameter | Value | Description |
|----|----|----|
| `INTERNAL_CPU_MODEL` | `1` | Switches the BlueField-3 to DPU mode where the ARM cores are active. A value of `0` keeps the card in NIC-only mode, which does not support DPF. |
| `SRIOV_EN` | `1` | Enables SR-IOV on both physical functions. The host agent creates Virtual Functions (VFs) that carry tenant traffic between the host and the DPU. |
| `NUM_OF_VFS` | Variable | Number of VFs per physical function. Set this value by using the `$NUM_VFS` environment variable. The default is `46`. |
| `LINK_TYPE_P1` / `LINK_TYPE_P2` | `ETH` | Sets both ports to Ethernet mode. DPF requires Ethernet. InfiniBand (`IB`) mode is not supported. |

Required BlueField-3 NVConfig parameters

> [!NOTE]
> If BlueField-3 already has the correct values, the DPU agent reports that no action is required and does not trigger a reset.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the DPF Operator.

- You have created the `DPFOperatorConfig` resource.

- You have set the DPF Operator environment variables. For details, see "DPF Operator installation environment variables".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `dpuflavor.yaml` for your MTU configuration and apply it.

    - For **Standard MTU (1500)**:

      ``` yaml
      apiVersion: provisioning.dpu.nvidia.com/v1alpha1
      kind: DPUFlavor
      metadata:
        name: hbn-ovnk
        namespace: dpf-operator-system
        annotations:
          # Required when flavor bfcfg exceeds the DPF limit of 128K
          provisioning.dpu.nvidia.com/skip-bfcfg-size-check: ""
      spec:
        grub:
          kernelParameters:
            - console=hvc0
            - console=ttyAMA0
            - earlycon=pl011,0x13010000
            - iommu.passthrough=1
            - cgroup_no_v1=net_prio,net_cls
            - hugepagesz=2048kB
            - hugepages=250
        nvconfig:
          - device: "*"
            parameters:
              - PF_BAR2_ENABLE=0
              - PER_PF_NUM_SF=1
              - PF_TOTAL_SF=20
              - PF_SF_BAR_SIZE=10
              - NUM_PF_MSIX_VALID=0
              - PF_NUM_PF_MSIX_VALID=1
              - PF_NUM_PF_MSIX=228
              - INTERNAL_CPU_MODEL=1
              - INTERNAL_CPU_OFFLOAD_ENGINE=0
              - SRIOV_EN=1
              - NUM_OF_VFS=$NUM_VFS
              - LAG_RESOURCE_ALLOCATION=1
              - LINK_TYPE_P1=ETH
              - LINK_TYPE_P2=ETH
        ovs:
          rawConfigScript: |
            #!/bin/bash
            set -e

            _ovs-vsctl() {
              ovs-vsctl --timeout 15 "$@"
            }

            restart_ovs=false

            _ovs-get-other-config() {
              _ovs-vsctl --if-exists get Open_vSwitch . "other_config:$1" 2>/dev/null | tr -d '"'
            }

            _ovs-set-other-config() {
              if [ "$(_ovs-get-other-config "$1")" != "$2" ]; then
                _ovs-vsctl set Open_vSwitch . "other_config:$1=$2"
                restart_ovs=true
              fi
            }

            _ovs-remove-other-config() {
              if [ -n "$(_ovs-get-other-config "$1")" ]; then
                _ovs-vsctl remove Open_vSwitch . other_config "$1"
                restart_ovs=true
              fi
            }

            _ovs-set-other-config doca-init true
            _ovs-set-other-config dpdk-max-memzones 50000
            _ovs-set-other-config hw-offload true
            _ovs-set-other-config pmd-quiet-idle true
            _ovs-set-other-config max-idle 20000
            _ovs-set-other-config max-revalidator 5000
            _ovs-set-other-config doca-congestion-threshold 60
            _ovs-set-other-config flow-limit 500000
            _ovs-set-other-config hw-offload-ct-unidir-udp-enabled true
            _ovs-remove-other-config default-datapath-type

            if [ "$restart_ovs" = true ]; then
              if systemctl list-unit-files openvswitch-switch.service &>/dev/null; then
                systemctl restart openvswitch-switch
              elif systemctl list-unit-files openvswitch.service &>/dev/null; then
                systemctl restart openvswitch
              fi
            fi

            _ovs-vsctl --may-exist add-br br-sfc
            _ovs-vsctl set bridge br-sfc datapath_type=netdev
            _ovs-vsctl set bridge br-sfc fail_mode=secure
            _ovs-vsctl --if-exists del-br br-hbn
            _ovs-vsctl --may-exist add-br br-hbn
            _ovs-vsctl set bridge br-hbn datapath_type=netdev
            _ovs-vsctl set bridge br-hbn fail_mode=secure
            _ovs-vsctl --may-exist add-port br-sfc p0
            _ovs-vsctl set Interface p0 type=dpdk
            _ovs-vsctl set Interface p0 mtu_request=9216
            _ovs-vsctl set Port p0 external_ids:dpf-type=physical

            # Activate DOCA for OVNK
            _ovs-vsctl set Open_vSwitch . external-ids:ovn-bridge-datapath-type=netdev
            # setup ovnkube managed bridge, br-dpu (this corresponds to br-ex on ovnk docs)
            _ovs-vsctl --may-exist add-br br-dpu
            _ovs-vsctl br-set-external-id br-dpu bridge-id br-dpu
            _ovs-vsctl br-set-external-id br-dpu bridge-uplink pbrdputobrovn
            _ovs-vsctl set bridge br-dpu datapath_type=netdev
            _ovs-vsctl --may-exist add-port br-dpu pf0hpf
            _ovs-vsctl set Interface pf0hpf type=dpdk

            # Create OVS bridge (br-ovn) in between the SC managed bridge and OVNK
            _ovs-vsctl --may-exist add-br br-ovn
            _ovs-vsctl set bridge br-ovn datapath_type=netdev
            _ovs-vsctl --may-exist add-port br-ovn pbrovntobrdpu
            _ovs-vsctl --may-exist add-port br-dpu pbrdputobrovn

            # Patch br-ovn and br-dpu together
            _ovs-vsctl set Interface pbrovntobrdpu type=patch options:peer=pbrdputobrovn
            _ovs-vsctl set Interface pbrdputobrovn type=patch options:peer=pbrovntobrdpu
      ```

    - For **Jumbo frames (MTU 9000)**:

      ``` yaml
      apiVersion: provisioning.dpu.nvidia.com/v1alpha1
      kind: DPUFlavor
      metadata:
        name: hbn-ovnk
        namespace: dpf-operator-system
        annotations:
          # Required when flavor bfcfg exceeds the DPF limit of 128K
          provisioning.dpu.nvidia.com/skip-bfcfg-size-check: ""
      spec:
        grub:
          kernelParameters:
            - console=hvc0
            - console=ttyAMA0
            - earlycon=pl011,0x13010000
            - iommu.passthrough=1
            - cgroup_no_v1=net_prio,net_cls
            - hugepagesz=2048kB
            - hugepages=250
        nvconfig:
          - device: "*"
            parameters:
              - PF_BAR2_ENABLE=0
              - PER_PF_NUM_SF=1
              - PF_TOTAL_SF=20
              - PF_SF_BAR_SIZE=10
              - NUM_PF_MSIX_VALID=0
              - PF_NUM_PF_MSIX_VALID=1
              - PF_NUM_PF_MSIX=228
              - INTERNAL_CPU_MODEL=1
              - INTERNAL_CPU_OFFLOAD_ENGINE=0
              - SRIOV_EN=1
              - NUM_OF_VFS=$NUM_VFS
              - LAG_RESOURCE_ALLOCATION=1
              - NUM_VF_MSIX=30
              - LINK_TYPE_P1=ETH
              - LINK_TYPE_P2=ETH
        ovs:
          rawConfigScript: |
            #!/bin/bash
            set -e

            _ovs-vsctl() {
              ovs-vsctl --timeout 15 "$@"
            }

            restart_ovs=false

            _ovs-get-other-config() {
              _ovs-vsctl --if-exists get Open_vSwitch . "other_config:$1" 2>/dev/null | tr -d '"'
            }

            _ovs-set-other-config() {
              if [ "$(_ovs-get-other-config "$1")" != "$2" ]; then
                _ovs-vsctl set Open_vSwitch . "other_config:$1=$2"
                restart_ovs=true
              fi
            }

            _ovs-remove-other-config() {
              if [ -n "$(_ovs-get-other-config "$1")" ]; then
                _ovs-vsctl remove Open_vSwitch . other_config "$1"
                restart_ovs=true
              fi
            }

            _ovs-set-other-config doca-init true
            _ovs-set-other-config dpdk-max-memzones 50000
            _ovs-set-other-config hw-offload true
            _ovs-set-other-config pmd-quiet-idle true
            _ovs-set-other-config max-idle 20000
            _ovs-set-other-config max-revalidator 5000
            _ovs-set-other-config doca-congestion-threshold 60
            _ovs-set-other-config flow-limit 500000
            _ovs-set-other-config hw-offload-ct-unidir-udp-enabled true
            _ovs-remove-other-config default-datapath-type

            if [ "$restart_ovs" = true ]; then
              if systemctl list-unit-files openvswitch-switch.service &>/dev/null; then
                systemctl restart openvswitch-switch
              elif systemctl list-unit-files openvswitch.service &>/dev/null; then
                systemctl restart openvswitch
              fi
            fi

            _ovs-vsctl --may-exist add-br br-sfc
            _ovs-vsctl set bridge br-sfc datapath_type=netdev
            _ovs-vsctl set bridge br-sfc fail_mode=secure
            _ovs-vsctl --if-exists del-br br-hbn
            _ovs-vsctl --may-exist add-br br-hbn
            _ovs-vsctl set bridge br-hbn datapath_type=netdev
            _ovs-vsctl set bridge br-hbn fail_mode=secure
            _ovs-vsctl --may-exist add-port br-sfc p0
            _ovs-vsctl set Interface p0 type=dpdk
            _ovs-vsctl set Interface p0 mtu_request=9216
            _ovs-vsctl set Port p0 external_ids:dpf-type=physical

            # Activate DOCA for OVNK
            _ovs-vsctl set Open_vSwitch . external-ids:ovn-bridge-datapath-type=netdev
            # setup ovnkube managed bridge, br-dpu (this corresponds to br-ex on ovnk docs)
            _ovs-vsctl --may-exist add-br br-dpu
            _ovs-vsctl br-set-external-id br-dpu bridge-id br-dpu
            _ovs-vsctl br-set-external-id br-dpu bridge-uplink pbrdputobrovn
            _ovs-vsctl set bridge br-dpu datapath_type=netdev
            _ovs-vsctl set Interface br-dpu mtu_request=9000
            _ovs-vsctl --may-exist add-port br-dpu pf0hpf
            _ovs-vsctl set Interface pf0hpf type=dpdk

            # Create OVS bridge (br-ovn) in between the SC managed bridge and OVNK
            _ovs-vsctl --may-exist add-br br-ovn
            _ovs-vsctl set bridge br-ovn datapath_type=netdev
            _ovs-vsctl set Interface br-ovn mtu_request=9000
            _ovs-vsctl --may-exist add-port br-ovn pbrovntobrdpu
            _ovs-vsctl --may-exist add-port br-dpu pbrdputobrovn

            # Patch br-ovn and br-dpu together
            _ovs-vsctl set Interface pbrovntobrdpu type=patch options:peer=pbrdputobrovn
            _ovs-vsctl set Interface pbrdputobrovn type=patch options:peer=pbrovntobrdpu
      ```

2.  Apply the resource file:

    ``` terminal
    $ envsubst < dpuflavor.yaml | oc apply -f -
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the `DPUFlavor` resource is created:

  ``` terminal
  $ oc get dpuflavor -n dpf-operator-system
  ```

</div>

# Create the `BFB` resource

You can create a `BFB` custom resource to define the DPU image, known as a BlueField Bootstream File, that is downloaded and placed on shared storage for DPU provisioning.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the DPF Operator.

- You have created the `DPFOperatorConfig` resource.

- You have set the DPF Operator environment variables. For details, see "DPF Operator installation environment variables".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `bfb.yaml` with the following content:

    ``` yaml
    apiVersion: provisioning.dpu.nvidia.com/v1alpha1
    kind: BFB
    metadata:
      name: bf-bundle
      namespace: dpf-operator-system
    spec:
      url: $BFB_URL
      versions:
        atf: 4.15.0-4-g419fbf393
        bsp: 4.15.0.13998
        doca: 3.4.1
        uefi: 4.15.0-19-g37c6f5adb2
    ```

2.  Apply the resource file:

    ``` terminal
    $ envsubst < bfb.yaml | oc apply -f -
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the BFB image phase is `Ready`:

  ``` terminal
  $ oc get bfb -n dpf-operator-system bf-bundle
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME        PHASE   AGE
  bf-bundle   Ready   3m
  ```

  </div>

</div>

# Create the DPUDeployment custom resource

You can create a `DPUDeployment` custom resource as the main orchestration object that connects DPU services with specific BFB images and DPU flavors. The `DPUDeployment` defines DPU sets for DPU provisioning and configures service chains to deploy services across DPUs.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the DPF Operator.

- You have created the `DPFOperatorConfig` resource.

- You have created the `NodeSRIOVDevicePluginConfig` resource.

- You have created the `DPUFlavor` resource.

- You have created the `BFB` resource and it is in the `Ready` phase.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `dpudeployment.yaml` with the following content:

    ``` yaml
    apiVersion: svc.dpu.nvidia.com/v1alpha1
    kind: DPUDeployment
    metadata:
      name: dpudeployment
      namespace: dpf-operator-system
    spec:
      dpus:
        nodeEffect:
          drain: true
        dpuSetStrategy:
          type: RollingUpdate
        bfb: bf-bundle
        flavor: hbn-ovnk
        dpuSets:
          - nameSuffix: "dpuset1"
            dpuNodeSelector:
              matchLabels:
                feature.node.kubernetes.io/dpu-enabled: ""
            dpuAnnotations:
              noderesources.dpu.nvidia.com/nodesriovdevicepluginconfig: bf3-vfs
      services:
        hbn:
          serviceTemplate: hbn
          serviceConfiguration: hbn
        ovn:
          serviceTemplate: ovn
          serviceConfiguration: ovn
        doca-telemetry-service:
          serviceTemplate: doca-telemetry-service
          serviceConfiguration: doca-telemetry-service
      serviceChains:
        switches:
          - ports:
              - serviceInterface:
                  matchLabels:
                    uplink: p0
              - service:
                  name: hbn
                  interface: p0_if
          - ports:
              - serviceInterface:
                  matchLabels:
                    uplink: p1
              - service:
                  name: hbn
                  interface: p1_if
          - ports:
              - serviceInterface:
                  matchLabels:
                    port: ovn
              - service:
                  name: hbn
                  interface: pf2dpu2_if
    ```

2.  Apply the resource file:

    ``` terminal
    $ oc apply -f dpudeployment.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify the `DPUDeployment` state:

  ``` terminal
  $ oc get DPUDeployment -n dpf-operator-system
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME            READY   PHASE     AGE
  dpudeployment   False   Pending   2m32s
  ```

  </div>

  > [!NOTE]
  > A `Pending` phase is expected at this stage. The `DPUDeployment` transitions to `Ready` after DPU provisioning is complete and all services are deployed.

</div>

# Create the HBN DPU service configuration

You can create a `DPUServiceConfiguration` custom resource for the Host-Based Networking (HBN) DPU service. The HBN service provides BGP-based networking on the DPU with ECMP routing support.

> [!NOTE]
> HBN and OVN-Kubernetes are currently the only supported DPU network services. The DOCA Telemetry Service (DTS), which you configure in a later step, is deployed for observability and is not a network service.

> [!NOTE]
> The `DPUServiceTemplate` resources are automatically created and managed by the `dpf-hcp-provisioner-operator`. You only need to create the `DPUServiceConfiguration` resources.

<div>

<div class="title">

Prerequisites

</div>

- The DPF Operator is installed.

- The `DPFOperatorConfig` resource is created.

- The DPF Operator environment variables are set. For details, see "DPF Operator installation environment variables".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `hbn.yaml` with the following content:

    ``` yaml
    apiVersion: svc.dpu.nvidia.com/v1alpha1
    kind: DPUServiceConfiguration
    metadata:
      name: hbn
      namespace: dpf-operator-system
    spec:
      deploymentServiceName: "hbn"
      serviceConfiguration:
        serviceDaemonSet:
          annotations:
            k8s.v1.cni.cncf.io/networks: |-
              [
              {"name": "iprequest", "interface": "ip_lo", "cni-args": {"poolNames": ["loopback"], "poolType": "cidrpool"}},
              {"name": "iprequest", "interface": "ip_pf2dpu2", "cni-args": {"poolNames": ["pool1"], "poolType": "cidrpool", "allocateDefaultGateway": true}}
              ]
        helmChart:
          values:
            configuration:
              perDPUValuesYAML: |
                - hostnamePattern: "*"
                  values:
                    bgp_peer_group: hbn
              startupYAMLJ2: |
                - header:
                    model: BLUEFIELD
                    nvue-api-version: nvue_v1
                    rev-id: 1.0
                    version: HBN 2.4.0
                - set:
                    interface:
                      lo:
                        ip:
                          address:
                            {{ ipaddresses.ip_lo.ip }}/32: {}
                        type: loopback
                      p0_if,p1_if:
                        type: swp
                        link:
                          mtu: 9216
                      pf2dpu2_if:
                        ip:
                          address:
                            {{ ipaddresses.ip_pf2dpu2.cidr }}: {}
                        type: swp
                        link:
                          mtu: 9216
                    router:
                      bgp:
                        autonomous-system: {{ ( ipaddresses.ip_lo.ip.split(".")[3] | int ) + 65101 }}
                        enable: on
                        graceful-restart:
                          mode: full
                        router-id: {{ ipaddresses.ip_lo.ip }}
                    vrf:
                      default:
                        router:
                          bgp:
                            address-family:
                              ipv4-unicast:
                                enable: on
                                redistribute:
                                  connected:
                                    enable: on
                              ipv6-unicast:
                                enable: on
                                redistribute:
                                  connected:
                                    enable: on
                            enable: on
                            neighbor:
                              p0_if:
                                peer-group: {{ config.bgp_peer_group }}
                                type: unnumbered
                              p1_if:
                                peer-group: {{ config.bgp_peer_group }}
                                type: unnumbered
                            path-selection:
                              multipath:
                                aspath-ignore: on
                            peer-group:
                              {{ config.bgp_peer_group }}:
                                remote-as: external
      interfaces:
        - name: p0_if
          network: mybrhbn
        - name: p1_if
          network: mybrhbn
        - name: pf2dpu2_if
          network: mybrhbn
    ```

2.  Apply the resource file:

    ``` terminal
    $ oc apply -f hbn.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    dpuserviceconfiguration.svc.dpu.nvidia.com/hbn created
    ```

    </div>

</div>

# Create the OVN-Kubernetes DPU service configuration

You can create a `DPUServiceConfiguration` custom resource for the OVN-Kubernetes DPU service. The OVN-Kubernetes service provides pod networking on the DPU.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the DPF Operator.

- You have created the `DPFOperatorConfig` resource.

- You have created the HBN `DPUServiceConfiguration` resource.

- You have set the DPF Operator environment variables. For details, see "DPF Operator installation environment variables".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `ovn-k.yaml` with the following content:

    ``` yaml
    apiVersion: svc.dpu.nvidia.com/v1alpha1
    kind: DPUServiceConfiguration
    metadata:
      name: ovn
      namespace: dpf-operator-system
    spec:
      deploymentServiceName: "ovn"
      serviceConfiguration:
        helmChart:
          values:
            global:
              enableOvnKubeIdentity: false
            k8sAPIServer: https://$HOST_CLUSTER_API:6443
            podNetwork: 10.128.0.0/14/23
            serviceNetwork: 172.30.0.0/16
            hostNetworkNamespace: "openshift-host-network"
            mtu: $OVN_MTU
            dpuManifests:
              kubernetesSecretName: "ovn-dpu"
              vtepCIDR: $VTEP_CIDR
              hostCIDR: $DPU_HOST_CIDR
              ipamPool: "pool1"
              ipamPoolType: "cidrpool"
              ipamVTEPIPIndex: 0
              ipamPFIPIndex: 1
              cniBinDir: "/var/lib/cni/bin/"
              cniConfDir: "/run/multus/cni/net.d"
    ```

2.  Apply the resource file:

    ``` terminal
    $ envsubst < ovn-k.yaml | oc apply -f -
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the HBN and OVN-Kubernetes service configurations are created:

  ``` terminal
  $ oc get dpuserviceconfiguration -n dpf-operator-system
  ```

</div>

# Create the DOCA Telemetry Service DPU service configuration

You can create a `DPUServiceConfiguration` custom resource for the DOCA Telemetry Service. The DOCA Telemetry Service provides metrics collection from the DPUs by using Prometheus.

> [!NOTE]
> The `DPUServiceTemplate` for DOCA Telemetry Service is automatically created and managed by the `dpf-hcp-provisioner-operator` controller. The operator uses the correct chart and image versions for the installed DPF version. You only need to create the `DPUServiceConfiguration` resource.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the DPF Operator.

- You have created the `DPFOperatorConfig` resource.

- You have set the DPF Operator environment variables. For details, see "DPF Operator installation environment variables".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `dts.yaml` with the following content:

    ``` yaml
    apiVersion: svc.dpu.nvidia.com/v1alpha1
    kind: DPUServiceConfiguration
    metadata:
      name: doca-telemetry-service
      namespace: dpf-operator-system
    spec:
      deploymentServiceName: "doca-telemetry-service"
      serviceConfiguration:
        configPorts:
          ports:
            - name: httpserverport
              port: 9189
              protocol: TCP
          serviceType: None
    ```

2.  Apply the resource file:

    ``` terminal
    $ oc apply -f dts.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the DOCA Telemetry Service configuration is created:

  ``` terminal
  $ oc get dpuserviceconfiguration -n dpf-operator-system doca-telemetry-service
  ```

</div>

# Create the OVN-Kubernetes credential request and role bindings

To authenticate with the management cluster API server, create a `DPUServiceCredentialRequest` custom resource and the associated role bindings to enable the OVN-Kubernetes DPU service on the hosted cluster. The `ClusterRoleBinding` grants the required permissions for OVN node network operations.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the DPF Operator.

- You have created the `DPFOperatorConfig` resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `dpucredentialreq.yaml` with the following content:

    ``` yaml
    apiVersion: svc.dpu.nvidia.com/v1alpha1
    kind: DPUServiceCredentialRequest
    metadata:
      name: ovn-dpu
      namespace: dpf-operator-system
    spec:
      serviceAccount:
        name: ovn-kubernetes-node-dpu-service
        namespace: openshift-ovn-kubernetes
      duration: 24h
      type: tokenFile
      secret:
        name: ovn-dpu
        namespace: dpf-operator-system
      metadata:
        labels:
          dpu.nvidia.com/image-pull-secret: ""
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: openshift-ovn-kubernetes-node-limited-dpu-service
      namespace: openshift-ovn-kubernetes
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: Role
      name: openshift-ovn-kubernetes-node-limited
    subjects:
    - kind: ServiceAccount
      name: ovn-kubernetes-node-dpu-service
      namespace: openshift-ovn-kubernetes
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: ovn-kubernetes-node-limited-binding
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: openshift-ovn-kubernetes-node-limited
    subjects:
    - kind: ServiceAccount
      name: ovn-kubernetes-node-dpu-service
      namespace: openshift-ovn-kubernetes
    ```

2.  Apply the resource file:

    ``` terminal
    $ oc apply -f dpucredentialreq.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the credential request and role bindings are created:

  ``` terminal
  $ oc get dpuservicecredentialrequest -n dpf-operator-system
  ```

  ``` terminal
  $ oc get clusterrolebinding ovn-kubernetes-node-limited-binding
  ```

</div>

# Create the DPUServiceInterface custom resources

You can create `DPUServiceInterface` custom resources to define interface objects that are specified in service chains. You must create physical interface resources for the DPU ports and an OVN-Kubernetes interface resource for host workloads.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the DPF Operator.

- You have created the `DPFOperatorConfig` resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `physical-if.yaml` with the following content to define the physical DPU port interfaces:

    ``` yaml
    apiVersion: svc.dpu.nvidia.com/v1alpha1
    kind: DPUServiceInterface
    metadata:
      name: p0
      namespace: dpf-operator-system
    spec:
      template:
        spec:
          template:
            metadata:
              labels:
                uplink: "p0"
            spec:
              interfaceType: physical
              physical:
                interfaceName: p0
    ---
    apiVersion: svc.dpu.nvidia.com/v1alpha1
    kind: DPUServiceInterface
    metadata:
      name: p1
      namespace: dpf-operator-system
    spec:
      template:
        spec:
          template:
            metadata:
              labels:
                uplink: "p1"
            spec:
              interfaceType: physical
              physical:
                interfaceName: p1
    ```

2.  Apply the physical interface resource file:

    ``` terminal
    $ oc apply -f physical-if.yaml
    ```

3.  Create a file named `ovnk-if.yaml` with the following content to define the OVN-Kubernetes interface:

    ``` yaml
    apiVersion: svc.dpu.nvidia.com/v1alpha1
    kind: DPUServiceInterface
    metadata:
      name: ovn
      namespace: dpf-operator-system
    spec:
      template:
        spec:
          template:
            metadata:
              labels:
                port: ovn
            spec:
              interfaceType: ovn
    ```

4.  Apply the OVN-Kubernetes interface resource file:

    ``` terminal
    $ oc apply -f ovnk-if.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that all `DPUServiceInterface` resources are created:

  ``` terminal
  $ oc get dpuserviceinterface -n dpf-operator-system
  ```

</div>

# Create the DPUServiceNAD resource

Create a `DPUServiceNAD` custom resource to define the network attachment available to DPU services on the hosted cluster. The `DPUServiceNAD` resource maps to an Open vSwitch (OVS) bridge on the DPU and specifies the resource type, IP address management (IPAM) mode, and maximum transmission unit (MTU) configuration:

- `mybrhbn` maps to the `br-hbn` bridge, used by the HBN service. IPAM is disabled because IP allocation is handled by `DPUServiceIPAM`.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the DPF Operator.

- You have created the `DPFOperatorConfig` resource.

- You have set the DPF Operator environment variables. For details, see "DPF Operator installation environment variables".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `dpuservice-nad.yaml` with the following content:

    ``` yaml
    apiVersion: svc.dpu.nvidia.com/v1alpha1
    kind: DPUServiceNAD
    metadata:
      name: mybrhbn
      namespace: dpf-operator-system
    spec:
      resourceType: sf
      ipam: false
      bridge: "br-hbn"
      serviceMTU: $NODES_MTU
    ```

2.  Apply the resource file:

    ``` terminal
    $ envsubst < dpuservice-nad.yaml | oc apply -f -
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the `DPUServiceNAD` resource is created:

  ``` terminal
  $ oc get dpuservicenad mybrhbn -n dpf-operator-system
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME       READY   AGE
  mybrhbn    True    2m
  ```

  </div>

</div>

# Create the `DPUServiceIPAM` resources

You can create `DPUServiceIPAM` custom resources to configure IP address management for DPU services. Two IPAM pools are required: one for the VTEP network used by the high-speed data plane, and one for loopback addresses used by the HBN service.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the DPF Operator.

- You have created the `DPFOperatorConfig` resource.

- You have set the DPF Operator environment variables. For details, see "DPF Operator installation environment variables".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `dpuservice-ipam.yaml` with the following content:

    ``` yaml
    ---
    apiVersion: svc.dpu.nvidia.com/v1alpha1
    kind: DPUServiceIPAM
    metadata:
      name: pool1
      namespace: dpf-operator-system
    spec:
      ipv4Network:
        network: $VTEP_CIDR
        gatewayIndex: 3
        prefixSize: 29
    ---
    apiVersion: svc.dpu.nvidia.com/v1alpha1
    kind: DPUServiceIPAM
    metadata:
      name: loopback
      namespace: dpf-operator-system
    spec:
      ipv4Network:
        network: "11.0.0.0/24"
        prefixSize: 32
    ```

2.  Apply the resource file:

    ``` terminal
    $ envsubst < dpuservice-ipam.yaml | oc apply -f -
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the `DPUServiceIPAM` resources are created:

  ``` terminal
  $ oc get dpuserviceipam -n dpf-operator-system
  ```

</div>
