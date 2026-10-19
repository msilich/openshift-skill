<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The DPF HCP Provisioner Operator automates the creation and lifecycle management of a hosted control plane cluster for DPU nodes.

# DPU hosted cluster provisioning with the DPF HCP Provisioner Operator

The DPF HCP Provisioner Operator abstracts hosted control plane complexity for DPF by orchestrating the full lifecycle of hosted clusters for DPU environments. The Operator treats the hosted control plane as a black box and maintains a 1:1:1 relationship: each `DPFHCPProvisioner` custom resource maps to exactly one `DPUCluster` and one `HostedCluster`.

The Operator provides the following capabilities:

HostedCluster lifecycle management
Creates, updates, and deletes `HostedCluster`, `NodePool`, and associated secret resources.

Automatic CSR approval
Approves Certificate Signing Requests from DPU worker nodes joining the hosted cluster.

BlueField OpenShift Container Platform layer image lookup
Matches OpenShift Container Platform release images to corresponding BlueField container images by using container registry tag lookup.

Kubeconfig provisioning
Extracts the hosted cluster admin kubeconfig, stores it in a secret, and sets the `spec.kubeconfig` field of the `DPUCluster` custom resource to reference that secret, enabling the management cluster to communicate with the DPU hosted cluster.

MetalLB configuration
Deploys `IPAddressPool` and `L2Advertisement` resources for `LoadBalancer` service exposure.

Ignition generation
Generates BlueField-specific ignition configurations from hosted control plane ignition for DPU node provisioning.

Status translation
Mirrors `HostedCluster` conditions to `DPFHCPProvisioner` status without exposing hosted control plane internals.

# Install the DPF HCP Provisioner Operator

You can install the DPF HCP Provisioner Operator by using a Helm chart. The operator manages the lifecycle of hosted clusters for DPU environments.

<div>

<div class="title">

Prerequisites

</div>

- The Multicluster Engine (MCE) Operator is installed and hosted control plane is enabled.

- The MetalLB Operator is installed and a `MetalLB` instance is created.

- A storage class is available for etcd persistent volumes, such as LVM Storage or an equivalent.

- The DPF Operator is installed and DPF CRDs are available.

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

2.  Install the operator by using Helm:

    ``` terminal
    $ helm upgrade --install dpf-hcp-provisioner-operator \
        oci://registry.redhat.io/dpu-kit-for-nvidia/dpf-hcp-provisioner-chart \
        --registry-config "${OPENSHIFT_PULL_SECRET}" \
        --version 4.22.0 \
        --namespace dpf-hcp-provisioner-system \
        --create-namespace \
        --set provisionerConfig.manageDPUServiceTemplates=true
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME: dpf-hcp-provisioner-operator
    LAST DEPLOYED: ...
    NAMESPACE: dpf-hcp-provisioner-system
    STATUS: deployed
    ```

    </div>

    > [!NOTE]
    > The Helm chart creates a `DPFHCPProvisionerConfig` singleton custom resource named `default` that defines the Operator-wide configuration. This resource controls settings such as the BlueField OpenShift Container Platform layer image repository, MetalLB integration, and `DPUServiceTemplate` management. To customize these settings, modify the `provisionerConfig` section in your Helm `values.yaml` file before running the `helm upgrade --install` command.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the Operator pod is running:

  ``` terminal
  $ oc get pods -n dpf-hcp-provisioner-system
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                                            READY   STATUS    RESTARTS   AGE
  dpf-hcp-provisioner-operator-xxx-yyy            1/1     Running   0          1m
  ```

  </div>

