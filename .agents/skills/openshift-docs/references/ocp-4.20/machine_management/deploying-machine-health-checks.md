<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure and deploy a machine health check to automatically repair damaged machines in a machine pool.

> [!IMPORTANT]
> You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API.
>
> Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation.
>
> To view the platform type for your cluster, run the following command:
>
> ``` terminal
> $ oc get infrastructure cluster -o jsonpath='{.status.platform}'
> ```

# About machine health checks

You can use machine health checks to detect and remediate unhealthy machines automatically, limiting disruption to the targeted machine pool.

> [!NOTE]
> You can only apply a machine health check to machines that are managed by compute machine sets or control plane machine sets.

To monitor machine health, create a resource to define the configuration for a controller. Set a condition to check, such as staying in the `NotReady` status for five minutes or displaying a permanent condition in the node-problem-detector, and a label for the set of machines to monitor.

The controller that observes a `MachineHealthCheck` resource checks for the defined condition. If a machine fails the health check, the machine is automatically deleted and one is created to take its place. When a machine is deleted, you see a `machine deleted` event.

To limit disruptive impact of the machine deletion, the controller drains and deletes only one node at a time. If there are more unhealthy machines than the `maxUnhealthy` threshold allows for in the targeted pool of machines, remediation stops and therefore enables manual intervention.

> [!NOTE]
> Consider the timeouts carefully, accounting for workloads and requirements.
>
> - Long timeouts can result in long periods of downtime for the workload on the unhealthy machine.
>
> - Too short timeouts can result in a remediation loop. For example, the timeout for checking the `NotReady` status must be long enough to allow the machine to complete the startup process.

To stop the check, remove the resource.

## Limitations when deploying machine health checks

There are limitations to consider before deploying a machine health check:

- Only machines owned by a machine set are remediated by a machine health check.

- If the node for a machine is removed from the cluster, a machine health check considers the machine to be unhealthy and remediates it immediately.

- If the corresponding node for a machine does not join the cluster after the `nodeStartupTimeout`, the machine is remediated.

- A machine is remediated immediately if the `Machine` resource phase is `Failed`.

<div>

<div class="title">

Additional resources

</div>

