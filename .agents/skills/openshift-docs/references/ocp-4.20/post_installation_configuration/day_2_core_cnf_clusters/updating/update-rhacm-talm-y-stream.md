<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Y-stream updates move clusters between minor versions. You can update through a single y-stream release or chain multiple sequential updates to reach a target version that is more than one minor release away.

# Updating clusters through y-stream releases

You can update clusters through minor version, or y-stream, releases by using RHACM policies and Topology Aware Lifecycle Manager (TALM). Y-stream updates introduce new features and might include API deprecations, requiring careful planning and validation.

You must perform y-stream updates through consecutive versions. You cannot skip versions during y-stream updates. For example, to update from 4.20 to 4.22, you must update from 4.20 to 4.21, and then from 4.21 to 4.22. If you need to move 2 y-stream versions, consider EUS-to-EUS updates instead.

> [!NOTE]
> The following procedure uses `spoke1` as an example cluster name. Replace it with your actual cluster name throughout.

<div>

<div class="title">

Prerequisites

</div>

- You have completed the pre-update health check successfully.

- TALM is installed and configured on the Red Hat Advanced Cluster Management (RHACM) hub cluster.

- A y-stream release is available, such as 4.21 when updating from 4.20.

- You have reviewed the y-stream release notes for API deprecations and breaking changes.

- You have scheduled a maintenance window. Y-stream updates take 1 to 2 hours.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Identify deprecated APIs in use on your cluster by running the following command:

    ``` terminal
    $ oc get apirequestcounts -o jsonpath='{range .items[?(@.status.removedInRelease!="")]}{.status.removedInRelease}{"\t"}{.metadata.name}{"\n"}{end}' | sort -k1
    ```

    This command shows APIs that will be removed in future releases. Review the OpenShift Container Platform release notes for your target version and update any resources that use deprecated or removed APIs before updating.

2.  Validate OLM Operator compatibility with the target y-stream version by running the following command:

    ``` terminal
    $ oc get csv -A
    ```

    All Operators must show `Succeeded` status. Investigate any Operators in a failed state before proceeding.

3.  Review Operator subscription channels to ensure they support the target OpenShift Container Platform version by running the following command:

    ``` terminal
    $ oc get subscription -A -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.channel}{"\n"}{end}'
    ```

    Update Operator subscriptions if needed before the cluster update.

4.  Create a RHACM policy to pause worker nodes:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: core-pause-worker-nodes
      namespace: openshift-upgrade-policies
    spec:
      remediationAction: inform
      disabled: false
      policy-templates:
      - objectDefinition:
          apiVersion: policy.open-cluster-management.io/v1
          kind: ConfigurationPolicy
          metadata:
            name: pause-worker-mcp
          spec:
            remediationAction: inform
            severity: high
            object-templates:
            - complianceType: musthave
              objectDefinition:
                apiVersion: machineconfiguration.openshift.io/v1
                kind: MachineConfigPool
                metadata:
                  name: worker
                spec:
                  paused: true
    ```

5.  Create a RHACM policy for the y-stream update:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: core-upgrade-4.21-policy
      namespace: openshift-upgrade-policies
    spec:
      remediationAction: inform
      disabled: false
      policy-templates:
      - objectDefinition:
          apiVersion: policy.open-cluster-management.io/v1
          kind: ConfigurationPolicy
          metadata:
            name: upgrade-cluster-version
          spec:
            remediationAction: inform
            severity: high
            object-templates:
            - complianceType: musthave
              objectDefinition:
                apiVersion: config.openshift.io/v1
                kind: ClusterVersion
                metadata:
                  name: version
                spec:
                  channel: stable-4.21
                  desiredUpdate:
                    version: 4.21.0
    ```

    Replace `4.21.0` with your target y-stream version. Both policies are set to `inform` so they do not immediately push changes. The `ClusterGroupUpgrade` custom resource (CR) enforces these policies at the scheduled update time.

6.  Apply the policies to RHACM by running the following commands:

    ``` terminal
    $ oc apply -f core-pause-worker-policy.yaml
    $ oc apply -f core-upgrade-4.21-policy.yaml
    ```

7.  Verify the policies and placement resources were created by running the following commands:

    ``` terminal
    $ oc get policy -n openshift-upgrade-policies
    $ oc get placementbinding -n openshift-upgrade-policies
    $ oc get placement -n openshift-upgrade-policies
    ```

    If no `PlacementBinding` or `Placement` exists, the policies will not apply to any clusters. Create appropriate placement resources for your target clusters.

