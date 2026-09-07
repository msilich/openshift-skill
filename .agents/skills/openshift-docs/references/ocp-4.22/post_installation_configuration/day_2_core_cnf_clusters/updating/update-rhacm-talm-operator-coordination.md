<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

OLM-managed Operators must be compatible with the target OpenShift Container Platform version before you begin a cluster update. Planning Operator updates alongside cluster updates prevents compatibility issues that can block or degrade the update process.

# Coordinating OLM Operator updates with cluster updates

You can coordinate Operator Lifecycle Manager (OLM) Operator updates with OpenShift Container Platform cluster updates to ensure Operator compatibility. Incompatible Operators can block cluster updates or cause degraded cluster Operators after updates complete.

<div>

<div class="title">

Prerequisites

</div>

- You have an understanding of OLM concepts including subscriptions, channels, and `ClusterServiceVersions` (CSVs).

- You have access to clusters with cluster-admin privileges.

- Topology Aware Lifecycle Manager (TALM) is installed on the Red Hat Advanced Cluster Management (RHACM) hub cluster.

- A cluster update is planned or in progress.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check installed Operator versions and subscription channels by running the following commands:

    ``` terminal
    $ oc get csv -A
    $ oc get subscription -A
    ```

    The following example shows the output:

    ``` terminal
    NAMESPACE                              NAME                                          VERSION   PHASE
    openshift-sriov-network-operator       sriov-network-operator.v4.20.0                4.20.0    Succeeded
    openshift-ptp                          ptp-operator.v4.20.0                          4.20.0    Succeeded
    openshift-cluster-node-tuning-operator node-tuning-operator.v4.20.0                  4.20.0    Succeeded
    ```

    The following example shows the output:

    ``` terminal
    NAMESPACE                              NAME                                PACKAGE                  SOURCE             CHANNEL
    openshift-sriov-network-operator       sriov-network-operator-subscription sriov-network-operator   redhat-operators   stable-4.20
    openshift-ptp                          ptp-operator-subscription           ptp-operator             redhat-operators   stable-4.20
    ```

