<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To ensure that virtual machines (VMs) recover automatically when a node fails, configure node health checks, automated remediation, and capacity planning. These recommendations come from chaos testing results and help minimize VM downtime during node failure conditions.

# How node health monitoring protects virtual machines

By default, virtual machines (VMs) are not automatically recovered to other available nodes when a node fails. To minimize VM downtime and ensure workload resilience, configure node health monitoring and automated remediation.

Without the Node Health Check Operator and a remediation Operator such as Self Node Remediation (SNR) or Fence Agents Remediation (FAR), VMs experience downtime until the node recovers. Apply the following configurations to ensure your workloads are resilient under node failure conditions:

- Configure VMs with `runStrategy: Always` to allow recovery to other available nodes.

- Deploy and configure the Node Health Check Operator to monitor node status changes and trigger automated remediation.

- Configure a remediation operator, such as SNR or FAR, to recover workloads from failed nodes.

- Plan node capacity to ensure that enough resources are available to host VMs that migrate from failed nodes.

## Configuring a VM run strategy by using the CLI

You can configure a run strategy for a virtual machine (VM) by using the command line. The run strategy controls whether a VM automatically restarts after disruptions such as node failures or maintenance events.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- Edit the `VirtualMachine` resource by running the following command:

  ``` terminal
  $ oc edit vm <vm_name> -n <namespace>
  ```

  Example run strategy:

  ``` yaml
  apiVersion: kubevirt.io/v1
  kind: VirtualMachine
  spec:
    runStrategy: Always
  # ...
  ```

</div>

# Configuring node health checks for virtual machines

You can configure the Node Health Check Operator to monitor node status and trigger automated remediation when a node becomes unhealthy.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Node Health Check Operator.

- You have installed a remediation operator.

- You have cluster administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `NodeHealthCheck` custom resource (CR) to define the health check criteria and remediation strategy:

    ``` yaml
    apiVersion: remediation.medik8s.io/v1alpha1
    kind: NodeHealthCheck
    metadata:
      name: nodehealthcheck-sample
    spec:
      minHealthy: <count>
      pauseRequests:
        - <pause_test_cluster>
      remediationTemplate:
        apiVersion: self-node-remediation.medik8s.io/v1alpha1
        name: self-node-remediation-automatic-strategy-template
        namespace: openshift-workload-availability
        kind: SelfNodeRemediationTemplate
      escalatingRemediations:
        - remediationTemplate:
            apiVersion: self-node-remediation.medik8s.io/v1alpha1
            name: self-node-remediation-resource-deletion-template
            namespace: openshift-workload-availability
            kind: SelfNodeRemediationTemplate
          order: 1
          timeout: 300s
      selector:
        matchExpressions:
          - key: node-role.kubernetes.io/worker
            operator: Exists
      unhealthyConditions:
        - type: Ready
          status: "False"
          duration: 30s
        - type: Ready
          status: Unknown
          duration: 30s
    ```

    where:

    - `spec.minHealthy` defines the number of worker nodes required to host VMs that migrate from failed nodes.

      - For critical environments, set this value to the minimum number of nodes that you require to maintain the cluster workload.

      - For hyperconverged storage, set this value to one less than your number of nodes to limit remediation to a single worker-node failure and maintain storage stability.

    - `spec.remediationTemplate` defines the remediation template to use when the Node Health Check Operator detects an unhealthy node. This example uses the Self Node Remediation Operator.

    - `spec.escalatingRemediations` defines escalating remediation strategies. If the initial remediation does not resolve the issue within the specified timeout, the next remediation strategy runs.

    - `spec.selector` defines the nodes to monitor. This example monitors all worker nodes.

    - `spec.unhealthyConditions` defines the parameters to identify an unhealthy node.

    - `spec.unhealthyConditions.duration` defines the duration that a condition must persist before remediation starts. Set lower values for faster recovery. The following table shows recommended values:

      | Environment  | Recommended duration |
      |--------------|----------------------|
      | Critical     | 30-60 seconds        |
      | Standard     | 60-180 seconds       |
      | Conservative | 180-360 seconds      |

      Recommended `unhealthyConditions` duration values

