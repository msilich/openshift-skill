<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

After the DPF Operator and the hosted cluster are configured, adjust the OVN-Kubernetes CNI settings, add DPU-equipped worker nodes to the management cluster, and provision the DPUs.

# Enable the OVN-Kubernetes resource injector

You can install the OVN-Kubernetes resource injector by using Helm to deploy a mutating admission webhook that automatically injects SR-IOV virtual function resource requests and network attachment annotations into each pod scheduled to a worker node.

> [!NOTE]
> Virtual function resource capacity on worker nodes is provided by the `NodeSRIOVDevicePluginConfig` resource, which replaces the manual SR-IOV device plugin `DaemonSet` and control plane node patching used in earlier DPF versions.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the management cluster as a user with the `cluster-admin` role.

- You have installed the `oc` CLI.

- You have installed the `helm` CLI.

- You have set the DPF Operator environment variables. For details, see "DPF Operator installation environment variables".

- You have created the `NodeSRIOVDevicePluginConfig` resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Install the OVN-Kubernetes resource injector by using Helm:

    ``` terminal
    $ helm upgrade --install -n openshift-ovn-kubernetes ovn-kubernetes \
      "$OVN_TEMPLATE_CHART_URL/ovn-kubernetes-chart" \
      --version "${OVN_CHART_VERSION}" \
      --skip-crds \
      --set ovn-kubernetes-resource-injector.enabled=true \
      --set ovn-kubernetes-resource-injector.resourceName="openshift.io/bf3_vfs" \
      --set ovn-kubernetes-resource-injector.prioritizeOffloading=false \
      --set ovn-kubernetes-resource-injector.controllerManager.hostNetwork=true \
      --set ovn-kubernetes-resource-injector.controllerManager.webhookPort="19443" \
      --set ovn-kubernetes-resource-injector.controllerManager.healthProbeBindAddress=":18081" \
      --set ovn-kubernetes-resource-injector.controllerManager.webhook.image.pullPolicy=IfNotPresent \
      --set "ovn-kubernetes-resource-injector.controllerManager.webhook.args={--leader-elect,--metrics-bind-address=:29091}" \
      --set nodeWithDPUManifests.enabled=false \
      --set nodeWithoutDPUManifests.enabled=false \
      --set dpuManifests.enabled=false \
      --set controlPlaneManifests.enabled=false \
      --set commonManifests.enabled=false
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME: ovn-kubernetes
    LAST DEPLOYED: Sun Nov  2 17:10:29 2025
    NAMESPACE: openshift-ovn-kubernetes
    STATUS: deployed
    REVISION: 1
    DESCRIPTION: Install complete
    TEST SUITE: None
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

- Verify the resource injector mutating webhook configuration was applied:

  ``` terminal
  $ oc get mutatingwebhookconfiguration | grep ovn
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                                                WEBHOOKS   AGE
  ovn-kubernetes-ovn-kubernetes-resource-injector     1          22h
  ```

  </div>

</div>

# OVN-Kubernetes DPU-Host mode

DPU-Host mode on worker nodes with accelerated OVN-Kubernetes CNI is automatically configured by the DPF provisioning controller.

When the `DPFOperatorConfig` resource is created and worker nodes with the `worker-dpu` label are provisioned, the DPF provisioning controller automatically configures the required settings for DPU-Host mode, including the network node identity and hardware offload configuration.

# Add worker nodes by using the Bare Metal Operator

You can add DPU-equipped worker nodes to the management cluster by creating `BareMetalHost` resources that the Bare Metal Operator provisions.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the management cluster as a user with the `cluster-admin` role.

- You have installed the `oc` CLI.

- You have installed the Bare Metal Operator on the management cluster.

- Physical worker servers with Redfish-compatible BMC, iDRAC, or iLO access are available.

- Network connectivity exists from the management cluster to the worker BMC interfaces.

- You have the BMC IP address and access credentials for each server.

- You have the MAC address of the management network interface for each server.

- You have the name of the root disk device for each server.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the following environment variables for the worker node:

    ``` terminal
    $ export BMC_IP=<bmc_ip_address>
    $ export BMC_USER=<bmc_username>
    $ export BMC_PASSWORD=<bmc_password>
    $ export WORKER_NAME=<worker_name>
    $ export BOOT_MAC=<management_interface_mac>
    $ export ROOT_DEVICE=<root_device_path>
    ```

    where:

    `<bmc_ip_address>`
    Specifies the IP address of the worker node BMC interface.

    `<bmc_username>`
    Specifies the username for BMC access.

    `<bmc_password>`
    Specifies the password for BMC access.

    `<worker_name>`
    Specifies a name for the worker node, such as `worker-01`.

    `<management_interface_mac>`
    Specifies the MAC address of the out-of-band management interface, such as `00:00:5E:00:53:01`.

    `<root_device_path>`
    Specifies the path to the root disk device, such as `/dev/nvme0n1`.

2.  Verify BMC connectivity from one of the control plane nodes:

    ``` terminal
    $ ping $BMC_IP
    ```

    ``` terminal
    $ curl -k https://$BMC_IP/redfish/v1/
    ```

    ``` terminal
    $ curl -k -u $BMC_USER:$BMC_PASSWORD https://$BMC_IP/redfish/v1/Systems
    ```

3.  Verify that the Bare Metal Operator is available:

    ``` terminal
    $ oc get clusteroperator baremetal
    ```

4.  Create a file named `provisioning.yaml` with the following content to disable the provisioning network:

    ``` yaml
    apiVersion: metal3.io/v1alpha1
    kind: Provisioning
    metadata:
      name: provisioning-configuration
    spec:
      provisioningNetwork: "Disabled"
      watchAllNamespaces: false
    ```

    > [!IMPORTANT]
    > When `provisioningNetwork` is set to `Disabled`, servers boot by using Redfish virtual media instead of PXE.

5.  Apply the `Provisioning` resource:

    ``` terminal
    $ oc apply -f provisioning.yaml
    ```

6.  Create a file named `bmc-secret.yaml` with the following content to store the BMC credentials:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: ${WORKER_NAME}-bmc-secret
      namespace: openshift-machine-api
    type: Opaque
    stringData:
      username: ${BMC_USER}
      password: ${BMC_PASSWORD}
    ```

