<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can pause and unpause worker nodes during cluster updates to stage control plane and worker node updates separately, minimizing workload disruption.

# Pausing and unpausing worker nodes by using TALM

You can pause worker nodes before updating the control plane by using Topology Aware Lifecycle Manager (TALM) policies. After the control plane update completes, you can unpause worker nodes to apply the update to compute resources during a separate maintenance window.

Pausing worker nodes prevents the `MachineConfigPool` resource from updating worker nodes while the control plane updates, minimizing workload disruption.

<div>

<div class="title">

Prerequisites

</div>

- You have access to clusters with cluster-admin privileges.

- Topology Aware Lifecycle Manager (TALM) is installed on the Red Hat Advanced Cluster Management (RHACM) hub cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a RHACM policy for each `MachineConfigPool` resource that needs to be paused during the update:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: pause-<mcp_name>
      namespace: openshift-upgrade-policies
    spec:
      disabled: false
      policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            evaluationInterval:
              compliant: never
            kind: ConfigurationPolicy
            metadata:
              name: pause-<mcp_name>
            spec:
              object-templates:
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: machineconfiguration.openshift.io/v1
                    kind: MachineConfigPool
                    metadata:
                      name: <mcp_name>
                    spec:
                      paused: true
              remediationAction: inform
              severity: low
      remediationAction: inform
    ```

    where `<mcp_name>` is the name of the machine config pool to pause, for example `mcp-1`. This value is used in both the policy name and the `MachineConfigPool` resource name.

    > [!IMPORTANT]
    > Create a separate policy for each `MachineConfigPool` resource that you need to pause during the cluster update. If the machine config pool is not paused, any machine configuration change triggers a node reboot. Pausing the machine config pool allows all configuration changes to be applied in a single reboot when the pool is unpaused.

2.  Apply the policy to RHACM by running the following command:

    ``` terminal
    $ oc apply -f pause-<mcp_name>-policy.yaml
    ```

3.  Include the pause policy in your `ClusterGroupUpgrade` custom resource (CR) before the update policy:

    ``` yaml
    apiVersion: ran.openshift.io/v1alpha1
    kind: ClusterGroupUpgrade
    metadata:
      name: <cgu_name>
      namespace: <namespace>
    spec:
      clusters:
      - <cluster_name>
      managedPolicies:
      - pause-<mcp_name>
      - <upgrade_policy_name>
      enable: false
      remediationStrategy:
        maxConcurrency: 1
        timeout: 120
    ```

    TALM applies the pause policy before applying the update policy, ensuring workers remain paused during the control plane update.

4.  After the control plane update completes and you are ready to update worker nodes, create an unpause policy for each `MachineConfigPool` resource:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: unpause-<mcp_name>
      namespace: openshift-upgrade-policies
    spec:
      disabled: false
      policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            evaluationInterval:
              compliant: never
            kind: ConfigurationPolicy
            metadata:
              name: unpause-<mcp_name>
            spec:
              object-templates:
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: machineconfiguration.openshift.io/v1
                    kind: MachineConfigPool
                    metadata:
                      name: <mcp_name>
                    spec:
                      paused: false
              remediationAction: inform
              severity: low
      remediationAction: inform
    ```

    where `<mcp_name>` is the name of the machine config pool to unpause, for example `mcp-1`.

    The unpause policies for each machine config pool are included as managed policies in the final `ClusterGroupUpgrade` CR. When TALM enforces these policies, the machine config pools unpause and all accumulated configuration changes are applied in a single reboot per node.

5.  Apply the unpause policy by using a `ClusterGroupUpgrade` CR:

    ``` yaml
    apiVersion: ran.openshift.io/v1alpha1
    kind: ClusterGroupUpgrade
    metadata:
      name: <cgu_name>
      namespace: <namespace>
    spec:
      clusters:
      - <cluster_name>
      managedPolicies:
      - unpause-<mcp_name>
      enable: false
      remediationStrategy:
        maxConcurrency: 1
    ```

6.  Apply and enable the `ClusterGroupUpgrade` CR to unpause workers by running the following commands:

    ``` terminal
    $ oc apply -f <unpause_cgu_cr_filename>.yaml
    $ oc patch cgu <cgu_name> \
      -n <namespace> \
      --type merge \
      -p '{"spec":{"enable":true}}'
    ```

