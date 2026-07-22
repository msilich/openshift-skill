<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can partially skip intermediate odd-numbered releases by using control-plane-only EUS-to-EUS updates with RHACM policies and Topology Aware Lifecycle Manager (TALM). With this approach, you can manage control plane and worker version skew during staged rollouts.

# Updating with EUS-to-EUS control-plane-only updates

You can update clusters from one Extended Update Support (EUS) release to another using control-plane-only updates. This approach updates the control plane while leaving worker nodes at the previous EUS version, enabling staged rollouts that minimize workload disruption.

EUS releases provide 18 months of support and include even-numbered minor versions such as 4.18, 4.20, and 4.22. Control plane and worker nodes can be up to two minor versions apart during EUS-to-EUS updates.

> [!WARNING]
> Control plane and worker version skew is limited to N-2, or two minor versions. For example, if the control plane is at 4.20, workers must be updated before the control plane reaches 4.22, or they will be in an unsupported configuration. Plan worker updates accordingly to avoid exceeding the version skew policy. For more information about version skew policies, see the Kubernetes version and version skew support policy.

The following procedure demonstrates an EUS-to-EUS update using an example cluster.

> [!NOTE]
> The following procedure uses `spoke1` as an example cluster name. Replace it with your actual cluster name throughout.

<div>

<div class="title">

Prerequisites

</div>

- You have completed the pre-update health check successfully.

- TALM is installed and configured on the Red Hat Advanced Cluster Management (RHACM) hub cluster.

- The current cluster is at the latest z-stream of a source EUS version, such as 4.20.latest.

- The target EUS version is available, such as 4.22.

- You have verified that the EUS-to-EUS update path is supported in the release notes.

- You have reviewed the release notes for API deprecations and breaking changes between the source and target EUS versions.

- You have scheduled a maintenance window. EUS-to-EUS updates take 2 to 3 hours.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify the current cluster version is at the latest z-stream of the source EUS by running the following command:

    ``` terminal
    $ oc --context=spoke1 get clusterversion
    ```

    The following example shows the output:

    ``` terminal
    NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
    version   4.20.35   True        False         30d     Cluster version is 4.20.35
    ```

    If not at the latest z-stream, update to the latest patch release before proceeding.

2.  Validate that your cloud-native network function (CNF) workloads tolerate control plane and worker version skew:

    Verify that your CNF workloads can operate with the control plane at 4.22 while workers remain at 4.20. Consult with application teams if needed.

3.  Create a RHACM policy to pause worker nodes:

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

4.  Verify the current cluster channel before creating the update policy by running the following command:

    ``` terminal
    $ oc --context=spoke1 get clusterversion -o jsonpath='{.items[0].spec.channel}'
    ```

    The following example shows the output:

    ``` terminal
    eus-4.20
    ```

    If the cluster is on a non-EUS channel, such as `stable-4.20`, changing to an EUS channel and setting the required version simultaneously can cause unexpected update behavior.

5.  Get the release image reference for the target version.

    The image reference is required for the update policy. Retrieve it by running the following command:

    ``` terminal
    $ oc adm release info 4.21.5 | head -9
    ```

    The following example shows the output:

    ``` terminal
    Name:           4.21.5
    Digest:         sha256:93879f84b3165c5b5bd1fdf4563a11155dc61ea35cd93e67dc61c2b66e11c8bb
    Created:        2025-03-13T09:17:26Z
    OS/Arch:        linux/amd64
    Manifests:      758
    Metadata files: 2

    Pull From: quay.io/openshift-release-dev/ocp-release@sha256:93879f84b3165c5b5bd1fdf4563a11155dc61ea35cd93e67dc61c2b66e11c8bb
    ```

    Use the `Pull From` value as the `image` field in the update policy.