2.  Apply the `NodeHealthCheck` CR by running the following command:

    ``` terminal
    $ oc apply -f nodehealthcheck-sample.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the `NodeHealthCheck` CR exists by running the following command:

  ``` terminal
  $ oc get nodehealthcheck nodehealthcheck-sample
  ```

</div>

> [!TIP]
> If remediation does not trigger as expected, verify that the remediation Operator runs correctly, and check the `NodeHealthCheck` CR events for errors:
>
> ``` terminal
> $ oc describe nodehealthcheck nodehealthcheck-sample
> ```

# Node remediation strategies for OpenShift Virtualization

Use the best remediation strategy for your environment to ensure that virtual machine (VM) workloads recover automatically when nodes become unhealthy.

Self Node Remediation (SNR) and Fence Agents Remediation (FAR) are the recommended remediation Operators for OpenShift Virtualization environments. Recovery time depends on the number of VMs on the failed nodes.

Self Node Remediation (SNR)
Use for nodes that do not have a management interface, or when the management interface might be unreachable. SNR does not require a management interface to function. Do not use SNR for hyperconverged storage because API unavailability can cause remediation actions that negatively impact hyperconverged storage protection domains.

Fence Agents Remediation (FAR)
The fastest remediation Operator for workload recovery time. Use FAR when a baseboard management controller (BMC) interface is available. FAR requires a management interface that is reachable from the Kubernetes pod network.

You must use FAR for hyperconverged storage configurations. For hyperconverged storage, set the Node Health Check `minHealthy` property to your total node count minus one. With this setting, FAR does not remediate more than a single worker-node failure within the same zone, storage placement, and replication group to maintain storage stability.

<div class="note">

<div class="title">

</div>

- Remediation actions start after the node conditions monitored by the Node Health Check Operator exceed the time specified in `spec.unhealthyConditions[].duration`.

- Disruption to the node running the `self-node-remediation-controller-manager` pod increases recovery times.

</div>

## Self Node Remediation configuration parameters

You can tune the Self Node Remediation (SNR) Operator configuration to optimize recovery times and ensure availability of VM workloads.

SelfNodeRemediationTemplate strategies
The `SelfNodeRemediationTemplate` custom resource (CR) defines the remediation strategy to use when the Node Health Check Operator identifies a node as unhealthy. Configure the remediation strategy in a `SelfNodeRemediationTemplate` CR:

``` yaml
apiVersion: self-node-remediation.medik8s.io/v1alpha1
kind: SelfNodeRemediationTemplate
metadata:
  name: self-node-remediation-resource-deletion-template
  namespace: openshift-operators
spec:
  template:
    spec:
      remediationStrategy: ResourceDeletion
```

where:

- `spec.remediationStrategy` defines the remediation strategy. Use `ResourceDeletion` to delete pods and associated volume attachments on the unhealthy node. Use `OutOfServiceTaint` to place an `out-of-service` taint on the unhealthy node and delete pods and associated volume attachments. This strategy is faster than `ResourceDeletion`.

SelfNodeRemediationConfig parameters
The `SelfNodeRemediationConfig` CR defines the timing and connectivity parameters for the SNR Operator. Tuning these parameters based on your environment conditions helps ensure availability of workloads and prevents unnecessary remediation actions. Configure the timing and connectivity parameters in a `SelfNodeRemediationConfig` CR:

``` yaml
apiVersion: self-node-remediation.medik8s.io/v1alpha1
kind: SelfNodeRemediationConfig
metadata:
  name: self-node-remediation-config
  namespace: openshift-operators
spec:
  safeTimeToAssumeNodeRebootedSeconds: 180
  watchdogFilePath: /dev/watchdog
  isSoftwareRebootEnabled: true
  apiServerTimeout: 15s
  apiCheckInterval: 5s
  maxApiErrorThreshold: 3
  peerApiServerTimeout: 5s
  peerDialTimeout: 5s
  peerRequestTimeout: 5s
  peerUpdateInterval: 15m
```

where:

- `spec.safeTimeToAssumeNodeRebootedSeconds` defines the time in seconds to wait before assuming the node has rebooted. Set this value to the node reboot time plus 20% for faster recovery, or plus 40% for a more conservative approach.

# Capacity planning for VM failover

Plan node capacity to ensure your cluster has enough resources to host VMs that migrate from failed nodes.

When a node fails and you have enabled remediation, VMs automatically migrate to other available nodes in the cluster. Monitor the following resources on your cluster to ensure adequate capacity for VM failover:

- VM count per node

- Available CPU

- Available memory

- Available disk

- Available network bandwidth

Check the current resource use of your nodes:

``` terminal
$ oc adm top nodes
```

> [!NOTE]
> The number of VMs that a node can host depends on the `maxPods` value set in the kubelet configuration:
>
> ``` yaml
> kubeletConfig:
>   maxPods: 250
> ```

# Additional resources

- [Configure eviction and run strategies](../nodes/virt-eviction-strategies.md#virt-eviction-strategies)

- [Run strategies](../nodes/virt-eviction-strategies.md#virt-runstrategies-vms_virt-eviction-strategies)

- [About high availability for virtual machines](../managing_vms/advanced_vm_management/virt-high-availability-for-vms.md#virt-high-availability-for-vms)

- [Control virtual machine states](../managing_vms/virt-controlling-vm-states.md#virt-controlling-vm-states)

- [Workload Availability for Red Hat OpenShift](https://docs.redhat.com/en/documentation/workload_availability_for_red_hat_openshift/24.3)