7.  Monitor worker node updates after unpausing by running the following command:

    ``` terminal
    $ oc get mcp <mcp_name> -w
    ```

    The `MachineConfigPool` status shows the rolling update progress. Nodes update in a rolling fashion based on the `maxUnavailable` setting.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that worker nodes are updated and workloads are healthy by running the following commands:

    ``` terminal
    $ oc get nodes
    $ oc get mcp <mcp_name>
    $ oc get pods -A | grep -v Running | grep -v Completed
    ```

    All nodes must show `Ready` status and the expected kubelet version. For the `MachineConfigPool` output, verify that `MACHINECOUNT` = `READYMACHINECOUNT` = `UPDATEDMACHINECOUNT`. The `oc get pods` command must return no unexpected pods.

</div>

<div>

<div class="title">

Troubleshooting

</div>

- If the pause policy does not take effect, verify the policy is enforced in RHACM by running the following command:

  ``` terminal
  $ oc get policy <pause_policy_name> -n <namespace>
  ```

- If workers update despite being paused, check for manual `MachineConfigPool` edits that override the policy.

- If a worker node update gets stuck, check the node status by running the following command:

  ``` terminal
  $ oc describe node <worker_node_name>
  ```

- Common issues include pod disruption budgets blocking node draining, pods with local storage that cannot be evicted, or node cordoning preventing new pods from scheduling.

  To identify blocking pod disruption budgets, run the following command:

  ``` terminal
  $ oc get pdb -A -o jsonpath='{range .items[?(@.status.disruptionsAllowed==0)]}{.metadata.namespace}{"\t"}{.metadata.name}{"\n"}{end}'
  ```

</div>

# Pausing and unpausing worker nodes by using machine config pools

You can pause and unpause worker nodes directly by patching the `MachineConfigPool` resource on the target cluster. Use this method when you are managing a single cluster or when you do not have Topology Aware Lifecycle Manager (TALM) configured.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the target cluster with cluster-admin privileges.

- The `oc` CLI tool is installed and configured.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Pause the worker `MachineConfigPool` resource by running the following command:

    ``` terminal
    $ oc patch mcp worker --type merge -p '{"spec":{"paused":true}}'
    ```

2.  Verify the worker `MachineConfigPool` resource is paused and workloads continue running by running the following commands:

    ``` terminal
    $ oc get mcp worker -o jsonpath='{.spec.paused}'
    $ oc get mcp worker
    $ oc get pods -A -o wide | grep worker
    ```

3.  After the control plane update completes and you are ready to update worker nodes, unpause the worker `MachineConfigPool` resource by running the following command:

    ``` terminal
    $ oc patch mcp worker --type merge -p '{"spec":{"paused":false}}'
    ```

4.  Monitor worker node updates after unpausing by running the following commands:

    ``` terminal
    $ oc get mcp worker -w
    $ oc get nodes -l node-role.kubernetes.io/worker= -w
    ```

    Nodes progress through the following states:

    - `Ready,SchedulingDisabled`: Node is being drained

    - `NotReady,SchedulingDisabled`: Node is rebooting with new configuration

    - `Ready`: Node update complete

</div>

<div>

<div class="title">

Verification

</div>

- Verify that worker nodes are updated and workloads are healthy by running the following commands:

  ``` terminal
  $ oc get nodes
  $ oc get mcp worker
  $ oc get pods -A | grep -v Running | grep -v Completed
  ```

  All nodes must show `Ready` status and the expected kubelet version. For the `MachineConfigPool` output, verify that `MACHINECOUNT` = `READYMACHINECOUNT` = `UPDATEDMACHINECOUNT`. The `oc get pods` command must return no unexpected pods.

</div>

# Additional resources

- [Complete an EUS-to-EUS cluster update with TALM](update-rhacm-talm-eus.md#core-cluster-upgrades-eus)

- [Prepare worker node pools before a cluster update with TALM](update-rhacm-talm-worker-batching.md#core-cluster-upgrades-worker-batching)

- [Using the Topology Aware Lifecycle Manager for cluster updates](../../../edge_computing/cnf-talm-for-cluster-upgrades.md#cnf-talm-for-cluster-updates)