7.  Apply the BMC credentials secret:

    ``` terminal
    $ envsubst < bmc-secret.yaml | oc apply -f -
    ```

8.  Create a file named `baremetalhost.yaml`. The `userData` secret determines the node type:

    - For a DPU-equipped worker node, reference the `worker-dpu-user-data-managed` secret:

      ``` yaml
      apiVersion: metal3.io/v1alpha1
      kind: BareMetalHost
      metadata:
        name: ${WORKER_NAME}
        namespace: openshift-machine-api
      spec:
        online: true
        bootMACAddress: ${BOOT_MAC}
        rootDeviceHints:
          deviceName: ${ROOT_DEVICE}
        bmc:
          address: redfish-virtualmedia+https://${BMC_IP}
          credentialsName: ${WORKER_NAME}-bmc-secret
          disableCertificateVerification: true
        customDeploy:
          method: install_coreos
        userData:
          name: worker-dpu-user-data-managed
          namespace: openshift-machine-api
      ```

    - For a regular worker node without a DPU, reference the `worker-user-data-managed` secret instead:

      ``` yaml
      apiVersion: metal3.io/v1alpha1
      kind: BareMetalHost
      metadata:
        name: ${WORKER_NAME}
        namespace: openshift-machine-api
      spec:
        online: true
        bootMACAddress: ${BOOT_MAC}
        rootDeviceHints:
          deviceName: ${ROOT_DEVICE}
        bmc:
          address: redfish-virtualmedia+https://${BMC_IP}
          credentialsName: ${WORKER_NAME}-bmc-secret
          disableCertificateVerification: true
        customDeploy:
          method: install_coreos
        userData:
          name: worker-user-data-managed
          namespace: openshift-machine-api
      ```

      > [!IMPORTANT]
      > Adding a regular worker node without a DPU is a Technology Preview feature.

