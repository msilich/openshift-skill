<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can diagnose and resolve common NVIDIA DPF Operator issues with DPU provisioning, hosted cluster readiness, networking, and collect diagnostic logs for support. These procedures complement the official NVIDIA debugging tools and guides.

# DPU provisioning does not start

If DPU provisioning does not start immediately after you add worker nodes to the management cluster, verify that certificate signing requests (CSRs), controller pods, Node Feature Discovery (NFD) labels, and DPF resource objects are in the correct state.

Verify that all worker CSRs are approved
Run the following command to list the CSR status on the management cluster:

``` terminal
$ oc get csr
```

Ensure that all CSRs for the worker nodes show an `Approved` status.

Verify that all DPF controller pods are running
Run the following command to check the status of the DPF Operator pods:

``` terminal
$ oc get pod -n dpf-operator-system
```

Ensure that all pods are in a `Running` state.

Verify that worker nodes are labeled for DPU provisioning by NFD
Run the following command to confirm that the `dpu-enabled` label is present on the worker nodes:

``` terminal
$ oc get nodes -l feature.node.kubernetes.io/dpu-enabled=""
```

The output lists the worker nodes that NFD has labeled for DPU provisioning. For example:

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
NAME           STATUS     ROLES               AGE   VERSION
host-worker1   NotReady   worker,worker-dpu   62s   v1.35.6
host-worker2   NotReady   worker,worker-dpu   66s   v1.35.6
```

</div>

Check BFB object status
Run the following command to verify that the BlueField Bootstream File (BFB) image is downloaded and ready:

``` terminal
$ oc describe bfb -n dpf-operator-system bf-bundle
```

Check the `status.conditions` field for download progress and any error messages.

Verify that the BFB image URL is reachable
If the BFB download fails, run the following command to confirm that the image URL is reachable, replacing `$BFB_URL` with the image URL:

``` terminal
$ curl -I $BFB_URL
```

Ensure that the response returns a `200 OK` status code. If the download fails, verify network connectivity to the image registry, check for firewall or proxy restrictions, and ensure that sufficient disk space is available on the node.

Monitor DPU provisioning progress
Run the following command to watch the DPU objects progress through provisioning:

``` terminal
$ oc get dpu -n dpf-operator-system -w
```

Wait for each DPU to progress from `Pending` to `Provisioning` to `Ready`.

Verify that the DPU hardware is detected on the worker node
Open a debug shell on the worker node:

``` terminal
$ oc debug node/<worker-node-name>
```

Inside the debug shell, run the following commands to confirm that a BlueField device is present:

``` terminal
sh-5.1# chroot /host
```

``` terminal
sh-5.1# lspci | grep -i mellanox
```

If the DPU is not listed, verify that it is properly seated in the PCIe slot and that it is not disabled in the server BIOS.

Verify DPU firmware and software compatibility
Inside the debug shell, run the following command to check the DPU firmware version:

``` terminal
sh-5.1# mlxfwmanager --query
```

Confirm that the BlueField firmware and DOCA software versions on the DPU are compatible with the DPF Operator version that you deployed.

Check `DPUDeployment` object status
Inspect the `DPUDeployment` object for information about the following resources:

- BFB object state

- `DPUServiceTemplate` objects state

- `DPUServiceConfiguration` objects state

Run the following command to view the full `DPUDeployment` status:

``` terminal
$ oc get dpudeployments -n dpf-operator-system dpudeployment -o yaml
```

Alternatively, run the following `dpfctl` command for a summarized view:

``` terminal
$ oc -n dpf-operator-system exec deploy/dpf-operator-controller-manager -- /dpfctl describe dpudeployments
```

# DPU objects remain in the `DPU Cluster Config` state

If DPU objects remain in a `DPU Cluster Config` state and do not progress, the hosted cluster might have pending certificate signing requests (CSRs) that must be approved.

Check for pending CSRs in the hosted cluster
Switch to the hosted cluster context and check for any pending CSRs:

``` terminal
$ export KUBECONFIG=<path_to_hosted_cluster_kubeconfig>
```

``` terminal
$ oc get csr
```

Review the output and approve any CSRs that show a `Pending` status.

# Management cluster nodes do not become ready

If management cluster nodes do not reach a `Ready` state after DPU provisioning completes, the OVN-Kubernetes CNI pods might not be running correctly on the management cluster or the hosted cluster.

Check OVN-Kubernetes pods on the management cluster
Switch to the management cluster context and verify that all OVN-Kubernetes pods are running on the x86_64 worker nodes and control plane nodes:

``` terminal
$ export KUBECONFIG=<path_to_management_cluster_kubeconfig>
```

``` terminal
$ oc get pods -n openshift-ovn-kubernetes -o wide
```

Check OVN-Kubernetes pods on the hosted cluster
Switch to the hosted cluster context and verify that all OVN-Kubernetes pods are running on the DPU workers:

``` terminal
$ export KUBECONFIG=<path_to_hosted_cluster_kubeconfig>
```

``` terminal
$ oc get pods -n openshift-ovn-kubernetes -o wide
```

Ensure that all pods in the `openshift-ovn-kubernetes` namespace are in a `Running` state on both clusters.

# DPU provisioning fails with BMC certificate errors

If DPU provisioning fails with certificate errors when you add worker nodes by using the Bare Metal Operator, the baseboard management controller (BMC) certificates might be untrusted or expired, or the `BareMetalHost` credentials might be incorrect.

Verify BMC certificate validity
Run the following command to inspect the BMC TLS certificate, replacing `<bmc_ip>` with the BMC IP address and `<bmc_hostname>` with the BMC hostname:

``` terminal
$ openssl s_client -connect <bmc_ip>:443 -servername <bmc_hostname>
```

Update the certificates in the BMC configuration if they are expired or untrusted.

Verify BareMetalHost BMC credentials
Ensure that the `BareMetalHost` resource references the correct BMC secret and connection details, including the Redfish address and credentials for the worker server.

# Worker node CSR approval fails

If certificate signing request (CSR) approval for worker nodes fails, network connectivity between the management cluster and the DPU or hosted cluster path might be incomplete.

Check Host-Based Networking pods on worker nodes
Run the following command to verify that HBN pods are running:

``` terminal
$ oc get pods -n openshift-hbn -o wide
```

Verify DPU management network connectivity
From a management cluster node, ping the DPU management IP address:

``` terminal
$ ping <dpu_management_ip>
```

Verify the `br-ex` bridge on worker nodes
Confirm that the `br-ex` bridge that the worker `MachineConfig` resource creates is present and that required firewall rules allow traffic on the DPU management and high-speed networks.

# DPU nodes remain NotReady in the hosted cluster

If DPU nodes remain in a `NotReady` state in the hosted cluster, DPU provisioning might be incomplete, or the DPU firmware and DOCA software versions might be incompatible with the DPF Operator version.

Check DPU and DPU service status on the management cluster
Run the following commands:

``` terminal
$ oc get dpu -n dpf-operator-system
```

``` terminal
$ oc get dpuservice -n dpf-operator-system
```

Verify node status in the hosted cluster
Switch to the hosted cluster kubeconfig and list the nodes:

``` terminal
$ export KUBECONFIG=<path_to_hosted_cluster_kubeconfig>
```

``` terminal
$ oc get nodes
```

Check DPF Operator and related pod logs
On the management cluster, inspect logs from DPF-related pods for provisioning or networking errors:

``` terminal
$ oc logs -n dpf-operator-system <dpu_related_pod_name>
```

Verify firmware and software compatibility
Confirm that the BlueField firmware and DOCA software versions on the DPU are compatible with the DPF Operator version that you deployed.

# Troubleshoot hosted cluster issues

You can diagnose and resolve DPU hosted cluster issues, including CSR approval failures, kubeconfig access problems, and worker node join failures.

<div>

<div class="title">

Prerequisites

</div>

- The DPF HCP Provisioner is installed and configured.

- DPU provisioning has completed on the management cluster.

- You have access to kubeconfig files for both the management cluster and the hosted cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that the hosted cluster is accessible by running the following commands:

    ``` terminal
    $ export KUBECONFIG=/path/to/hosted-cluster.kubeconfig
    ```

    ``` terminal
    $ oc cluster-info
    ```

    If the hosted cluster API server is not accessible, check the hosted control plane status on the management cluster.

2.  Switch to the management cluster context and verify that the hosted control plane components are running:

    ``` terminal
    $ export KUBECONFIG=/path/to/management-cluster.kubeconfig
    ```

    ``` terminal
    $ oc get pods -n clusters-$HOSTED_CLUSTER_NAME
    ```

    Verify that the `etcd`, `kube-apiserver`, `kube-controller-manager`, and `kube-scheduler` pods are all in a `Running` state.

3.  Check the DPF HCP Provisioner status for any error conditions:

    ``` terminal
    $ oc get dpfhcpprovisioner -n dpf-operator-system -o yaml
    ```

    Review the `status.conditions` field for any conditions that indicate a failure.

4.  Return to the hosted cluster context and check for pending CSRs:

    ``` terminal
    $ export KUBECONFIG=/path/to/hosted-cluster.kubeconfig
    ```

    ``` terminal
    $ oc get csr --sort-by=.metadata.creationTimestamp
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME        AGE   SIGNERNAME                                    REQUESTOR                  CONDITION
    csr-abc12   30s   kubernetes.io/kubelet-serving                 system:node:dpu-worker1    Pending
    csr-def34   25s   kubernetes.io/kube-apiserver-client-kubelet   system:bootstrap:abc123    Pending
    ```

    </div>

5.  Approve any pending CSRs. To approve a single CSR, run the following command, replacing `<csr-name>` with the CSR name:

    ``` terminal
    $ oc adm certificate approve <csr-name>
    ```

    To approve all pending CSRs in a single command, run:

    ``` terminal
    $ oc get csr -o name | xargs oc adm certificate approve
    ```

6.  Verify that the DPU workers are joining the hosted cluster:

    ``` terminal
    $ oc get nodes
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                 STATUS   ROLES    AGE   VERSION
    dpu-worker1          Ready    worker   5m    v1.35.6
    dpu-worker2          Ready    worker   5m    v1.35.6
    ```

    </div>

7.  If nodes are not joining, check whether the bootstrap token is still valid by running the following command on the hosted cluster:

    ``` terminal
    $ oc get secrets -n kube-system | grep bootstrap-token
    ```

    Bootstrap tokens have a limited lifetime. The DPF HCP Provisioner should create new tokens automatically. If tokens are expired and not being renewed, check the provisioner logs for errors.

8.  Check the kubelet logs on the DPU for authentication or certificate errors. Switch to the management cluster context and open a debug shell on the DPU-enabled worker node:

    ``` terminal
    $ export KUBECONFIG=/path/to/management-cluster.kubeconfig
    ```

    ``` terminal
    $ oc debug node/<dpu-enabled-worker-node>
    ```

    Inside the debug shell, run the following commands to stream the kubelet logs:

    ``` terminal
    sh-5.1# chroot /host
    ```

    ``` terminal
    sh-5.1# journalctl -u kubelet -f
    ```

    Look for authentication errors or certificate-related failures in the log output.

9.  Verify that OVN-Kubernetes is running correctly on the hosted cluster. Switch to the hosted cluster context and run the following command:

    ``` terminal
    $ export KUBECONFIG=/path/to/hosted-cluster.kubeconfig
    ```

    ``` terminal
    $ oc get pods -n openshift-ovn-kubernetes -o wide
    ```

    Ensure that OVN-Kubernetes pods are running on the DPU ARM cores.

</div>

<div class="formalpara">

<div class="title">

Troubleshooting

</div>

**CSR approval failures**: Verify that the DPF HCP Provisioner has the required RBAC permissions to approve CSRs, check the provisioner logs for certificate-related errors, and ensure that the cluster CA is configured correctly.

</div>

**Node join failures**: Verify that the bootstrap kubeconfig was correctly generated by the provisioner, check network connectivity between the DPUs and the hosted control plane API server, and ensure that the kubelet configuration includes the correct API server endpoint.

**Control plane access issues**: Verify that the hosted cluster virtual IP address is configured and accessible, check the `LoadBalancer` service status for the hosted API server, and ensure that MetalLB is correctly configured and announcing the VIP.

**Network connectivity problems**: Verify the VTEP network configuration between DPUs, check that the DPU high-speed network interfaces are operational, and ensure that the required ports are open for inter-DPU communication.

# Troubleshoot DPF networking issues

You can diagnose and resolve DPF networking issues, including OVN-Kubernetes configuration problems, MTU mismatches, and connectivity failures.

<div>

<div class="title">

Prerequisites

</div>

- DPU provisioning completed successfully.

- The hosted cluster is accessible with DPU worker nodes joined.

- You have access to both management and hosted cluster contexts.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify OVN-Kubernetes pod status on the management cluster:

    ``` terminal
    $ export KUBECONFIG=/path/to/management-cluster.kubeconfig
    ```

    ``` terminal
    $ oc get pods -n openshift-ovn-kubernetes -o wide
    ```

    Check that the following pods are running:

    - `ovnkube-control-plane-*` pods are running on control plane nodes only.

    - `ovnkube-node-*` pods are running on all nodes.

    - `ovs-node-*` pods are running on all nodes.

2.  Check OVN-Kubernetes configuration on the hosted cluster:

    ``` terminal
    $ export KUBECONFIG=/path/to/hosted-cluster.kubeconfig
    ```

    ``` terminal
    $ oc get pods -n openshift-ovn-kubernetes -o wide
    ```

    Verify that OVN-Kubernetes pods are running on DPU ARM cores, not on host x86 CPUs.

3.  Verify the network MTU configuration:

    ``` terminal
    $ oc get network.operator.openshift.io cluster -o yaml | grep -A 5 defaultNetwork
    ```

    Check the following MTU values:

    - Standard networks: MTU 1400 for pods, 1500 for nodes.

    - Jumbo frame networks: MTU 8940 for pods, 9000 for nodes.

4.  Test basic pod-to-pod connectivity:

    ``` terminal
    $ export KUBECONFIG=/path/to/hosted-cluster.kubeconfig
    ```

    ``` terminal
    $ oc run test-pod-1 --image=nicolaka/netshoot --rm -it -- /bin/bash
    ```

    From another terminal, run:

    ``` terminal
    $ oc run test-pod-2 --image=nicolaka/netshoot --rm -it -- /bin/bash
    ```

    Test connectivity between the pods by using cluster IP addresses.

5.  Check VTEP network configuration:

    ``` terminal
    $ export KUBECONFIG=/path/to/management-cluster.kubeconfig
    ```

    ``` terminal
    $ oc debug node/<dpu-enabled-worker-node>
    ```

    In the debug shell, run:

    ``` terminal
    $ chroot /host
    ```

    ``` terminal
    $ ip addr show | grep $VTEP_CIDR
    ```

    Verify that VTEP interfaces are configured with the correct IP addresses from the `VTEP_CIDR` range.

6.  Test VTEP connectivity:

    ``` terminal
    $ ping -c 4 <other-dpu-vtep-ip>
    ```

    If the ping fails, check routing and firewall rules between DPU nodes.

7.  Verify OVN database connectivity:

    ``` terminal
    $ export KUBECONFIG=/path/to/hosted-cluster.kubeconfig
    ```

    ``` terminal
    $ oc exec -n openshift-ovn-kubernetes <ovnkube-node-pod> -- ovn-nbctl show
    ```

    The output should display the OVN logical network topology.

8.  Check OVN-Kubernetes log errors:

    ``` terminal
    $ oc logs -n openshift-ovn-kubernetes <ovnkube-node-pod> -c ovn-controller
    ```

    Look for the following error types:

    - Database connectivity issues

    - Port binding failures

    - Flow programming errors

9.  Verify service mesh connectivity:

    ``` terminal
    $ export KUBECONFIG=/path/to/hosted-cluster.kubeconfig
    ```

    ``` terminal
    $ oc create service clusterip test-svc --tcp=80:80
    ```

    ``` terminal
    $ oc run test-client --image=nicolaka/netshoot --rm -it -- nc -vz test-svc 80
    ```

    A successful connection indicates that service traffic is flowing through the DPU data plane.

10. Check the SR-IOV network device plugin:

    ``` terminal
    $ export KUBECONFIG=/path/to/management-cluster.kubeconfig
    ```

    ``` terminal
    $ oc get sriovnetworknodepolicy -n openshift-sriov-network-operator
    ```

    Verify that SR-IOV policies are correctly applied to DPU-enabled worker nodes.

</div>

<div class="formalpara">

<div class="title">

Troubleshooting

</div>

**OVN-Kubernetes pod failures**

</div>

Check that the OVN Helm chart version is compatible with your OpenShift Container Platform version. Verify that the CNI configuration matches the DPU acceleration requirements. Ensure that OVN databases are accessible from the DPU worker nodes.

**MTU mismatch issues**

Verify that all network components use consistent MTU values. Check that the physical network infrastructure supports the configured MTU. Update MTU values if the network environment has changed.

**VTEP connectivity problems**

Verify that the VTEP CIDR does not conflict with existing network ranges. Check that routing is configured between DPU nodes. Ensure that firewalls allow VTEP traffic on the required ports.

**Service connectivity failures**

Verify that kube-proxy is correctly configured on DPU nodes. Check that iptables rules are correctly programmed. Ensure that DPU acceleration is correctly handling service traffic.

**SR-IOV configuration issues**

Verify that the SR-IOV Operator is compatible with the DPU firmware. Check that the VF count matches the configured value. Ensure that VFs are correctly allocated to the correct namespaces.

# DPF diagnostic commands and log collection

You can run diagnostic commands and collect logs to investigate DPF component status, DPU provisioning failures, and hosted cluster issues when troubleshooting or opening support cases.

## Quick status overview commands

The following commands provide a quick overview of DPF component status:

<div class="formalpara">

<div class="title">

DPF resource status

</div>

``` terminal
$ oc get dpudeployment,dpuservicetemplate,dpuserviceconfiguration,bfb,dpu -n dpf-operator-system
```

</div>

<div class="formalpara">

<div class="title">

DPF Operator pod status

</div>

``` terminal
$ oc get pods -n dpf-operator-system -l app.kubernetes.io/part-of=dpf-operator
```

</div>

<div class="formalpara">

<div class="title">

DPU-enabled worker node status

</div>

``` terminal
$ oc get nodes -l feature.node.kubernetes.io/dpu-enabled="" \
  -o custom-columns=NAME:.metadata.name,STATUS:.status.conditions[?(@.type=="Ready")].status,AGE:.metadata.creationTimestamp