2.  Identify Operators that need channel updates before the cluster update:

    Review Operator compatibility in the OpenShift Container Platform release notes and identify which Operator channels support your target OpenShift Container Platform version. For a cluster updating from 4.20 to 4.21, identify Operators still on 4.20 channels. Refer to the [Red Hat Catalog](https://catalog.redhat.com/en) for compatibility details for each Operator.

3.  Create an OLM Operator update policy.

    In environments where Operator updates are set to manual approval, use a TALM-managed policy to coordinate Operator updates. When TALM enforces the policy, it automatically approves the Operator `InstallPlan`:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: upgrade-olm-21
      namespace: openshift-upgrade-policies
      annotations:
        ran.openshift.io/soak-seconds: "60"
    spec:
      disabled: false
      policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: upgrade-olm-21
            spec:
              object-templates:
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: operators.coreos.com/v1alpha1
                    kind: Subscription
                    metadata:
                      name: cluster-logging
                      namespace: openshift-logging
                    spec:
                      name: cluster-logging
                      channel: stable-6.1
                    status:
                      state: AtLatestKnown
    ```

    where:

    - `ran.openshift.io/soak-seconds`: Specifies the soak-seconds annotation that gives the catalog pod time to restart and OLM time to read version data from the new pod before evaluating the `Subscription` status. This avoids a race condition where the policy evaluates too quickly after a catalog image change.

    - `channel`: Sets the channel only if it needs to change for the new version. Channels are determined by the Operator development team. Refer to the [Red Hat Catalog](https://catalog.redhat.com/en) for compatibility.

    - `status.state: AtLatestKnown`: Ensures the Operator update completes before TALM proceeds to the next step.

    You can include multiple Operator subscriptions in the same policy. The following example shows multiple Operators in a single policy:

    ``` yaml
    spec:
      disabled: false
      policy-templates:
        - objectDefinition:
            apiVersion: policy.open-cluster-management.io/v1
            kind: ConfigurationPolicy
            metadata:
              name: upgrade-olm-20to21
            spec:
              object-templates:
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: operators.coreos.com/v1alpha1
                    kind: Subscription
                    metadata:
                      name: sriov-network-operator-subscription
                      namespace: openshift-sriov-network-operator
                    spec:
                      name: sriov-network-operator
                      channel: stable
                      installPlanApproval: Manual
                      source: redhat-operators
                      sourceNamespace: openshift-marketplace
                    status:
                      state: AtLatestKnown
                - complianceType: musthave
                  objectDefinition:
                    apiVersion: operators.coreos.com/v1alpha1
                    kind: Subscription
                    metadata:
                      name: kubernetes-nmstate-operator
                      namespace: openshift-nmstate
                    spec:
                      name: kubernetes-nmstate-operator
                      channel: stable
                      installPlanApproval: Manual
                      source: redhat-operators
                      sourceNamespace: openshift-marketplace
                    status:
                      state: AtLatestKnown
    ```

    For an example of creating this policy with zero touch provisioning (ZTP), see [Example OLM update policy in the OpenShift KNI reference repository](https://github.com/openshift-kni/telco-reference/blob/main/telco-core/configuration/core-upgrade.yaml#L68-L101).

4.  Monitor Operator updates and verify the new versions by running the following commands:

    ``` terminal
    $ oc get csv -n openshift-sriov-network-operator -w
    $ oc get csv -n openshift-sriov-network-operator -o jsonpath='{.items[?(@.spec.version=="4.21.0")].status.phase}'
    ```

    The Operator creates a new `ClusterServiceVersion` and transitions to the new version.

    The following example shows the output:

    ``` terminal
    Succeeded
    ```

5.  After the control plane update completes, check for pending Operator updates by running the following command:

    ``` terminal
    $ oc get csv -A
    ```

    Some Operators might not update until after the cluster update completes.

6.  If Operators are configured with manual approval, list and approve pending install plans by running the following commands:

    ``` terminal
    $ oc get installplan -A
    $ oc patch installplan <install_plan_name> \
      -n <namespace> \
      --type merge \
      -p '{"spec":{"approved":true}}'
    ```

7.  Verify Operator health after cluster update by running the following command:

    ``` terminal
    $ oc get csv -A
    ```

    All Operators must show `Succeeded` phase.

8.  Verify CNF-specific Operator pods and custom resources by running the following commands:

    ``` terminal
    $ oc get pods -n openshift-sriov-network-operator
    $ oc get pods -n openshift-ptp
    $ oc get performanceprofile -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.conditions[?(@.type=="Applied")].status}{"\n"}{end}'
    $ oc get ptpconfig -n openshift-ptp
    $ oc get sriovnetworknodepolicy -n openshift-sriov-network-operator
    $ oc get sriovnetworknodepolicy -n openshift-sriov-network-operator -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.syncStatus}{"\n"}{end}'
    $ oc get pods -n openshift-ptp -l app=linuxptp-daemon -o wide
    ```

    All custom resources must show expected status.

    Review Operator considerations specific to your deployment:

    - Node Tuning Operator: The Node Tuning Operator provides performance tuning capabilities through `PerformanceProfile` custom resources. Verify that performance profiles are reconciled after the update.

    - SR-IOV Network Operator: The SR-IOV Network Operator might require node reboots when updating to new versions. Schedule Operator updates during maintenance windows to avoid unexpected node reboots.

    - PTP Operator: PTP configurations are sensitive to version changes. Validate PTP synchronization after Operator updates.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that all Operators and custom resources are healthy by running the following commands:

    ``` terminal
    $ oc get csv -A
    $ oc get pods -A | grep -E "openshift-sriov|openshift-ptp|openshift-performance"
    $ oc get performanceprofile,ptpconfig,sriovnetworknodepolicy -A
    ```

    All `ClusterServiceVersion` resources must show `Succeeded` phase. All Operator pods must be `Running` and ready. Custom resources must exist and show the expected configuration.

</div>

<div>

<div class="title">

Troubleshooting

</div>

- If an Operator blocks the cluster update, update the Operator subscription channel before updating the cluster.

- If an Operator is stuck in `Installing` phase, check catalog source availability by running the following command:

  ``` terminal
  $ oc get catalogsource -n openshift-marketplace
  ```

- If a custom resource is not reconciling, check Operator logs by running the following command:

  ``` terminal
  $ oc logs -n <operator_namespace> deployment/<operator_deployment>
  ```

- If Operator pods are in `CrashLoopBackOff`, check for compatibility issues with the new cluster version.

</div>

# Additional resources

- [Prepare RHACM policies and TALM for cluster updates](update-rhacm-talm-preparing-policies.md#core-cluster-upgrades-preparing-policies)

- [OpenShift Container Platform update documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/)