9.  Apply the `BareMetalHost` resource:

    ``` terminal
    $ envsubst < baremetalhost.yaml | oc apply -f -
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Monitor the provisioning progress:

  ``` terminal
  $ oc get bmh -n openshift-machine-api -w
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME        STATE          CONSUMER   ONLINE   ERROR   AGE
  worker-01   registering               true             10s
  worker-01   inspecting                true             15s
  worker-01   preparing                 true             20s
  worker-01   available                 true             30s
  worker-01   provisioning              true             1m
  worker-01   provisioned               true             10m
  ```

  </div>

</div>

# Approve worker node CSRs

You must approve the pending certificate signing requests (CSRs) for worker nodes that join the management cluster.

> [!NOTE]
> Worker nodes provisioned by using a `BareMetalHost` resource do not have an associated `Machine` object, so the default OpenShift machine approver does not automatically approve their certificate signing requests (CSRs). You must manually approve the `kube-apiserver-client-kubelet` CSR from the `node-bootstrapper` service account and the `kubelet-serving` CSR from the node for each worker node.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the management cluster as a user with the `cluster-admin` role.

- You have installed the `oc` CLI.

- Worker nodes are booted and attempting to join the management cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Watch for pending CSRs:

    ``` terminal
    $ oc get csr -w
    ```

2.  Approve all pending CSRs:

    ``` terminal
    $ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs oc adm certificate approve
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    certificatesigningrequest.certificates.k8s.io/csr-27bgq approved
    certificatesigningrequest.certificates.k8s.io/csr-69g65 approved
    certificatesigningrequest.certificates.k8s.io/csr-7r862 approved
    certificatesigningrequest.certificates.k8s.io/csr-f5vk7 approved
    ```

    </div>

    Repeat this step until no pending CSRs remain. Each node typically generates multiple CSRs.

3.  Verify that the worker nodes joined the cluster:

    ``` terminal
    $ oc get nodes
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME               STATUS     ROLES                         AGE     VERSION
    host-worker1       NotReady   worker                        68s     v1.35.6
    host-worker2       NotReady   worker                        75s     v1.35.6
    master-0           Ready      control-plane,master,worker   4d22h   v1.35.6
    master-1           Ready      control-plane,master,worker   4d21h   v1.35.6
    master-2           Ready      control-plane,master,worker   4d22h   v1.35.6
    ```

    </div>

    > [!NOTE]
    > The worker nodes show a status of `NotReady` until the DPU provisioning process is fully completed and all OVN-Kubernetes CNI components on the host and the DPU are running. Do not proceed to the next steps until all pending CSRs are approved.

</div>

# Verify DPU provisioning

After the worker nodes join the management cluster, the `DPUSet` controller automatically detects nodes with the `feature.node.kubernetes.io/dpu-enabled` label, which the Node Feature Discovery Operator applies to DPU-equipped nodes. The controller then creates a `DPU` object for each node and starts the provisioning process. You can monitor the provisioning stages to verify progress.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the management cluster as a user with the `cluster-admin` role.

- You have installed the `oc` CLI.

- The worker node CSRs are approved and the nodes have joined the management cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Watch for `DPU` object creation:

    ``` terminal
    $ oc get dpu -n dpf-operator-system -w
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                     READY   OPERATIONAL   PHASE                        AGE
    <node-name>-<dpu-id>             Unknown       Node Effect                  25s
    <node-name>-<dpu-id>             Unknown       Initialize Interface         26s
    <node-name>-<dpu-id>             Unknown       Config FW Parameters         28s
    <node-name>-<dpu-id>             Unknown       Prepare BFB                  28s
    <node-name>-<dpu-id>             Unknown       OS Installing                5m28s
    <node-name>-<dpu-id>             Unknown       DPU Config                   15m
    <node-name>-<dpu-id>             Unknown       Rebooting                    26m
    <node-name>-<dpu-id>             Unknown       Host Network Configuration   27m
    <node-name>-<dpu-id>             False         DPU Cluster Config           64m
    <node-name>-<dpu-id>             Unknown       Node Effect Removal          71m
    <node-name>-<dpu-id>     True    True          Ready                        71m
    ```

    </div>

    The `DPU` objects progress through the following provisioning stages:

    `Initializing`
    The `DPU` object is created.

    `OS Installing`
    The BFB installation is in progress.

    `Rebooting`
    The host and DPU are resetting.

    `DPU Cluster Config`
    The DPU Kubernetes node join procedure is in progress. DPU CSRs are automatically approved by the DPF HCP Provisioner Operator.

    `Host Network Configuration`
    Networking configuration adjustments are applied on the host.

    `Ready`
    The DPU is successfully provisioned and ready to use.

    `Error`
    Provisioning failed. Check events and conditions for details.

    > [!IMPORTANT]
    > When the provisioning stage reaches `DPU Cluster Config`, proceed to "Configure authorization for the hosted cluster" to complete the DPU node join process.

2.  Monitor detailed provisioning progress:

    ``` terminal
    $ oc -n dpf-operator-system exec deploy/dpf-operator-controller-manager -- /dpfctl describe dpudeployments
    ```

3.  Optional: View detailed status for a specific `DPU` object:

    In the following command, replace `<dpu_name>` with the name of the `DPU` resource:

    ``` terminal
    $ oc describe dpu -n dpf-operator-system <dpu_name>
    ```

4.  Optional: Follow the provisioning controller logs for a specific DPU:

    In the following command, replace `<dpu_name>` with the name of the `DPU` resource:

    ``` terminal
    $ oc logs -n dpf-operator-system -l dpu.nvidia.com/component=dpf-provisioning-controller-manager --tail=-1 -f | grep <dpu_name>
    ```

</div>

# Configure authorization for the hosted cluster

DPF services running on DPU nodes require privileged access to host networking and devices. You must create a `ClusterRoleBinding` on the hosted cluster that grants the `privileged` security context constraint (SCC) to all service accounts in the `dpf-operator-system` namespace.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the hosted cluster as a user with the `cluster-admin` role.

- You have installed the `oc` CLI.

- The hosted cluster kubeconfig file is available.

- DPU provisioning has reached the `DPU Cluster Config` stage.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Get the hosted cluster kubeconfig:

    ``` terminal
    $ oc get secret $HOSTED_CLUSTER_NAME-admin-kubeconfig -n $CLUSTERS_NAMESPACE -o jsonpath='{.data.kubeconfig}' | base64 -d > $HOSTED_CLUSTER_NAME.kubeconfig
    ```

2.  Switch to the hosted cluster context:

    ``` terminal
    $ export KUBECONFIG="$(pwd)/$HOSTED_CLUSTER_NAME.kubeconfig"
    ```

3.  Create a file named `dpu-cluster-scc.yaml` with the following content:

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: dpf-system-scc-privileged
      labels:
        app.kubernetes.io/component: rbac
        app.kubernetes.io/part-of: dpu-services
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: system:openshift:scc:privileged
    subjects:
    - kind: Group
      apiGroup: rbac.authorization.k8s.io
      name: system:serviceaccounts:dpf-operator-system
    ```