- [About listing all the nodes in a cluster](../nodes/nodes/nodes-nodes-viewing.md#nodes-nodes-viewing-listing_nodes-nodes-viewing)

- [Short-circuiting machine health check remediation](deploying-machine-health-checks.md#machine-health-checks-short-circuiting_deploying-machine-health-checks)

- [About the Control Plane Machine Set Operator](control_plane_machine_management/cpmso-about.md#cpmso-about)

</div>

# About the MachineHealthCheck custom resource

You control how a machine health check remediates unhealthy machines by using a `MachineHealthCheck` custom resource (CR) to configure health criteria, remediation limits, and startup timeouts for machines in a targeted pool.

The `MachineHealthCheck` resource for all cloud-based installation types, and other than bare metal, resembles the following YAML file:

``` yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineHealthCheck
metadata:
  name: example
  namespace: openshift-machine-api
spec:
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-machine-role: <role>
      machine.openshift.io/cluster-api-machine-type: <role>
      machine.openshift.io/cluster-api-machineset: <cluster_name>-<label>-<zone>
  unhealthyConditions:
  - type:    "Ready"
    timeout: "300s"
    status: "False"
  - type:    "Ready"
    timeout: "300s"
    status: "Unknown"
  maxUnhealthy: "40%"
  nodeStartupTimeout: "10m"
```

where:

`metadata.name`
Specifies the name of the machine health check to deploy.

`spec.selector.matchLabels`
Specifies the machine pool and machine set to check by adding labels:

- `machine.openshift.io/cluster-api-machine-role`: Specifies a label for the machine pool that you want to check.

- `machine.openshift.io/cluster-api-machine-type`: Specifies a label for the machine pool that you want to check.

- `machine.openshift.io/cluster-api-machineset`: Specifies the machine set to track in the `<cluster_name>-<label>-<zone>` format. For example, `prod-node-us-east-1a`.

`spec.unhealthyConditions.timeout`
Specifies the timeout duration for a node condition. If a condition is met for the duration of the timeout, the machine will be remediated. Long timeouts can result in long periods of downtime for a workload on an unhealthy machine.

`spec.maxUnhealthy`
Specifies the amount of machines allowed to be concurrently remediated in the targeted pool. This can be set as a percentage or an integer. If the number of unhealthy machines exceeds the limit set by `maxUnhealthy`, remediation is not performed.

`spec.nodeStartupTimeout`
Specifies the timeout duration that a machine health check must wait for a node to join the cluster before a machine is determined to be unhealthy.

> [!NOTE]
> The `matchLabels` are examples only; you must map your machine groups based on your specific needs.

## About short-circuiting machine health check remediation

You can use machine health check short-circuiting to ensure that machine health checks remediate machines only when the cluster is healthy, by configuring the `maxUnhealthy` field in the `MachineHealthCheck` resource.

If you define a value for the `maxUnhealthy` field, before remediating any machines, the `MachineHealthCheck` compares the value of `maxUnhealthy` with the number of machines within its target pool that it has determined to be unhealthy. Remediation is not performed if the number of unhealthy machines exceeds the `maxUnhealthy` limit.

> [!IMPORTANT]
> If `maxUnhealthy` is not set, the value defaults to `100%` and the machines are remediated regardless of the state of the cluster.

The appropriate `maxUnhealthy` value depends on the scale of the cluster you deploy and how many machines the `MachineHealthCheck` covers. For example, you can use the `maxUnhealthy` value to cover multiple compute machine sets across multiple availability zones so that if you lose an entire zone, your `maxUnhealthy` setting prevents further remediation within the cluster. In global Azure regions that do not have multiple availability zones, you can use availability sets to ensure high availability.

> [!IMPORTANT]
> If you configure a `MachineHealthCheck` resource for the control plane, set the value of `maxUnhealthy` to `1`.
>
> This configuration ensures that the machine health check takes no action when multiple control plane machines appear to be unhealthy. Multiple unhealthy control plane machines can indicate that the etcd cluster is degraded or that a scaling operation to replace a failed machine is in progress.
>
> If the etcd cluster is degraded, manual intervention might be required. If a scaling operation is in progress, the machine health check should allow it to finish.

The `maxUnhealthy` field can be set as either an integer or percentage. There are different remediation implementations depending on the `maxUnhealthy` value.

Setting maxUnhealthy by using an absolute value
If `maxUnhealthy` is set to `2`:

- Remediation will be performed if 2 or fewer nodes are unhealthy

- Remediation will not be performed if 3 or more nodes are unhealthy

These values are independent of how many machines are being checked by the machine health check.

Setting maxUnhealthy by using percentages
If `maxUnhealthy` is set to `40%` and there are 25 machines being checked:

- Remediation will be performed if 10 or fewer nodes are unhealthy

- Remediation will not be performed if 11 or more nodes are unhealthy

If `maxUnhealthy` is set to `40%` and there are 6 machines being checked:

- Remediation will be performed if 2 or fewer nodes are unhealthy

- Remediation will not be performed if 3 or more nodes are unhealthy

> [!NOTE]
> The allowed number of machines is rounded down when the percentage of `maxUnhealthy` machines that are checked is not a whole number.

# Creating a machine health check resource

You can create a `MachineHealthCheck` resource to monitor and automatically remediate unhealthy machines in a machine set.

> [!NOTE]
> You can only apply a machine health check to machines that are managed by compute machine sets or control plane machine sets.

<div>

<div class="title">

Prerequisites

</div>

- Install the `oc` command-line interface.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `healthcheck.yml` file that contains the definition of your machine health check.

2.  Apply the `healthcheck.yml` file to your cluster:

    ``` terminal
    $ oc apply -f healthcheck.yml
    ```

</div>

# About power-based remediation of bare metal

You can configure and deploy a machine health check to detect and repair unhealthy bare-metal nodes, which is critical to ensuring the overall health of the cluster.

Physically remediating a cluster can be challenging and any delay in putting the machine into a safe or an operational state increases the time the cluster remains in a degraded state, and the risk that subsequent failures might bring the cluster offline. Power-based remediation helps counter such challenges.

Instead of reprovisioning the nodes, power-based remediation uses a power controller to power off an inoperable node. This type of remediation is also called power fencing.

OpenShift Container Platform uses the `MachineHealthCheck` controller to detect faulty bare metal nodes. Power-based remediation is fast and reboots faulty nodes instead of removing them from the cluster.

Power-based remediation provides the following capabilities:

- Allows the recovery of control plane nodes

- Reduces the risk of data loss in hyperconverged environments

- Reduces the downtime associated with recovering physical machines

## About machine health checks on bare metal

Machine deletion on bare metal cluster triggers reprovisioning of a bare metal host. Usually bare metal reprovisioning is a lengthy process, during which the cluster is missing compute resources and applications might be interrupted.

There are two ways to change the default remediation process from machine deletion to host power-cycle:

1.  Annotate the `MachineHealthCheck` resource with the `machine.openshift.io/remediation-strategy: external-baremetal` annotation.

2.  Create a `Metal3RemediationTemplate` resource, and refer to it in the `spec.remediationTemplate` of the `MachineHealthCheck`.

After using one of these methods, unhealthy machines are power-cycled by using Baseboard Management Controller (BMC) credentials.

About the annotation-based remediation process
The annotation-based remediation process performs the following steps:

1.  The MachineHealthCheck (MHC) controller detects that a node is unhealthy.

2.  The MHC notifies the bare metal machine controller which requests to power-off the unhealthy node.

3.  After the power is off, the node is deleted, which allows the cluster to reschedule the affected workload on other nodes.

4.  The bare metal machine controller requests to power on the node.

5.  After the node is up, the node re-registers itself with the cluster, resulting in the creation of a new node.

6.  After the node is recreated, the bare metal machine controller restores the annotations and labels that existed on the unhealthy node before its deletion.

> [!NOTE]
> If the power operations did not complete, the bare metal machine controller triggers the reprovisioning of the unhealthy node unless this is a control plane node or a node that was provisioned externally.

About the metal3-based remediation process
The metal3-based remediation process performs the following steps:

1.  The MachineHealthCheck (MHC) controller detects that a node is unhealthy.

2.  The MHC creates a metal3 remediation custom resource for the metal3 remediation controller, which requests to power-off the unhealthy node.

3.  After the power is off, the node is deleted, which allows the cluster to reschedule the affected workload on other nodes.

4.  The metal3 remediation controller requests to power on the node.

5.  After the node is up, the node re-registers itself with the cluster, resulting in the creation of a new node.

6.  After the node is recreated, the metal3 remediation controller restores the annotations and labels that existed on the unhealthy node before its deletion.

> [!NOTE]
> If the power operations did not complete, the metal3 remediation controller triggers the reprovisioning of the unhealthy node unless this is a control plane node or a node that was provisioned externally.

## Creating a MachineHealthCheck resource for bare metal

You control how a machine health check remediates unhealthy machines by using a `MachineHealthCheck` resource to configure health criteria, remediation limits, and startup timeouts for machines in a targeted pool.

<div>

<div class="title">

Prerequisites

</div>

- The OpenShift Container Platform is installed using installer-provisioned infrastructure.

- Access to Baseboard Management Controller (BMC) credentials or BMC access to each node.

- Network access to the BMC interface of the unhealthy node.

- For a metal3-based remediation, a `Metal3RemediationTemplate` resource must exist.

  <div class="formalpara">

  <div class="title">

  Sample `Metal3RemediationTemplate` resource for bare metal, metal3-based remediation

  </div>

  ``` yaml
  apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
  kind: Metal3RemediationTemplate
  metadata:
    name: metal3-remediation-template
    namespace: openshift-machine-api
  spec:
    template:
      spec:
        strategy:
          type: Reboot
          retryLimit: 1
          timeout: 5m0s
  ```

  </div>

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `healthcheck.yaml` file that contains the definition of your machine health check.

    <div class="formalpara">

    <div class="title">

    Sample `MachineHealthCheck` resource for bare metal, annotation-based remediation

    </div>

    ``` yaml
    apiVersion: machine.openshift.io/v1beta1
    kind: MachineHealthCheck
    metadata:
      name: example
      namespace: openshift-machine-api
      annotations:
        machine.openshift.io/remediation-strategy: external-baremetal
    spec:
      selector:
        matchLabels:
          machine.openshift.io/cluster-api-machine-role: <role>
          machine.openshift.io/cluster-api-machine-type: <role>
          machine.openshift.io/cluster-api-machineset: <cluster_name>-<label>-<zone>
      unhealthyConditions:
      - type:    "Ready"
        timeout: "300s"
        status: "False"
      - type:    "Ready"
        timeout: "300s"
        status: "Unknown"
      maxUnhealthy: "40%"
      nodeStartupTimeout: "10m"
    ```

    </div>

    where

    `metadata.name`
    Specify the name of the machine health check to deploy.

    `metadata.annotations`
    Specify the required annotation for the annotation-based remediation process.

    > [!IMPORTANT]
    > You must include the `machine.openshift.io/remediation-strategy: external-baremetal` annotation in the `annotations` section to enable annotation-based remediation. With this remediation strategy, unhealthy hosts are rebooted instead of removed from the cluster.

    `spec.selector.matchLabels`
    Specify the machine pool and machine set to check by adding labels:

    - `machine.openshift.io/cluster-api-machine-role`: Specify a label for the machine pool that you want to check.

    - `machine.openshift.io/cluster-api-machine-type`: Specify a label for the machine pool that you want to check.

    - `machine.openshift.io/cluster-api-machineset`: Specify the machine set to track in the `<cluster_name>-<label>-<zone>` format. For example, `prod-node-us-east-1a`.

    `spec.unhealthyConditions.timeout`
    Specify the timeout duration for a node condition. If a condition is met for the duration of the timeout, the machine will be remediated. Long timeouts can result in long periods of downtime for a workload on an unhealthy machine.

    `spec.maxUnhealthy`
    Specify the amount of machines allowed to be concurrently remediated in the targeted pool. This can be set as a percentage or an integer. If the number of unhealthy machines exceeds the limit set by `maxUnhealthy`, remediation is not performed.

    `spec.nodeStartupTimeout`
    Specify the timeout duration that a machine health check must wait for a node to join the cluster before a machine is determined to be unhealthy.

    <div class="formalpara">

    <div class="title">

    Sample `MachineHealthCheck` resource for bare metal, metal3-based remediation

    </div>

    ``` yaml
    apiVersion: machine.openshift.io/v1beta1
    kind: MachineHealthCheck
    metadata:
      name: example
      namespace: openshift-machine-api
    spec:
      selector:
        matchLabels:
          machine.openshift.io/cluster-api-machine-role: <role>
          machine.openshift.io/cluster-api-machine-type: <role>
          machine.openshift.io/cluster-api-machineset: <cluster_name>-<label>-<zone>
      remediationTemplate:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: Metal3RemediationTemplate
        name: metal3-remediation-template
        namespace: openshift-machine-api
      unhealthyConditions:
      - type:    "Ready"
        timeout: "300s"
    ```

    </div>

    where:

    `metadata.name`
    Specify the name of the machine health check to deploy.

    `spec.selector.matchLabels`
    Specify the machine pool and machine set to check by adding labels:

    - `machine.openshift.io/cluster-api-machine-role`: Specify a label for the machine pool that you want to check.

    - `machine.openshift.io/cluster-api-machine-type`: Specify a label for the machine pool that you want to check.

    - `machine.openshift.io/cluster-api-machineset`: Specify the machine set to track in the `<cluster_name>-<label>-<zone>` format. For example, `prod-node-us-east-1a`.

    `spec.remediationTemplate`
    Specify the metal3 remediation template to use. Provide the following information:

    - `apiVersion`. Specify the API version as `infrastructure.cluster.x-k8s.io/v1beta1`.

    - `kind`. Specify `Metal3RemediationTemplate`.

    - `name`. Specify the name of the template.

    - `namespace`. Specify the namespace of the template.

    `spec.unhealthyConditions.timeout`
    Specify the timeout duration for a node condition. If a condition is met for the duration of the timeout, the machine will be remediated. Long timeouts can result in long periods of downtime for a workload on an unhealthy machine.

    > [!NOTE]
    > The `matchLabels` are examples only; you must map your machine groups based on your specific needs.

2.  Apply the `healthcheck.yaml` file to your cluster using the following command:

    ``` terminal
    $ oc apply -f healthcheck.yaml
    ```

</div>

## Troubleshooting issues with power-based remediation

To troubleshoot issues you are having with power-based remediation, check the connection to the Baseboard Management Controller (BMC).

<div>

<div class="title">

Procedure

</div>

- Verify the following conditions:

  - You have access to the BMC.

  - The BMC is connected to the control plane node that is responsible for running the remediation task.

</div>
