<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can update clusters to z-stream patch releases by using RHACM policies and Topology Aware Lifecycle Manager (TALM).

# Updating clusters with z-stream releases

You can update clusters to z-stream patch releases by using RHACM policies and Topology Aware Lifecycle Manager (TALM). Z-stream updates apply security fixes and bug fixes with minimal risk and should be performed regularly to maintain cluster security.

Apply z-stream updates as soon as they become available to address critical vulnerabilities and maintain security compliance.

> [!NOTE]
> The following procedure uses `spoke1` and `spoke2` as example cluster names. Replace these with your actual cluster names throughout.

<div>

<div class="title">

Prerequisites

</div>

- You have completed the pre-update health check successfully.

- TALM is installed and configured on the Red Hat Advanced Cluster Management (RHACM) hub cluster.

- A z-stream patch release is available on the Red Hat Customer Portal.

- A recent etcd backup exists that was created within the past 24 hours.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify the current cluster version by running the following command:

    ``` terminal
    $ oc get clusterversion
    ```

    The following example shows the output:

    ``` terminal
    NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
    version   4.20.0    True        False         30d     Cluster version is 4.20.0
    ```

2.  Check for available z-stream updates by running the following command:

    ``` terminal
    $ oc adm upgrade
    ```

    The following example shows the output:

    ``` terminal
    Cluster version is 4.20.0

    Upstream is unset, so the cluster will use an appropriate default.
    Channel: stable-4.20 (available channels: candidate-4.20, eus-4.20, fast-4.20, stable-4.20)

    Recommended updates:

      VERSION     IMAGE
      4.20.1      quay.io/openshift-release-dev/ocp-release@sha256:abc123...
      4.20.2      quay.io/openshift-release-dev/ocp-release@sha256:def456...
    ```

    Review the OpenShift Container Platform release notes for the target version to identify security fixes and bug fixes included in the z-stream release.

3.  Create a RHACM policy for the z-stream update:

    ``` yaml
    apiVersion: policy.open-cluster-management.io/v1
    kind: Policy
    metadata:
      name: core-upgrade-4.20.1-policy
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
                  channel: stable-4.20
                  desiredUpdate:
                    version: 4.20.1
    ```

    Replace `4.20.1` with your target z-stream version. The policy is set to `inform` so it does not immediately push the update. The `ClusterGroupUpgrade` custom resource (CR) enforces the policy at the scheduled update time.

4.  Apply the policy to the RHACM hub cluster by running the following command:

    ``` terminal
    $ oc apply -f core-upgrade-4.20.1-policy.yaml
    ```

5.  Verify the policy and placement resources were created by running the following commands:

    ``` terminal
    $ oc get policy core-upgrade-4.20.1-policy -n openshift-upgrade-policies
    $ oc get placementbinding -n openshift-upgrade-policies
    $ oc get placement -n openshift-upgrade-policies
    ```

    The following example shows the output:

    ``` terminal
    NAME                           REMEDIATION ACTION   COMPLIANCE STATE   AGE
    core-upgrade-4.20.1-policy    inform               NonCompliant       30s
    ```

    If no `PlacementBinding` or `Placement` exists, the policy will not apply to any clusters. Create appropriate placement resources for your target clusters.

6.  Create a `ClusterGroupUpgrade` CR for the z-stream update:

    ``` yaml
    apiVersion: ran.openshift.io/v1alpha1
    kind: ClusterGroupUpgrade
    metadata:
      name: core-zstream-upgrade-4.20.1
      namespace: openshift-upgrade-policies
    spec:
      clusters:
      - spoke1
      - spoke2
      managedPolicies:
      - core-upgrade-4.20.1-policy
      enable: false
      remediationStrategy:
        maxConcurrency: 2
        timeout: 60
    ```

    where:

    - `clusters`: Specifies your target cluster names.

    - `maxConcurrency`: Specifies the number of clusters to update simultaneously.

    - `timeout`: Specifies the maximum time in minutes to wait for each cluster update. For example, 60 equals 1 hour per cluster.

7.  Apply and enable the `ClusterGroupUpgrade` CR to start the update by running the following commands:

    ``` terminal
    $ oc apply -f core-zstream-cgu.yaml
    $ oc patch cgu core-zstream-upgrade-4.20.1 \
      -n openshift-upgrade-policies \
      --type merge \
      -p '{"spec":{"enable":true}}'
    ```

8.  Monitor the update progress by running the following commands:

    ``` terminal
    $ oc get cgu core-zstream-upgrade-4.20.1 -n openshift-upgrade-policies -w
    $ oc --context=spoke1 get clusterversion -w
    $ oc --context=spoke1 get co
    ```

    The `ClusterGroupUpgrade` CR progresses through these states:

    - `Preparing`: TALM validates cluster readiness

    - `InProgress`: Clusters are updating

    - `Complete`: All clusters successfully updated

    Operators update sequentially during the z-stream update.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify the cluster version and Operator health by running the following commands:

    ``` terminal
    $ oc --context=spoke1 get clusterversion -o jsonpath='{.items[0].status.desired.version}'
    $ oc --context=spoke1 get co
    ```

    The cluster version must show the target z-stream version. All Operators must show `AVAILABLE=True`, `PROGRESSING=False`, `DEGRADED=False`.

2.  Check workload health by running the following command:

    ``` terminal
    $ oc --context=spoke1 get pods -A | grep -v Running | grep -v Completed
    ```

    Pods must not show unexpected failures or crash loops.

3.  Verify CNF-specific resources by running the following commands:

    ``` terminal
    $ oc --context=spoke1 get performanceprofile
    $ oc --context=spoke1 get ptpconfig -n openshift-ptp
    $ oc --context=spoke1 get sriovnetworknodepolicy -n openshift-sriov-network-operator
    ```

    All custom resources must show expected status.

4.  Run smoke tests for critical workloads to ensure functionality after the update.

</div>

<div>

<div class="title">

Troubleshooting

</div>

- If the `ClusterGroupUpgrade` CR is stuck in `Preparing` state, check policy compliance in RHACM by running the following command:

  ``` terminal
  $ oc get policy core-upgrade-4.20.1-policy -n openshift-upgrade-policies
  ```

- If a cluster Operator becomes degraded during the update, check Operator logs by running the following command:

  ``` terminal
  $ oc --context=spoke1 logs -n openshift-<operator_namespace> deployment/<operator_deployment>
  ```

- If the update exceeds the timeout, investigate slow nodes or image pull issues by running the following command:

  ``` terminal
  $ oc --context=spoke1 get events -A --sort-by='.lastTimestamp' | tail -20
  ```

</div>

# Additional resources

- [Prepare RHACM policies and TALM for cluster updates](update-rhacm-talm-preparing-policies.md#core-cluster-upgrades-preparing-policies)

- [Perform health checks before a cluster update with TALM](update-rhacm-talm-health-checks.md#core-cluster-upgrades-health-checks)

- [Troubleshoot cluster updates with TALM](update-rhacm-talm-troubleshooting.md#core-cluster-upgrades-troubleshooting)

- [OpenShift Container Platform update documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/)

- [OpenShift Container Platform update lifecycle and support policy](https://access.redhat.com/support/policy/updates/openshift)
