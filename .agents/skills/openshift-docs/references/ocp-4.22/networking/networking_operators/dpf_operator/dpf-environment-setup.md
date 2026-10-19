<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before installing the NVIDIA DPF Operator, you must set up the management cluster, configure worker nodes, and install and configure the required Operators.

# Set up the management cluster

The management cluster is a standard OpenShift Container Platform 4.22 cluster installed by using the Assisted Installer. This cluster hosts the DPF Operators and the hosted control planes for managing the hosted cluster on DPUs.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the [Red Hat Hybrid Cloud Console](https://console.redhat.com/openshift/create).

- You have the OpenShift CLI (`oc`) installed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Go to the [Red Hat Hybrid Cloud Console cluster creation page](https://console.redhat.com/openshift/create) and create a cluster with control-plane nodes only. Select **Data center** → **Assisted Installer**.

2.  Optional: Configure jumbo MTU for each control plane node.

    1.  Under **Hosts' network configuration** in the Assisted Installer wizard, select **Static IP, bridges, and bonds**.

    2.  Set the **Static network configurations** section per node according to the following template, using the relevant MAC address and interface name for each node:

        ``` yaml
        interfaces:
          - ipv4:
              dhcp: true
              enabled: true
            mac-address: <xx:xx:xx:xx:xx:xx>
            mtu: 1500 # Set to 1500 for standard MTU or 9000 for jumbo frames
            name: <interface-name>
            state: up
            type: ethernet
        ```

        <div class="note">

        <div class="title">

        </div>

        - You can alternatively configure MTU allocation on the DHCP server that allocates IPs to the control plane nodes.

        - If virtual machines are used for control-plane nodes, the MTU must be set on the bridge of the hypervisor used by the VMs.

        - When using MTU 9000, ensure the switch ports that connect the cluster’s control-plane nodes are set to handle jumbo frames.

        </div>

3.  Select the following operators to install with the cluster:

    - **Storage** → **Logical Volume Manager Storage**

    - **Platform Operations & Lifecycle** → **MultiCluster Engine**

    - **Scheduling** → **Node Feature Discovery**

4.  Click **Add hosts** to add hosts to the cluster. Only control plane nodes are required at this stage.

5.  After the installation completes, download the `KUBECONFIG` file and save it as `mgmt-kubeconfig`.

</div>

<div>

<div class="title">

Verification

</div>

1.  Set the `KUBECONFIG` environment variable:

    ``` terminal
    $ export KUBECONFIG="$(pwd)/mgmt-kubeconfig"
    ```

2.  Verify that all nodes are in a `Ready` state:

    ``` terminal
    $ oc get nodes
    ```

</div>

# Configure worker nodes for DPU operation

You must deploy the `dpu-worker-config` Helm chart to configure worker nodes with DPUs before adding those nodes to the management cluster. The `dpu-worker-config` Helm chart creates the `MachineConfigPool`, `dpu-worker-configuration` MachineConfig, and other required resources that configure the bridge, OVS services, and IP routing on worker nodes. The `MachineConfigPool` groups DPU-equipped worker nodes so that the Machine Config Operator can apply DPU-specific configurations to them.

The MachineConfig resource performs several configuration tasks required by DPF:

- **Bridge Configuration**: Creates a `br-ex` bridge interface that enables communication between the DPU and the hosted cluster control plane running on the management cluster. This name must match the `dpuNodeOOBBridgeName` value in the `DPFOperatorConfig` resource, or DPU provisioning fails. For more information refer to [DPF Operator Prerequisites](https://networking-docs.nvidia.com/dpf/26.4.1/host-network-configuration-prerequisites).

- **OVS Service Management**: Disables OpenShift’s default OVS services on x86 worker nodes. This is required for OVN-Kubernetes DPU Host mode operation, where networking functions are offloaded to the DPU rather than running on the host CPU.

- **IP Rules Configuration**: Sets routing rules required for pod-to-host control-plane traffic.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

- The Helm CLI (`helm`) is installed on your workstation.

- You have a pull secret file that includes credentials for `registry.redhat.io`. Helm reads its registry credentials from this file, which is separate from the container runtime configuration.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the `OPENSHIFT_PULL_SECRET` environment variable to the path of your pull secret file:

    ``` terminal
    $ export OPENSHIFT_PULL_SECRET="/root/pull-secret.txt"
    ```

2.  Deploy the `dpu-worker-config` Helm chart:

    ``` terminal
    $ helm upgrade --install dpu-worker-config \
        oci://registry.redhat.io/dpu-kit-for-nvidia/dpu-worker-config-chart \
        --version 4.22.0 \
        --registry-config "${OPENSHIFT_PULL_SECRET}" \
        --namespace dpf-hcp-provisioner-system \
        --create-namespace \
        --disable-openapi-validation
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the `dpu-worker-config` Helm release is deployed:

  ``` terminal
  $ helm list -n dpf-hcp-provisioner-system
  ```

- Verify that the `MachineConfigPool` was created automatically:

  ``` terminal
  $ oc get mcp worker-dpu
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME         CONFIG                                                 UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
  worker-dpu   rendered-worker-dpu-b4a44cc606c2ffcf07067d1e943a8758   True      False      False      0              0                   0                     0                      2m
  ```

  </div>

- Verify that the `dpu-worker-configuration` MachineConfig is created:

  ``` terminal
  $ oc get machineconfig dpu-worker-configuration
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                       GENERATEDBYCONTROLLER   IGNITIONVERSION   AGE
  dpu-worker-configuration                           3.2.0             2m
  ```

  </div>

</div>

> [!NOTE]
> The Machine Config Operator automatically reboots worker nodes to apply DPU-specific configurations after nodes with the `worker-dpu` label are added to the cluster.

# Create the DPF namespace

You must create a dedicated namespace for the DPF Operator and its components before installing the Operator.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- Create the `dpf-operator-system` namespace:

  ``` terminal
  $ oc create namespace dpf-operator-system
  ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the namespace was created:

  ``` terminal
  $ oc get namespace dpf-operator-system
  ```

</div>

# Required Operators

Before you install the DPF Operator, you must install the cert-manager Operator for Red Hat OpenShift, MetalLB Operator, Red Hat OpenShift GitOps, and NVIDIA Maintenance Operator.

The multicluster engine Operator and the Node Feature Discovery Operator can be installed during management cluster creation by using the Assisted Installer. If you did not install the multicluster engine Operator, follow "Install the multicluster engine Operator" before configuring the required Operators.

## Install the multicluster engine Operator

If you did not install the multicluster engine Operator by using the Assisted Installer, install it from the OpenShift CLI. You do not need to install Red Hat Advanced Cluster Management or create a `MultiClusterHub` resource to use the multicluster engine Operator. If the Assisted Installer already created a `MultiClusterEngine` resource, skip this procedure.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the management cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

- No `MultiClusterEngine` resource exists on the cluster.

- If you already have an existing `MultiClusterEngine` resource with a different name, note that the following verification commands use `mce`. Substitute your resource’s name where needed.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check which multicluster engine channels are available from the `redhat-operators` catalog:

    ``` terminal
    $ oc get packagemanifests -n openshift-marketplace -l catalog=redhat-operators \
      -o jsonpath='{.items[?(@.metadata.name=="multicluster-engine")].status.channels[*].name}{"\n"}'
    ```

    The following example uses `stable-2.17`, which is the channel used by this deployment. If your catalog does not offer this channel, select a supported channel for your OpenShift version before continuing.

2.  Create a file named `mce-operator.yaml` with the following content:

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: multicluster-engine
    ---
    apiVersion: operators.coreos.com/v1
    kind: OperatorGroup
    metadata:
      name: multicluster-engine
      namespace: multicluster-engine
    spec:
      targetNamespaces:
      - multicluster-engine
    ---
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: multicluster-engine
      namespace: multicluster-engine
    spec:
      channel: stable-2.17
      name: multicluster-engine
      source: redhat-operators
      sourceNamespace: openshift-marketplace
      installPlanApproval: Automatic
    ```

    If you selected a different supported channel, replace `stable-2.17` with that channel in the file.

3.  Apply the file:

    ``` terminal
    $ oc apply -f mce-operator.yaml
    ```

4.  Wait until the multicluster engine Operator CSV reports `Succeeded` and the `MultiClusterEngine` CRD is established:

    ``` terminal
    $ oc get csv -n multicluster-engine
    $ oc wait crd/multiclusterengines.multicluster.openshift.io --for=create --timeout=10m
    $ oc wait crd/multiclusterengines.multicluster.openshift.io --for=condition=Established --timeout=5m
    ```

    Repeat the CSV check until its phase is `Succeeded` before creating the custom resource.

5.  Create a file named `mce.yaml` with the following content:

    ``` yaml
    apiVersion: multicluster.openshift.io/v1
    kind: MultiClusterEngine
    metadata:
      name: mce
    spec:
      overrides:
        components:
        - name: hypershift
          enabled: true
    ```

6.  Apply the file:

    ``` terminal
    $ oc apply -f mce.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Wait for the `MultiClusterEngine` resource to become available:

  ``` terminal
  $ oc wait multiclusterengine/mce --for=jsonpath='{.status.phase}'=Available --timeout=15m
  ```

- Verify that the hosted control plane component is enabled:

  ``` terminal
  $ oc get multiclusterengine mce -o jsonpath='{.spec.overrides.components[?(@.name=="hypershift")].enabled}{"\n"}'
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  true
  ```

  </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Installing the multicluster engine Operator while connected online](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/clusters/cluster_mce_overview#installing-while-connected-online-mce)

</div>

## Install the cert-manager Operator

The cert-manager Operator for Red Hat OpenShift manages TLS certificates for DPF components. You install this operator by using the OpenShift CLI.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `cert-manager-operator.yaml` with the following content:

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cert-manager
    ---
    apiVersion: operators.coreos.com/v1
    kind: OperatorGroup
    metadata:
      name: openshift-cert-manager-operator
      namespace: cert-manager
    spec:
      targetNamespaces:
      - cert-manager
    ---
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: openshift-cert-manager-operator
      namespace: cert-manager
    spec:
      channel: stable-v1
      name: openshift-cert-manager-operator
      source: redhat-operators
      sourceNamespace: openshift-marketplace
    ```

2.  Apply the file:

    ``` terminal
    $ oc apply -f cert-manager-operator.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the Operator is installed:

  ``` terminal
  $ oc get pods -n cert-manager
  ```

</div>

## Install the MetalLB Operator

The MetalLB Operator provides load balancing services for DPF components on the management cluster. You install this operator by using the OpenShift CLI.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `metallb-operator.yaml` with the following content:

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: metallb-system
    ---
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: metallb-operator
      namespace: openshift-operators
    spec:
      channel: "stable"
      name: metallb-operator
      source: redhat-operators
      sourceNamespace: openshift-marketplace
      installPlanApproval: Automatic
      config:
        # Tolerate the taint on the master nodes
        tolerations:
        - key: "node-role.kubernetes.io/control-plane"
          operator: "Exists"
          effect: "NoSchedule"
        # Force scheduling only on nodes with the control-plane label
        affinity:
          nodeAffinity:
            requiredDuringSchedulingIgnoredDuringExecution:
              nodeSelectorTerms:
              - matchExpressions:
                - key: "node-role.kubernetes.io/control-plane"
                  operator: "Exists"
    ```

2.  Apply the file:

    ``` terminal
    $ oc apply -f metallb-operator.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Wait for the MetalLB custom resource definition to be created and established before configuring MetalLB:

  ``` terminal
  $ oc wait crd/metallbs.metallb.io --for=create --timeout=10m
  $ oc wait crd/metallbs.metallb.io --for=condition=Established --timeout=5m
  ```

</div>

## Install the GitOps Operator

The Red Hat OpenShift GitOps manages DPF service deployments and configurations using GitOps principles. You install this operator by using the OpenShift CLI.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `gitops-operator.yaml` with the following content:

    ``` yaml
    apiVersion: v1
    kind: Namespace
    metadata:
      name: openshift-gitops-operator
      labels:
        openshift.io/cluster-monitoring: "true"
    ---
    apiVersion: operators.coreos.com/v1
    kind: OperatorGroup
    metadata:
      name: openshift-gitops-operator
      namespace: openshift-gitops-operator
    spec:
      upgradeStrategy: Default
    ---
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: openshift-gitops-operator
      namespace: openshift-gitops-operator
    spec:
      channel: gitops-1.21
      config:
        env:
        - name: ARGOCD_CLUSTER_CONFIG_NAMESPACES
          value: "openshift-gitops,dpf-operator-system"
        - name: CONTROLLER_CLUSTER_ROLE
          value: "cluster-admin"
        - name: SERVER_CLUSTER_ROLE
          value: "cluster-admin"
      installPlanApproval: Automatic
      name: openshift-gitops-operator
      source: redhat-operators
      sourceNamespace: openshift-marketplace
    ```

2.  Apply the file:

    ``` terminal
    $ oc apply -f gitops-operator.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Wait for the Argo CD custom resource definition to be created and established before creating an `ArgoCD` resource:

  ``` terminal
  $ oc wait crd/argocds.argoproj.io --for=create --timeout=10m
  $ oc wait crd/argocds.argoproj.io --for=condition=Established --timeout=5m
  ```

</div>

## Install the NVIDIA Maintenance Operator

The NVIDIA Maintenance Operator assists in performing maintenance tasks and gracefully draining DPU worker nodes. You install this operator by using Helm.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

- You have installed the Helm CLI (`helm`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a Helm values file named `maintenance-operator-values.yaml` with the following content:

    ``` yaml
    operatorConfig:
      maxParallelOperations: 60%
    operator:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                  - key: "node-role.kubernetes.io/master"
                    operator: Exists
              - matchExpressions:
                  - key: "node-role.kubernetes.io/control-plane"
                    operator: Exists
      tolerations:
        - key: node-role.kubernetes.io/master
          operator: Exists
          effect: NoSchedule
        - key: node-role.kubernetes.io/control-plane
          operator: Exists
          effect: NoSchedule
    ```

2.  Install the Operator by using Helm:

    ``` terminal
    $ helm upgrade --install maintenance-operator oci://ghcr.io/mellanox/maintenance-operator-chart \
      --namespace dpf-operator-system \
      --create-namespace \
      --disable-openapi-validation \
      --version 0.3.0 \
      --values maintenance-operator-values.yaml \
      --wait
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the Operator pod is running:

  ``` terminal
  $ oc get pods -n dpf-operator-system
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [DPF Operator prerequisites](https://networking-docs.nvidia.com/dpf/26.4.1/host-network-configuration-prerequisites)

</div>

# Configure the required Operators

After the required Operators are installed, configure Node Feature Discovery, MetalLB, GitOps, and Cluster Network Operator for the DPF environment. This procedure also verifies that the multicluster engine and hosted control plane components are ready.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

- You have installed the cert-manager Operator for Red Hat OpenShift, MetalLB Operator, Red Hat OpenShift GitOps, and NVIDIA Maintenance Operator.

- You have installed the Logical Volume Manager Storage Operator, multicluster engine Operator, and the Node Feature Discovery Operator. You can install them by using the Assisted Installer during cluster creation. If you did not install the multicluster engine Operator, follow "Install the multicluster engine Operator" before continuing.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Define the cluster variables:

    ``` terminal
    $ export CLUSTER_NAME="doca-mgmt"
    $ export BASE_DOMAIN="example.com"
    $ export HOST_CLUSTER_API="api.${CLUSTER_NAME}.${BASE_DOMAIN}"
    ```

    where:

    `CLUSTER_NAME`
    Specifies the management cluster name.

    `BASE_DOMAIN`
    Specifies the management cluster base domain.

    `HOST_CLUSTER_API`
    Specifies the management cluster API endpoint.

2.  Create a file named `nfd-instance.yaml` with the following `NodeFeatureDiscovery` resource definition:

    ``` yaml
    apiVersion: nfd.openshift.io/v1
    kind: NodeFeatureDiscovery
    metadata:
      name: nfd-instance
      namespace: openshift-nfd
    spec:
      operand:
        workerEnvs:
          - name: KUBERNETES_SERVICE_HOST
            value: $HOST_CLUSTER_API
          - name: KUBERNETES_SERVICE_PORT
            value: "6443"
      workerConfig:
        configData: |
          sources:
            pci:
              deviceClassWhitelist:
                - "0200"
                - "03"
                - "12"
                - "0207"
              deviceLabelFields:
                - "vendor"
                - "device"
                - "class"
    ```

3.  Apply the file by using `envsubst` to substitute the environment variables:

    ``` terminal
    $ envsubst < nfd-instance.yaml | oc apply -f -
    ```

4.  Create a file named `nfd-rule.yaml` with the following `NodeFeatureRule` resource definition:

    ``` yaml
    apiVersion: nfd.openshift.io/v1alpha1
    kind: NodeFeatureRule
    metadata:
      name: dpu-detection-rule
      namespace: openshift-nfd
    spec:
      rules:
        - labels:
            dpu-enabled: ""
          matchFeatures:
            - feature: pci.device
              matchExpressions:
                device:
                  op: In
                  value:
                    - a2d6
                    - a2dc
                vendor:
                  op: In
                  value:
                    - 15b3
          name: DPU-detection-rule
    ```

5.  Apply the file:

    ``` terminal
    $ oc apply -f nfd-rule.yaml
    ```

6.  Create a file named `metallb-config.yaml` with the following `MetalLB` resource definition:

    ``` yaml
    apiVersion: metallb.io/v1beta1
    kind: MetalLB
    metadata:
      name: metallb
      namespace: openshift-operators
    spec:
      nodeSelector:
        node-role.kubernetes.io/control-plane: ""
      speakerTolerations:
        - key: node-role.kubernetes.io/control-plane
          operator: Exists
          effect: NoSchedule
    ```

7.  Apply the MetalLB resource file:

    ``` terminal
    $ oc apply -f metallb-config.yaml
    ```

8.  Create a file named `argocd-instance.yaml` with the following `ArgoCD` resource definition:

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: argocd
      namespace: dpf-operator-system
    spec:
      nodePlacement:
        nodeSelector:
          node-role.kubernetes.io/control-plane: ""
        tolerations:
        - key: node-role.kubernetes.io/master
          operator: Exists
          effect: NoSchedule
        - key: node-role.kubernetes.io/control-plane
          operator: Exists
          effect: NoSchedule
      server:
        route:
          enabled: true
      controller: {}
      repo: {}
      applicationSet:
        enabled: false
      resourceExclusions: |
        - apiGroups:
          - packages.operators.coreos.com
          kinds:
          - PackageManifest
      sso:
        provider: dex
        dex:
          openShiftOAuth: true
      notifications:
        enabled: false
    ```

9.  Apply the Argo CD file:

    ``` terminal
    $ oc apply -f argocd-instance.yaml
    ```

10. Wait for the ArgoCD Redis deployment to be ready:

    ``` terminal
    $ oc wait deployment argocd-redis -n dpf-operator-system \
      --for=condition=Available --timeout=120s
    ```

11. Enable global IP forwarding on the OVN-Kubernetes configuration:

    This command enables IP packet forwarding between different networks managed by OVN-Kubernetes.

    ``` terminal
    $ oc patch network.operator.openshift.io cluster --type=merge -p \
      '{"spec":{"defaultNetwork":{"ovnKubernetesConfig":{"gatewayConfig":{"ipForwarding":"Global"}}}}}'
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the `MultiClusterEngine` instance is created:

  ``` terminal
  $ oc get multiclusterengine mce
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME   STATUS      AGE     CURRENTVERSION   DESIREDVERSION   MESSAGE
  mce    Available   4m58s   2.17.2           2.17.2           All components available
  ```

  </div>

- Verify that the hosted control plane component is enabled:

  ``` terminal
  $ oc get multiclusterengine mce -o jsonpath='{.spec.overrides.components[?(@.name=="hypershift")].enabled}{"\n"}'
  ```

  > [!NOTE]
  > The manual installation procedure creates `mce` with `hypershift` enabled. If the previous command returns `true`, no further action is needed. If it returns `false` or an empty result, you must enable the `hypershift` component before DPU provisioning can succeed.

  To enable the `hypershift` component on the `MultiClusterEngine` resource, use the following steps. In current multicluster engine Operator versions the component is named `hypershift`. Earlier versions use `hypershift-preview`.

  - If the result is empty, check whether the `components` list exists:

    ``` terminal
    $ oc get multiclusterengine mce -o jsonpath='{.spec.overrides.components}{"\n"}'
    ```

    If the list exists but has no `hypershift` entry, append it without replacing the other components:

    ``` terminal
    $ oc patch multiclusterengine mce --type=json \
        -p='[{"op":"add","path":"/spec/overrides/components/-","value":{"name":"hypershift","enabled":true}}]'
    ```

    If the list is absent, edit the resource instead and create `spec.overrides.components` with an entry named `hypershift` set to `enabled: true`.

  - If the result is `false`, an entry exists but is disabled. Edit the resource and set the `hypershift` component to `enabled: true`:

    ``` terminal
    $ oc edit multiclusterengine mce
    ```

    > [!IMPORTANT]
    > Do not use `oc patch --type=merge` to enable the component, because a merge patch replaces the entire `components` array and removes the other components. Use the JSON `add` patch only when the `components` list exists. Otherwise, use `oc edit`.

- Verify that the `NodeFeatureDiscovery` instance and `NodeFeatureRule` are configured:

  ``` terminal
  $ oc get nodefeaturediscovery,nodefeaturerule -n openshift-nfd
  ```

- Verify that the `MetalLB` instance was created:

  ``` terminal
  $ oc get metallb -n openshift-operators
  ```

- Verify that the Argo CD pods are running:

  ``` terminal
  $ oc get pods -n dpf-operator-system | grep argocd
  ```

- Verify that IP forwarding is set to `Global`:

  ``` terminal
  $ oc get network.operator.openshift.io cluster -o jsonpath='{.spec.defaultNetwork.ovnKubernetesConfig.gatewayConfig.ipForwarding}'
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  Global
  ```

  </div>

</div>