8.  Create a `ClusterGroupUpgrade` CR for the y-stream update:

    ``` yaml
    apiVersion: ran.openshift.io/v1alpha1
    kind: ClusterGroupUpgrade
    metadata:
      name: core-ystream-upgrade-4.21
      namespace: openshift-upgrade-policies
    spec:
      clusters:
      - spoke1
      managedPolicies:
      - core-pause-worker-nodes
      - core-upgrade-4.21-policy
      enable: false
      remediationStrategy:
        maxConcurrency: 1
        timeout: 120
      actions:
        beforeEnable:
          addClusterLabels:
            upgrade-in-progress: "true"
        afterCompletion:
          addClusterLabels:
            upgraded-to: "4.21"
            control-plane-upgraded: "true"
    ```

    For canary deployments, use a single cluster first before updating additional clusters.

9.  Apply and enable the `ClusterGroupUpgrade` CR to start the control plane update by running the following commands:

    ``` terminal
    $ oc apply -f core-ystream-cgu.yaml
    $ oc patch cgu core-ystream-upgrade-4.21 \
      -n openshift-upgrade-policies \
      --type merge \
      -p '{"spec":{"enable":true}}'
    ```

10. Monitor the control plane update progress by running the following commands:

    ``` terminal
    $ oc get cgu core-ystream-upgrade-4.21 -n openshift-upgrade-policies -w
    $ oc --context=spoke1 get clusterversion -w
    $ oc --context=spoke1 get co
    ```

    Cluster Operators update sequentially during the y-stream update. The control plane update typically takes 60 to 120 minutes.

11. After the control plane update completes, verify control plane health by running the following commands:

    ``` terminal
    $ oc --context=spoke1 get nodes -l node-role.kubernetes.io/master=
    $ oc --context=spoke1 get co | grep -v "True.*False.*False"
    ```

    All control plane nodes and Operators must be healthy before proceeding.

12. Create an OLM Operator update policy that updates Operator subscription channels to versions compatible with the new y-stream:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: core-upgrade-olm-4.21
      namespace: openshift-upgrade-policies
    spec:
      remediationAction: inform
      disabled: false
      policy-templates:
      - objectDefinition:
          apiVersion: policy.open-cluster-management.io/v1
          kind: ConfigurationPolicy
          metadata:
            name: upgrade-olm-operators
          spec:
            remediationAction: inform
            severity: high
            object-templates:
            - complianceType: musthave
              objectDefinition:
                apiVersion: operators.coreos.com/v1alpha1
                kind: Subscription
                metadata:
                  name: sriov-network-operator-subscription
                  namespace: openshift-sriov-network-operator
                spec:
                  channel: stable-4.21
                status:
                  state: AtLatestKnown
    ```

    You can include multiple Operator subscriptions in the same policy. For more details about creating OLM update policies, see "Coordinating OLM Operator updates with cluster updates".

13. Create a `ClusterGroupUpgrade` CR to apply the OLM Operator update policy:

    ``` yaml
    apiVersion: ran.openshift.io/v1alpha1
    kind: ClusterGroupUpgrade
    metadata:
      name: core-olm-upgrade-4.21
      namespace: openshift-upgrade-policies
    spec:
      clusters:
      - spoke1
      managedPolicies:
      - core-upgrade-olm-4.21
      enable: true
      remediationStrategy:
        maxConcurrency: 1
        timeout: 60
    ```

14. Apply the OLM Operator update policy and `ClusterGroupUpgrade` CR by running the following commands:

    ``` terminal
    $ oc apply -f core-olm-upgrade-policy.yaml
    $ oc apply -f core-olm-cgu.yaml
    ```

15. Monitor the OLM Operator update and verify that worker nodes remain at the previous version by running the following commands:

    ``` terminal
    $ oc get cgu core-olm-upgrade-4.21 -n openshift-upgrade-policies -w
    $ oc --context=spoke1 get nodes
    ```

    Worker nodes must still show the previous kubelet version.

16. Create a policy to unpause worker nodes:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: core-unpause-worker-nodes
      namespace: openshift-upgrade-policies
    spec:
      remediationAction: inform
      disabled: false
      policy-templates:
      - objectDefinition:
          apiVersion: policy.open-cluster-management.io/v1
          kind: ConfigurationPolicy
          metadata:
            name: unpause-worker-mcp
          spec:
            remediationAction: inform
            severity: high
            object-templates:
            - complianceType: musthave
              objectDefinition:
                apiVersion: machineconfiguration.openshift.io/v1
                kind: MachineConfigPool
                metadata:
                  name: worker
                spec:
                  paused: false
    ```

