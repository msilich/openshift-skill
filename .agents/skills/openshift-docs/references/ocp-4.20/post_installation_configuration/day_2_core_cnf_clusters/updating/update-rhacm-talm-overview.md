<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use Red Hat Advanced Cluster Management (RHACM) and Topology Aware Lifecycle Manager (TALM) to perform z-stream, y-stream, and EUS-to-EUS updates on spoke clusters managed from a hub cluster.

The policy-based update workflow uses update policies that you define on the RHACM hub while TALM orchestrates their enforcement across target clusters.

If you are managing a single cluster or troubleshooting a specific cluster directly, see "Updating an OpenShift Container Platform cluster" for manual updates of individual clusters.

# Policy-based cluster updates with RHACM and TALM

You can use Red Hat Advanced Cluster Management (RHACM) and Topology Aware Lifecycle Manager (TALM) to automate cluster updates across spoke clusters managed from a hub cluster.

Optionally, you can manage RHACM policies through a GitOps workflow, storing them in a Git repository for versioning, review, and auditability.

RHACM provides the policy framework for managing cluster configuration across a fleet of spoke clusters from a central hub cluster. You define RHACM policies that declare the target cluster version, and RHACM evaluates compliance across target clusters.

TALM orchestrates the rollout of RHACM policies to target clusters according to your batching strategy. TALM uses `ClusterGroupUpgrade` custom resources (CRs) to coordinate which clusters to update, which policies to apply, and how to manage concurrency. A `ClusterGroupUpgrade` CR progresses through several states during an update:

- `Preparing`: Cluster readiness and policy compliance are being evaluated.

- `InProgress`: Policies are being applied to clusters in batches.

- `Complete`: All clusters are successfully updated and compliant.

- `Failed`: One or more clusters failed to update.

# Benefits of TALM for large-scale deployments

Topology Aware Lifecycle Manager (TALM) is specifically designed for large-scale deployments with many clusters across many sites.

With TALM, you can do the following:

- Update hundreds or thousands of clusters from a central hub.

- Test updates on a single target cluster before rolling out to the fleet.

- Schedule updates during planned downtime using blocking custom resources.

- Manage update policies through existing GitOps tools, such as Argo CD, and the same workflows and approval processes you already use for cluster configuration.

# GitOps workflows for RHACM update policies

GitOps provides a declarative approach to managing cluster configuration and lifecycle operations. You define the desired state of your clusters in Git, and automation tools ensure the actual state matches the desired state.

For cluster updates, the GitOps workflow begins with defining the desired cluster version as a policy in a Git repository. After committing and pushing the policy changes through your review process, you apply the policy to the RHACM hub cluster. TALM then orchestrates the rollout to target clusters according to your batching strategy, using `ClusterGroupUpgrade` custom resources (CRs). You can monitor progress and verify successful updates throughout the process.

With a GitOps workflow for cluster updates, you can do the following:

- Track changes through Git commit history for full audit trails.

- Review policy changes through pull requests before application.

- Revert to previous policy versions if needed.

- Maintain consistent update configurations across all clusters.

# Cluster update scenarios

You can perform z-stream, y-stream, and EUS-to-EUS updates on clusters managed by Red Hat Advanced Cluster Management (RHACM) and Topology Aware Lifecycle Manager (TALM). Each update scenario has different risk profiles, release cadences, and use cases that align with your operational requirements and maintenance windows.

## Z-stream updates

Z-stream updates apply patch releases within a minor version, such as updating from 4.20.0 to 4.20.1. These updates address security vulnerabilities and bug fixes without introducing new features.

Z-stream releases follow a weekly cadence and should be applied as soon as they become available. The risk profile for z-stream updates is low because they do not include API changes or feature modifications.

The following list describes use cases for z-stream updates:

- Applying critical security patches (CVEs)

- Resolving production bugs identified in the current minor version

- Maintaining compliance with security policies that require timely patching

- Performing regular maintenance updates during normal operating windows

When configured with proper pod disruption budgets, z-stream updates cause minimal workload disruption. Control plane nodes update in a rolling fashion, and worker nodes update one at a time or in small batches.

## Y-stream updates