4.  Apply the resource file on the hosted cluster:

    ``` terminal
    $ oc apply -f dpu-cluster-scc.yaml
    ```

</div>

# Verify full system readiness

After the DPU provisioning process completes, you can verify that all worker nodes, SR-IOV virtual functions, and DPU services are operational on the management cluster.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the management cluster as a user with the `cluster-admin` role.

- You have installed the `oc` CLI.

- DPU provisioning has completed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Switch back to the management cluster context:

    ``` terminal
    $ export KUBECONFIG="$(pwd)/mgmt-kubeconfig"
    ```

2.  Verify that all worker nodes are in a `Ready` state:

    ``` terminal
    $ oc get nodes
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME               STATUS   ROLES                         AGE     VERSION
    host-worker1       Ready    worker                        57m     v1.35.6
    host-worker2       Ready    worker                        57m     v1.35.6
    master-0           Ready    control-plane,master,worker   4d23h   v1.35.6
    master-1           Ready    control-plane,master,worker   4d22h   v1.35.6
    master-2           Ready    control-plane,master,worker   4d23h   v1.35.6
    ```

    </div>

3.  Verify that SR-IOV virtual functions are registered as Kubernetes node resources on the worker nodes:

    ``` terminal
    $ oc get nodes -l 'node-role.kubernetes.io/worker,!node-role.kubernetes.io/control-plane' -o json | \
      jq '.items[] | {name: .metadata.name, capacity: .status.capacity."openshift.io/bf3_vfs", allocatable: .status.allocatable."openshift.io/bf3_vfs"}'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    {
      "name": "host-worker1",
      "capacity": "90",
      "allocatable": "90"
    }
    {
      "name": "host-worker2",
      "capacity": "90",
      "allocatable": "90"
    }
    ```

    </div>

4.  Verify that all DPU services are in a `Success` phase:

    ``` terminal
    $ oc get dpuservices -n dpf-operator-system
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                            READY   PHASE     AGE
    doca-telemetry-service-7s8pb    True    Success   42m
    flannel                         True    Success   26h
    hbn-gffmv                       True    Success   25m
    kube-state-metrics-rbac         True    Success   4h10m
    node-problem-detector           True    Success   4h10m
    nvidia-k8s-ipam-node            True    Success   4h10m
    ovn-f49zx                       True    Success   17m
    ovs-cni                         True    Success   26h
    servicechainset-rbac-and-crds   True    Success   138m
    sfc-controller                  True    Success   26h
    sriov-device-plugin             True    Success   26h
    ```

    </div>

5.  Optional: View detailed DPU service status:

    ``` terminal
    $ oc -n dpf-operator-system exec deploy/dpf-operator-controller-manager -- /dpfctl describe all --show-resources=dpuservice --grouping=false
    ```

</div>