17. Create a `ClusterGroupUpgrade` CR to unpause workers:

    ``` yaml
    apiVersion: ran.openshift.io/v1alpha1
    kind: ClusterGroupUpgrade
    metadata:
      name: core-unpause-workers-4.21
      namespace: openshift-upgrade-policies
    spec:
      clusters:
      - spoke1
      managedPolicies:
      - core-unpause-worker-nodes
      enable: false
      remediationStrategy:
        maxConcurrency: 1
    ```

18. Apply and enable the unpause `ClusterGroupUpgrade` CR by running the following commands:

    ``` terminal
    $ oc apply -f core-unpause-workers-cgu.yaml
    $ oc patch cgu core-unpause-workers-4.21 \
      -n openshift-upgrade-policies \
      --type merge \
      -p '{"spec":{"enable":true}}'
    ```

19. Monitor worker node updates by running the following command:

    ``` terminal
    $ oc --context=spoke1 get mcp worker -w
    ```

    Worker nodes update in a rolling fashion. The process typically takes 30 to 60 minutes depending on the number of worker nodes.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify all nodes are at the target y-stream version by running the following command:

    ``` terminal
    $ oc --context=spoke1 get nodes
    ```

2.  Verify all cluster Operators are healthy by running the following command:

    ``` terminal
    $ oc --context=spoke1 get co
    ```

3.  Verify workload health and CNF-specific resources by running the following commands:

    ``` terminal
    $ oc --context=spoke1 get pods -A | grep -v Running | grep -v Completed
    $ oc --context=spoke1 get performanceprofile
    $ oc --context=spoke1 get ptpconfig -n openshift-ptp
    $ oc --context=spoke1 get sriovnetworknodepolicy -n openshift-sriov-network-operator
    ```

4.  Run smoke tests for critical workloads.

</div>

<div>

<div class="title">

Troubleshooting

</div>

- If API deprecation warnings appear, update manifests to use new API versions before updating.

- If Operator compatibility issues occur, update Operator subscriptions to channels that support the target y-stream.

- If worker node updates get stuck, check `MachineConfigPool` resource status and node logs.

</div>

# Updating through sequential y-stream releases

You can update clusters through multiple sequential y-stream releases when you need to move from an older version to a newer version that is more than one minor release away. You must update through each intermediate y-stream version because skipping versions is not supported.

For example, to update from 4.20 to 4.22, you must first update from 4.20 to 4.21, and then update from 4.21 to 4.22.

> [!NOTE]
> The following procedure uses `spoke1` as an example cluster name. Replace it with your actual cluster name throughout.

> [!IMPORTANT]
> When planning to update clusters through multiple sequential y-stream releases, allow at least 24 hours, and up to 48 hours, between y-stream updates to monitor cluster stability.

<div>

<div class="title">

Prerequisites

</div>

- You have completed the pre-update health check successfully.

- TALM is installed and configured on the Red Hat Advanced Cluster Management (RHACM) hub cluster.

- You have access to the target clusters with cluster-admin privileges.

- The `oc` CLI tool is installed and configured for the target clusters.

- All intermediate y-stream releases are available, such as both 4.21 and 4.22 when updating from 4.20 to 4.22.

- You have reviewed the release notes for each intermediate y-stream version for API deprecations and breaking changes.

- You have planned maintenance windows for each y-stream update.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Determine the complete update path:

    Identify your current version and target version, then map out the required intermediate versions.

    | Current version | Update path to 4.22                          |
    |-----------------|----------------------------------------------|
    | 4.20.20         | 4.20.20 → 4.21.latest → 4.22.0               |
    | 4.19.10         | 4.19.10 → 4.20.latest → 4.21.latest → 4.22.0 |

    Example update paths

2.  Update to the first intermediate y-stream version:

    Follow the procedure in "Updating clusters through y-stream releases" to update to the first intermediate version.

    For example, update from 4.20.20 to 4.21.latest.

3.  Verify the first y-stream update completed successfully by running the following command:

    ``` terminal
    $ oc --context=spoke1 get clusterversion
    ```

    Verify all cluster Operators are healthy by running the following command:

    ``` terminal
    $ oc --context=spoke1 get co | grep -v "True.*False.*False"
    ```

    All cluster Operators must show healthy status before proceeding.