Y-stream updates move between minor versions, such as updating from 4.20.x to 4.21.0. These updates introduce new features, performance improvements, and might include API deprecations.

Typically, Y-stream releases follow a four-month release cadence. You must update through consecutive y-stream versions and cannot skip versions. For example, to update from 4.20 to 4.22, you must update from 4.20 to 4.21, and then from 4.21 to 4.22. If you need to move 2 y-stream versions, consider EUS-to-EUS updates instead.

The risk profile for y-stream updates is medium because they might include deprecated APIs and configuration changes. Review release notes carefully before updating to identify breaking changes that affect your workloads.

The following list describes use cases for y-stream updates:

- Accessing new OpenShift Container Platform features and capabilities

- Maintaining support lifecycle compliance because older versions eventually lose support

- Meeting requirements for updated Operator versions

- Adopting performance improvements and optimizations

Y-stream updates require a planned maintenance window. The control plane update typically completes in 60 to 120 minutes, and worker node updates take an additional 30 to 60 minutes. You can minimize workload disruption by pausing worker nodes and updating the control plane first.

<div>

<div class="title">

Additional resources

</div>

- [EUS-to-EUS updates](#core-cluster-upgrade-scenario-eus_core-cluster-upgrades-overview)

</div>

## EUS-to-EUS updates

Extended Update Support (EUS) releases receive 18 months of support and include even-numbered minor versions such as 4.18, 4.20, and 4.22. With EUS-to-EUS updates, the worker nodes in your cluster can jump versions, reducing your upgrade timeline.

With control-plane-only updates, you can update the control plane to a new EUS version while leaving worker nodes at the previous version. The control plane and workers can be up to two minor versions apart during this staged approach.

The risk profile for EUS-to-EUS updates is medium to high because they involve larger version jumps. Thorough testing and validation are critical before performing EUS-to-EUS updates in production.

The following list describes use cases for EUS-to-EUS updates:

- Staging control plane updates separately from worker node updates

- Minimizing workload disruption by deferring worker updates to a later maintenance window

- Aligning updates with long-term support cycles that have 18-month support windows

- Managing capacity-constrained environments where full cluster downtime is not feasible

Control-plane-only EUS updates affect only control plane components. Workloads continue running on worker nodes at the previous version. Worker nodes can be updated days or weeks after the control plane, depending on your maintenance schedule.

## Selecting an update scenario

The following decision matrix helps you determine which update scenario to use:

| Scenario | When to use | Key considerations |
|----|----|----|
| Z-stream | Security patches or bug fixes needed | Apply weekly. Minimal risk and minimal downtime. |
| Y-stream | New features required or approaching end of support | Typically a four-month cadence. Review release notes and plan a maintenance window. |
| EUS-to-EUS | Long-term planning with staged rollouts | 18-month support. Control plane and workers can update separately. Larger version jumps require more validation. |

Decision matrix for update scenarios

## Application and cluster configuration policy changes

In addition to OpenShift Container Platform and OLM Operator update policies, review and prepare policies for application and cluster configuration changes that the update might require.

This can include changes to user policies, security context constraints (SCCs), or version-specific configuration for your cluster.

For further policy configuration, see the Red Hat Advanced Cluster Management (RHACM) documentation.

# Additional resources

- [Updating an OpenShift Container Platform cluster](update-welcome.md#update-welcome)

- [Verifying cluster API versions between update versions](update-api.md#update-api)

- [Using the Topology Aware Lifecycle Manager for cluster updates](../../../edge_computing/cnf-talm-for-cluster-upgrades.md#cnf-talm-for-cluster-updates)

- [Bare metal Core reference design specifications](../../../scalability_and_performance/telco-core-rds.md#telco-core-ref-design-specs)

- [How to use the Topology Aware Lifecycle Manager](https://www.redhat.com/en/blog/how-to-use-the-topology-aware-lifecycle-manager)

- [The ultimate guide to OpenShift release and update process for cluster administrators](https://www.redhat.com/en/blog/the-ultimate-guide-to-openshift-release-and-upgrade-process-for-cluster-administrators)

- [OpenShift Container Platform update documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/)

- [OpenShift Container Platform update lifecycle and support policy](https://access.redhat.com/support/policy/updates/openshift)