```

</div>

<div class="formalpara">

<div class="title">

Hosted cluster status (if using HCP Provisioner)

</div>

``` terminal
$ oc get hostedcluster -n clusters-$HOSTED_CLUSTER_NAME
```

</div>

\+

``` terminal
$ oc get nodepool -n clusters-$HOSTED_CLUSTER_NAME
```

## Detailed diagnostic commands

<div class="formalpara">

<div class="title">

DPU provisioning status

</div>

``` terminal
$ oc describe dpu -n dpf-operator-system
```

</div>

\+

``` terminal
$ oc describe bfb -n dpf-operator-system bf-bundle
```

<div class="formalpara">

<div class="title">

DPF Operator configuration

</div>

``` terminal
$ oc get dpfoperatorconfig -n dpf-operator-system -o yaml
```

</div>

<div class="formalpara">

<div class="title">

Service template and configuration status

</div>

``` terminal
$ oc describe dpuservicetemplate -n dpf-operator-system
```

</div>

\+

``` terminal
$ oc describe dpuserviceconfiguration -n dpf-operator-system
```

<div class="formalpara">

<div class="title">

DPU service status

</div>

``` terminal
$ oc get dpuservice -n dpf-operator-system -o wide
```

</div>

\+

``` terminal
$ oc describe dpuservice -n dpf-operator-system
```

<div class="formalpara">

<div class="title">

Node Feature Discovery status

</div>

``` terminal
$ oc get nodefeaturerule -n openshift-nfd
```

</div>

\+

``` terminal
$ oc describe node <worker-node> | grep -A 20 "Labels:"
```

## Log collection commands

<div class="formalpara">

<div class="title">

DPF Operator logs

</div>

``` terminal
$ oc logs -n dpf-operator-system -l app.kubernetes.io/name=dpf-operator --tail=200 > dpf-operator.log
```

</div>

<div class="formalpara">

<div class="title">

HCP Provisioner logs (if using hosted clusters)

</div>

``` terminal
$ oc logs -n dpf-operator-system -l app.kubernetes.io/name=dpfhcp-provisioner-operator --tail=200 > dpfhcp-provisioner.log
```

</div>

<div class="formalpara">

<div class="title">

Worker node kubelet logs

</div>

``` terminal
$ oc debug node/<dpu-worker-node>
```

</div>

\+ In the debug shell, run:

\+

``` terminal
$ chroot /host
```

\+

``` terminal
$ journalctl -u kubelet --since "1 hour ago" > kubelet.log
```

<div class="formalpara">

<div class="title">

OVN-Kubernetes logs

</div>

``` terminal
$ oc logs -n openshift-ovn-kubernetes -l app=ovnkube-node --tail=100 > ovn-kubernetes.log
```

</div>

<div class="formalpara">

<div class="title">

SR-IOV Network Operator logs

</div>

``` terminal
$ oc logs -n openshift-sriov-network-operator -l app=sriov-network-operator --tail=100 > sriov-operator.log
```

</div>

<div class="formalpara">

<div class="title">

Node Feature Discovery logs

</div>

``` terminal
$ oc logs -n openshift-nfd -l app=nfd-worker --tail=100 > nfd.log
```

</div>

## System information collection

<div class="formalpara">

<div class="title">

Hardware information

</div>

``` terminal
$ oc debug node/<dpu-worker-node>
```

</div>

\+ In the debug shell, run:

\+

``` terminal
$ lspci | grep -i mellanox
```

\+

``` terminal
$ lshw -class network
```

\+

``` terminal
$ dmidecode -t system
```

<div class="formalpara">

<div class="title">

DPU firmware information

</div>

``` terminal
$ mlxfwmanager --query
```

</div>

\+

``` terminal
$ mst status
```

<div class="formalpara">

<div class="title">

Network interface information

</div>

``` terminal
$ ip addr show
```

</div>

\+

``` terminal
$ ip route show
```

\+

``` terminal
$ ethtool -i <interface>
```

## Performance monitoring commands

<div class="formalpara">

<div class="title">

DPU service metrics

</div>

``` terminal
$ oc exec -n dpf-operator-system <dts-service-pod> -- \
  curl -s localhost:9189/metrics | grep -E "(current_link_speed|p[01]_eth_)"