- Verify that the `DPFHCPProvisionerConfig` singleton resource was created and that `manageDPUServiceTemplates` is set to `true`:

  ``` terminal
  $ oc get dpfhcpprovisionerconfigs.provisioning.dpu.hcp.io default -o yaml
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` yaml
  apiVersion: provisioning.dpu.hcp.io/v1alpha1
  kind: DPFHCPProvisionerConfig
  metadata:
    name: default
    labels:
      app.kubernetes.io/managed-by: Helm
      helm.sh/chart: dpf-hcp-provisioner-chart-4.22.0
  spec:
    blueFieldOCPLayerRepo: registry.redhat.io/dpu-kit-for-nvidia/bluefield-ocp-layer-rhel10
    disableMetalLB: false
    manageDPUServiceTemplates: true
  ```

  </div>

  where:

  `blueFieldOCPLayerRepo`
  The container registry repository for BlueField OpenShift Container Platform layer images. The operator queries this repository for an image tag that matches the OpenShift Container Platform version.

  `disableMetalLB`
  Disables MetalLB configuration even when a virtual IP is specified.

  `manageDPUServiceTemplates`
  Controls whether the operator creates and manages the `DPUServiceTemplate` resources for OVN-Kubernetes, DTS, and HBN in the `DPUCluster` namespace. This value must be `true` otherwise DPU provisioning fails because the required `DPUServiceTemplate` resources are missing. This field is deprecated and will be removed in a future release, at which point `DPUServiceTemplate` management is always enabled.

</div>

# Hosted cluster provisioning environment variables

The following environment variables are used throughout the hosted cluster provisioning procedures. These environment variables must be set before you create secrets, the `DPUCluster` resource, or the `DPFHCPProvisioner` resource.

| Variable | Description | Example value |
|----|----|----|
| `HOSTED_CLUSTER_NAME` | The name of the hosted DPU cluster. | `dpf-hosted` |
| `OPENSHIFT_VERSION` | The OpenShift Container Platform version for the hosted cluster. | `4.22.7` |
| `CLUSTERS_NAMESPACE` | The namespace where hosted cluster resources are created. | `clusters` |
| `BASE_DOMAIN` | The base DNS domain for the hosted cluster. | `example.com` |
| `ETCD_STORAGE_CLASS` | The storage class used for etcd persistent volume claims. | `lvms-vg1` |
| `OCP_RELEASE_IMAGE` | The OpenShift Container Platform release image for the hosted cluster. Derived from `OPENSHIFT_VERSION`. | `quay.io/openshift-release-dev/ocp-release:4.22.7-multi` |
| `PULL_SECRET_NAME` | The name of the Kubernetes secret that contains the pull secret for the hosted cluster. | `pull-secret` |
| `OPENSHIFT_PULL_SECRET` | The file path to the pull secret JSON file on your workstation. | `/root/pull-secret.txt` |
| `SSH_KEY_SECRET_NAME` | The name of the Kubernetes secret that contains the SSH public key for the hosted cluster. | `ssh-key` |
| `SSH_KEY` | The file path to the SSH public key file on your workstation. Use ed25519 keys for better security. | `/root/.ssh/id_ed25519.pub` |
| `HOSTED_CLUSTER_VIP` | The virtual IP address for the hosted cluster API server, allocated from the management cluster subnet. | `192.168.1.200` |

Hosted cluster provisioning environment variables

You must set the following environment variables in your terminal session before you proceed.

``` terminal
$ export HOSTED_CLUSTER_NAME="dpf-hosted"
$ export OPENSHIFT_VERSION="4.22.7"
$ export CLUSTERS_NAMESPACE="clusters"
$ export BASE_DOMAIN="example.com"
$ export ETCD_STORAGE_CLASS="lvms-vg1"
$ export OCP_RELEASE_IMAGE="quay.io/openshift-release-dev/ocp-release:${OPENSHIFT_VERSION}-multi"
$ export PULL_SECRET_NAME="my-pull-secret"
$ export OPENSHIFT_PULL_SECRET="/root/pull-secret.txt"
$ export SSH_KEY_SECRET_NAME="my-ssh-key"
$ export SSH_KEY="/root/.ssh/id_ed25519.pub"
$ export HOSTED_CLUSTER_VIP="192.168.1.200"
$ export DPU_HOST_CIDR="10.0.110.0/24"
$ export VTEP_CIDR="10.0.120.0/22"
$ export NODES_MTU="1500"      # Use 1500 for standard MTU, 9000 for jumbo frames
$ export FLANNEL_POD_CIDR="10.132.0.0/14"
```

# Create secrets for the hosted cluster

You must create a pull secret and an SSH key secret in the clusters namespace before provisioning the hosted cluster. The `DPFHCPProvisioner` resource references these secrets during hosted cluster creation.

> [!NOTE]
> The BlueField OpenShift Container Platform layer image that the Operator resolves automatically might require authentication to the Quay or Red Hat registry. Ensure that the pull secret includes credentials for that image registry.

<div>

<div class="title">

Prerequisites

</div>

- You have set the environment variables described in "Hosted cluster provisioning environment variables".

- You have a valid OpenShift Container Platform pull secret file at the path specified by `OPENSHIFT_PULL_SECRET`.

- You have an SSH public key file at the path specified by `SSH_KEY`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the clusters namespace:

    ``` terminal
    $ oc create namespace $CLUSTERS_NAMESPACE
    ```

2.  Create the pull secret:

    ``` terminal
    $ oc create secret generic $PULL_SECRET_NAME \
        --from-file=.dockerconfigjson=$OPENSHIFT_PULL_SECRET \
        --type=kubernetes.io/dockerconfigjson \
        -n $CLUSTERS_NAMESPACE
    ```

3.  Create the SSH key secret:

    ``` terminal
    $ oc create secret generic $SSH_KEY_SECRET_NAME \
        --from-file=id_rsa.pub=$SSH_KEY \
        --type=Opaque \
        -n $CLUSTERS_NAMESPACE
    ```

    > [!NOTE]
    > The `id_rsa.pub` secret data key is a fixed name that the provisioner expects and it does not require an RSA key. The `SSH_KEY` variable can point to any supported public key file, such as an Ed25519 key.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the secrets were created in the clusters namespace:

  ``` terminal
  $ oc get secrets -n $CLUSTERS_NAMESPACE
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME             TYPE     DATA   AGE
  my-pull-secret   Opaque   1      10s
  my-ssh-key       Opaque   1      5s
  ```

  </div>

</div>

# Create the DPUCluster custom resource

The `DPUCluster` resource tells the DPF Operator about the hosted cluster where DPU services will run.

Do not set the `spec.kubeconfig` field. After you create the hosted cluster, the DPF HCP Provisioner Operator automatically creates the admin kubeconfig secret in the `dpf-operator-system` namespace and sets the `spec.kubeconfig` field of this resource to reference it.

<div>

<div class="title">

Prerequisites

</div>

- You have set the environment variables described in "Hosted cluster provisioning environment variables".

- You have installed the DPF Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `dpucluster.yaml` with the following content:

    ``` yaml
    apiVersion: provisioning.dpu.nvidia.com/v1alpha1
    kind: DPUCluster
    metadata:
      name: $HOSTED_CLUSTER_NAME
      namespace: dpf-operator-system
    spec:
      type: static
      maxNodes: 10
    ```

2.  Apply the resource with variable substitution:

    ``` terminal
    $ envsubst < dpucluster.yaml | oc apply -f -
    ```

</div>

# Create the DPFHCPProvisioner custom resource

The `DPFHCPProvisioner` custom resource triggers the creation of the complete hosted cluster infrastructure. This includes the `HostedCluster`, the MetalLB `IPAddressPool`, the `L2Advertisement`, and kubeconfig injection into the `DPUCluster`.

<div>

<div class="title">

Prerequisites

</div>

- You have set the environment variables described in "Hosted cluster provisioning environment variables".

- You have installed the DPF HCP Provisioner Operator and it is running.

- You have created the pull secret and SSH key secret in the clusters namespace.

- You have created the `DPUCluster` resource in the `dpf-operator-system` namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `dpfhcpprovisioner.yaml` with the following content:

    ``` yaml
    apiVersion: provisioning.dpu.hcp.io/v1alpha1
    kind: DPFHCPProvisioner
    metadata:
      name: $HOSTED_CLUSTER_NAME
      namespace: $CLUSTERS_NAMESPACE
    spec:
      baseDomain: $BASE_DOMAIN
      dpuClusterRef:
        name: $HOSTED_CLUSTER_NAME
        namespace: dpf-operator-system
      dpuDeploymentRef:
        name: dpudeployment
        namespace: dpf-operator-system
      etcdStorageClass: $ETCD_STORAGE_CLASS
      ocpReleaseImage: $OCP_RELEASE_IMAGE
      pullSecretRef:
        name: $PULL_SECRET_NAME
      sshKeySecretRef:
        name: $SSH_KEY_SECRET_NAME
      virtualIP: $HOSTED_CLUSTER_VIP
    ```

    where:

    `baseDomain`
    Specifies the base DNS domain for the hosted cluster.

    `dpuClusterRef`
    Specifies a reference to the `DPUCluster` resource that represents the DPU hosted cluster.

    `dpuDeploymentRef`
    Specifies a reference to the `DPUDeployment` resource in the `dpf-operator-system` namespace.

    `etcdStorageClass`
    Specifies the storage class for etcd persistent volume claims.

    `ocpReleaseImage`
    Specifies the OpenShift Container Platform release image for the hosted cluster.

    `pullSecretRef`
    Specifies the name of the pull secret in the same namespace.

    `sshKeySecretRef`
    Specifies the name of the SSH key secret in the same namespace.

    `virtualIP`
    Specifies the virtual IP address for the hosted cluster API server, allocated from the management cluster subnet.

    The following optional fields use working defaults and do not need to be specified unless you want to override them:

    `controlPlaneAvailabilityPolicy`
    Specifies the availability policy for the hosted cluster control plane. This optional parameter defaults to `HighlyAvailable`. Set it to `SingleReplica` for a single-node control plane, in which case `virtualIP` is not required.

    `flannelEnabled`
    Specifies whether to enable Flannel networking in the hosted cluster. This optional parameter defaults to `true`.

    `clusterNetwork`
    Specifies the pod network CIDR for the hosted cluster. This optional parameter defaults to `10.128.0.0/14`.

    `serviceNetwork`
    Specifies the service network CIDR for the hosted cluster. This optional parameter defaults to `172.30.0.0/16`.

    `machineNetwork`
    Specifies the machine network CIDR for the hosted cluster. This optional parameter uses the management cluster network by default.

    `nodeSelector`
    Specifies a node selector for scheduling the hosted control plane pods. This optional parameter uses default scheduling by default.

2.  Apply the resource with variable substitution:

    ``` terminal
    $ envsubst < dpfhcpprovisioner.yaml | oc apply -f -
    ```

</div>

# Verify hosted cluster creation

After creating the `DPFHCPProvisioner` resource, you can monitor its status to verify that the hosted cluster is provisioned and becomes ready. The provisioning process can take up to 30 minutes.

<div>

<div class="title">

Prerequisites

</div>

- You have created the `DPFHCPProvisioner` resource in the clusters namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Monitor the `DPFHCPProvisioner` status:

    ``` terminal
    $ oc get dpfhcpprovisioner -n ${CLUSTERS_NAMESPACE}
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME         PHASE          READY   HOSTEDCLUSTER   AGE
    dpf-hosted   Provisioning   False   dpf-hosted      2m
    ```

    </div>

2.  Wait for the `DPFHCPProvisioner` to reach the `Ready` phase:

    ``` terminal
    $ oc wait dpfhcpprovisioner ${HOSTED_CLUSTER_NAME} -n ${CLUSTERS_NAMESPACE} \
        --for=jsonpath='{.status.phase}'=Ready --timeout=30m
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    dpfhcpprovisioner.provisioning.dpu.hcp.io/dpf-hosted condition met
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

- Confirm that the `DPUCluster` is ready:

  ``` terminal
  $ oc get dpucluster ${HOSTED_CLUSTER_NAME} -n dpf-operator-system
  ```

  A `Ready` status indicates that the operator created the admin kubeconfig secret referenced by the `DPUCluster` resource and that the hosted cluster API is reachable, which is the prerequisite for DPU worker nodes to join:

- Confirm that the admin kubeconfig secret referenced by the `DPUCluster` was created in the `dpf-operator-system` namespace:

  ``` terminal
  $ oc get secret ${HOSTED_CLUSTER_NAME}-admin-kubeconfig -n dpf-operator-system
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                          TYPE     DATA   AGE
  dpf-hosted-admin-kubeconfig   Opaque   1      10m
  ```

  </div>

</div>

# Verify DPU service reconciliation

After the DPU hosted cluster and `DPUCluster` are ready, the DPF Operator creates the DPU services, IPAM pools, service interfaces, and service chains for the `DPUDeployment`.

These resources are created but will not be fully reconciled until DPU worker nodes are provisioned and joined to the cluster. For full verification of DPU service status, see "Verify full system readiness" after completing worker node provisioning.