4.  Wait at least 24 hours, and up to 48 hours, between y-stream updates:

    Allow time to monitor cluster stability after the first update. Extend this period for large production deployments or if any anomalies are observed.

    During this wait period:

    - Monitor workload health and performance.

    - Check for unexpected behavior or errors.

    - Run smoke tests for critical cloud-native network function (CNF) workloads.

    - Verify all custom resources specific to your deployment are functioning correctly.

    - Review release notes for the next y-stream version for additional API deprecations or configuration changes.

5.  Update OLM Operator subscriptions if needed:

    Some Operators might require intermediate channel updates when updating through multiple y-streams. Verify the Operator status by running the following command:

    ``` terminal
    $ oc --context=spoke1 get csv -A
    ```

    Verify all Operators are at versions compatible with your current cluster version before proceeding.

6.  Create RHACM policies for the second y-stream update:

    Update the cluster version policy to target the next y-stream:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: core-upgrade-4.22-policy
      namespace: openshift-upgrade-policies
    spec:
      remediationAction: inform
      disabled: false
      policy-templates:
      - objectDefinition:
          apiVersion: policy.open-cluster-management.io/v1
          kind: ConfigurationPolicy
          metadata:
            name: upgrade-cluster-version
          spec:
            remediationAction: inform
            severity: high
            object-templates:
            - complianceType: musthave
              objectDefinition:
                apiVersion: config.openshift.io/v1
                kind: ClusterVersion
                metadata:
                  name: version
                spec:
                  channel: stable-4.22
                  desiredUpdate:
                    version: 4.22.0
    ```

7.  Apply the updated policy by running the following command:

    ``` terminal
    $ oc apply -f core-upgrade-4.22-policy.yaml
    ```

8.  Create a new `ClusterGroupUpgrade` custom resource (CR) for the second y-stream:

    ``` yaml
    apiVersion: ran.openshift.io/v1alpha1
    kind: ClusterGroupUpgrade
    metadata:
      name: core-ystream-upgrade-4.22
      namespace: openshift-upgrade-policies
    spec:
      clusters:
      - spoke1
      managedPolicies:
      - core-pause-worker-nodes
      - core-upgrade-4.22-policy
      enable: false
      remediationStrategy:
        maxConcurrency: 1
        timeout: 120
    ```

9.  Apply and enable the `ClusterGroupUpgrade` CR by running the following commands:

    ``` terminal
    $ oc apply -f core-ystream-upgrade-4.22-cgu.yaml
    $ oc patch cgu core-ystream-upgrade-4.22 \
      -n openshift-upgrade-policies \
      --type merge \
      -p '{"spec":{"enable":true}}'
    ```

10. Monitor the second y-stream update and verify completion by running the following commands:

    ``` terminal
    $ oc get cgu core-ystream-upgrade-4.22 -n openshift-upgrade-policies -w
    $ oc --context=spoke1 get clusterversion
    $ oc --context=spoke1 get co
    ```

11. Update Operators for the second y-stream by running the following command:

    ``` terminal
    $ oc --context=spoke1 get csv -A | grep -v Succeeded
    ```

    Update Operator channels as needed for the new cluster version.

12. Unpause worker nodes and complete the second y-stream update:

    Follow the worker node unpause procedure from "Pausing and unpausing worker nodes by using TALM".

13. Repeat steps 2-12 for any additional intermediate y-stream versions:

    If updating through more than two y-streams, repeat the process for each intermediate version.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify the final cluster version by running the following command:

    ``` terminal
    $ oc --context=spoke1 get clusterversion -o jsonpath='{.items[0].status.desired.version}'
    ```

2.  Run comprehensive health checks:

    Follow the procedure in "Performing health checks before cluster updates".

3.  Verify workload functionality after all updates:

    Run smoke tests and validate that all CNF workloads operate correctly at the final version.

</div>

<div>

<div class="title">

Troubleshooting

</div>

- If the cluster becomes degraded after the first y-stream update, resolve all issues before proceeding to the second y-stream.

- If Operator versions are incompatible with an intermediate y-stream, update the Operator subscription before updating the cluster.

- If configuration changes are needed between y-streams, apply those changes during the wait period before proceeding.

</div>

# Additional resources

- [Complete an EUS-to-EUS cluster update with TALM](update-rhacm-talm-eus.md#core-cluster-upgrades-eus)

- [Prepare RHACM policies and TALM for cluster updates](update-rhacm-talm-preparing-policies.md#core-cluster-upgrades-preparing-policies)

- [Perform health checks before a cluster update with TALM](update-rhacm-talm-health-checks.md#core-cluster-upgrades-health-checks)

- [OpenShift Container Platform update documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/)

- [OpenShift Container Platform update lifecycle and support policy](https://access.redhat.com/support/policy/updates/openshift)