6.  Create a policy for the EUS update.

    For an EUS-to-EUS update, you need a separate policy for each y-stream step. The following example shows a policy for the first y-stream update:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: upgrade-ocp-20to21
      namespace: openshift-upgrade-policies
      annotations:
        policy.open-cluster-management.io/categories: CM Configuration Management
        policy.open-cluster-management.io/controls: CM-2 Baseline Configuration
        policy.open-cluster-management.io/standards: NIST SP 800-53
      labels:
        app.kubernetes.io/instance: policies
    spec:
      disabled: false
      policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: upgrade-ocp-20to21
            spec:
              object-templates:
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: config.openshift.io/v1
                    kind: ClusterVersion
                    metadata:
                      name: version
                    spec:
                      channel: eus-4.22
                      desiredUpdate:
                        force: true
                        image: quay.io/openshift-release-dev/ocp-release@sha256:df00d64554b9b5d860273f938e0ff3b0c4a7af8356fbd103658ebe6fa2a830c8
                        version: 4.21.29
                    status:
                      history:
                        - state: Completed
                          version: 4.21.29
              remediationAction: inform
              severity: low
      remediationAction: inform
    ```

    where:

    - `channel`: Sets the cluster channel to the target EUS release. Refer to the [update selection tool](https://access.redhat.com/labs/ocpupgradegraph/update_path/) when setting the channel.

    - `image`: Specifies the release image reference obtained from the `oc adm release info` command.

    - `version`: Sets the specific y-stream and z-stream release version for the cluster update. The `status.history` section ensures the policy remains noncompliant until the update completes.

    - `force`: The `force: true` field bypasses the Cincinnati update graph safety checks. Use this field only when the update path has been verified through the update selection tool or release notes. Removing this field or setting it to `false` causes the update to follow the standard update graph, which might not include a direct path for EUS-to-EUS intermediate hops.

    > [!IMPORTANT]
    > For an EUS-to-EUS update, create a policy for each y-stream step. For example, updating from 4.20 to 4.22 requires one policy for 4.20-to-4.21 and another for 4.21-to-4.22. For a complete example of chaining multiple policies across y-stream steps, see "Configuring ClusterGroupUpgrade custom resources for cluster updates".

7.  Apply the policies to RHACM by running the following commands:

    ``` terminal
    $ oc apply -f upgrade-ocp-20to21-policy.yaml
    $ oc apply -f core-pause-worker-nodes-policy.yaml
    ```

8.  Create a `ClusterGroupUpgrade` custom resource (CR) for the EUS update:

    ``` yaml
    apiVersion: ran.openshift.io/v1alpha1
    kind: ClusterGroupUpgrade
    metadata:
      name: core-eus-upgrade-4.20-to-4.22
      namespace: openshift-upgrade-policies
    spec:
      clusters:
      - spoke1
      managedPolicies:
      - core-pause-worker-nodes
      - upgrade-ocp-20to21
      enable: false
      remediationStrategy:
        maxConcurrency: 1
        timeout: 180
    ```

    EUS updates might take longer than single y-stream updates, so the timeout is set to 180 minutes, or 3 hours.

9.  Apply and enable the `ClusterGroupUpgrade` CR to start the EUS update by running the following commands:

    ``` terminal
    $ oc apply -f core-eus-upgrade-cgu.yaml
    $ oc patch cgu core-eus-upgrade-4.20-to-4.22 \
      -n openshift-upgrade-policies \
      --type merge \
      -p '{"spec":{"enable":true}}'
    ```

10. Monitor the EUS control plane update progress by running the following commands:

    ``` terminal
    $ oc get cgu core-eus-upgrade-4.20-to-4.22 -n openshift-upgrade-policies -w
    $ oc --context=spoke1 get clusterversion -w
    $ oc --context=spoke1 get co
    ```

    The cluster version progresses through intermediate versions during the EUS update. For example, updating from 4.20 to 4.22 goes through 4.21 internally. Cluster Operators might take longer to stabilize during EUS updates because of the larger version jump.

11. After the control plane update completes, verify control plane and worker node status by running the following commands:

    ``` terminal
    $ oc --context=spoke1 get nodes -l node-role.kubernetes.io/master=
    $ oc --context=spoke1 get co | grep -v "True.*False.*False"
    $ oc --context=spoke1 get nodes -l node-role.kubernetes.io/worker=
    ```

    The following example shows the output for control plane nodes:

    ``` terminal
    NAME                   STATUS   ROLES                  AGE   VERSION
    master-0.example.com   Ready    control-plane,master   60d   v1.35.0
    master-1.example.com   Ready    control-plane,master   60d   v1.35.0
    master-2.example.com   Ready    control-plane,master   60d   v1.35.0
    ```

    Control plane nodes must show the new kubelet version, 4.22. All Operators must be healthy before updating worker nodes.

    The following example shows the output for worker nodes:

    ``` terminal
    NAME                   STATUS   ROLES    AGE   VERSION
    worker-0.example.com   Ready    worker   60d   v1.33.0
    worker-1.example.com   Ready    worker   60d   v1.33.0
    worker-2.example.com   Ready    worker   60d   v1.33.0
    ```

    Worker nodes must still show the previous kubelet version, 4.20.

12. Update OLM Operators for the new EUS version:

    Operators might need multiple version jumps for EUS-to-EUS updates. Check the status of OLM Operators by running the following command:

    ``` terminal
    $ oc --context=spoke1 get csv -A | grep -v Succeeded
    ```

    Update Operator subscriptions to EUS-compatible channels by running the following command:

    ``` terminal
    $ oc --context=spoke1 patch subscription sriov-network-operator-subscription \
      -n openshift-sriov-network-operator \
      --type merge \
      -p '{"spec":{"channel":"stable-4.22"}}'
    ```

13. When ready to update worker nodes, create and apply an unpause policy:

    Determine the timing for worker node updates based on your maintenance schedule. Workers can remain at the previous EUS version for an extended period if needed.

    Follow the procedure in "Pausing and unpausing worker nodes by using TALM" to unpause and update workers.

14. Monitor worker node updates to completion by running the following command:

    ``` terminal
    $ oc --context=spoke1 get mcp worker -w
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify all nodes are at the target EUS version by running the following command:

    ``` terminal
    $ oc --context=spoke1 get nodes
    ```

2.  Verify all cluster Operators are healthy by running the following command:

    ``` terminal
    $ oc --context=spoke1 get co
    ```

3.  Validate CNF-specific resources by running the following commands:

    ``` terminal
    $ oc --context=spoke1 get performanceprofile
    $ oc --context=spoke1 get ptpconfig -n openshift-ptp
    $ oc --context=spoke1 get sriovnetworknodepolicy -n openshift-sriov-network-operator
    ```

4.  Run comprehensive smoke tests for all CNF workloads.

</div>

<div>

<div class="title">

Troubleshooting

</div>

- If the EUS update path is not available, verify you are at the latest z-stream of the source EUS version.

- If the control plane update gets stuck, check for Operator compatibility issues with the target EUS version.

- If worker nodes fail to update after unpause, check the `MachineConfigPool` resource status and node logs.

</div>

# Additional resources

- [Prepare RHACM policies and TALM for cluster updates](update-rhacm-talm-preparing-policies.md#core-cluster-upgrades-preparing-policies)

- [Manage worker nodes during a cluster update with TALM](update-rhacm-talm-worker-management.md#core-cluster-upgrades-worker-management)

- [Perform health checks before a cluster update with TALM](update-rhacm-talm-health-checks.md#core-cluster-upgrades-health-checks)

- [OpenShift Container Platform update documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/)

- [OpenShift Container Platform update lifecycle and support policy](https://access.redhat.com/support/policy/updates/openshift)