```

</div>

<div class="formalpara">

<div class="title">

Container resource usage

</div>

``` terminal
$ oc adm top pods -n dpf-operator-system --containers
```

</div>

\+

``` terminal
$ oc adm top nodes -l feature.node.kubernetes.io/dpu-enabled=""
```

## Support information package

When opening a support case, collect the following information:

**Environment information**

- OpenShift Container Platform cluster version and build

- DPF Operator version and configuration

- Hardware specifications (server model, DPU model, firmware versions)

- Network topology and configuration

**Configuration files**

- DPF Operator configuration (`dpfoperatorconfig`)

- Service templates and configurations

- Network policies and configurations

- Environment variables used during installation

**Log files**

- DPF Operator logs (past 24 hours)

- Worker node system logs (past 4 hours)

- Kubernetes event logs related to DPF resources

- Application logs for affected services

## Common log analysis patterns

Look for the following patterns in logs when troubleshooting:

**DPU provisioning issues**:

- `Error downloading BFB image`

- `Failed to detect DPU hardware`

- `Provisioning timeout exceeded`

**Networking issues**:

- `OVN database connection failed`

- `Failed to program flows`

- `Interface binding failed`

**Service deployment issues**:

- `Image pull failed`

- `Insufficient resources`

- `ConfigMap not found`

**Authentication issues**:

- `Certificate signing request denied`

- `Unauthorized access to API server`

- `Token validation failed`

# Additional resources

- [DOCA Platform Framework troubleshooting documentation](https://networking-docs.nvidia.com/dpf/26.4.1/troubleshooting)
