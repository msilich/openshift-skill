<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

With OpenShift Container Platform 4, you can update an OpenShift Container Platform cluster with a single operation by using the web console or the OpenShift CLI (`oc`).

Platform administrators can view new update options either by going to **Administration** → **Cluster Settings** in the web console or by looking at the output of the `oc adm upgrade` command.

# Cluster update overview

OpenShift Container Platform updates involve several services, Operators, and processes working in tandem to change the cluster to the desired version.

Red Hat hosts a public OpenShift Update Service (OSUS), which serves a graph of update possibilities based on the OpenShift Container Platform release images in the official registry. The graph contains update information for any public release. OpenShift Container Platform clusters are configured to connect to the OSUS by default, and the OSUS responds to clusters with information about known update targets.

An update begins when either a cluster administrator or an automatic update controller edits the custom resource (CR) of the Cluster Version Operator (CVO) with a new version. To reconcile the cluster with the newly specified version, the CVO retrieves the target release image from an image registry and begins to apply changes to the cluster.

> [!NOTE]
> Operators previously installed through Operator Lifecycle Manager (OLM) follow a different process for updates. See [Updating installed Operators](../../operators/admin/olm-upgrading-operators.md#olm-upgrading-operators) for more information.

The target release image contains manifest files for all cluster components that form a specific OCP version. When updating the cluster to a new version, the CVO applies manifests in separate stages called Runlevels. Most, but not all, manifests support one of the cluster Operators. As the CVO applies a manifest to a cluster Operator, the Operator might perform update tasks to reconcile itself with its new specified version.

The CVO monitors the state of each applied resource and the states reported by all cluster Operators. The CVO only proceeds with the update when all manifests and cluster Operators in the active Runlevel reach a stable condition. After the CVO updates the entire control plane through this process, the Machine Config Operator (MCO) updates the operating system and configuration of every node in the cluster.

# Common questions about update availability

There are several factors that affect if and when an update is made available to an OpenShift Container Platform cluster.

The following list provides common questions regarding the availability of an update:

**What are the differences between each of the update channels?**

- A new release is initially added to the `candidate` channel.

- After successful final testing, a release on the `candidate` channel is promoted to the `fast` channel, an errata is published, and the release is now fully supported.

- After a delay, a release on the `fast` channel is finally promoted to the `stable` channel. This delay represents the only difference between the `fast` and `stable` channels.

  > [!NOTE]
  > For the latest z-stream releases, this delay may generally be a week or two. However, the delay for initial updates to the latest minor version may take much longer, generally 45-90 days.

- Releases promoted to the `stable` channel are simultaneously promoted to the `eus` channel. The primary purpose of the `eus` channel is to serve as a convenience for clusters performing a Control Plane Only update.

**Is a release on the `stable` channel safer or more supported than a release on the `fast` channel?**

- If a regression is identified for a release on a `fast` channel, it will be resolved and managed to the same extent as if that regression was identified for a release on the `stable` channel.

- The only difference between releases on the `fast` and `stable` channels is that a release only appears on the `stable` channel after it has been on the `fast` channel for some time, which provides more time for new update risks to be discovered.

- A release that is available on the `fast` channel always becomes available on the `stable` channel after this delay.

**What does it mean if an update has known issues?**

- Red Hat continuously evaluates data from multiple sources to determine whether updates from one version to another have any declared issues. Identified issues are typically documented in the version’s release notes. Even if the update path has known issues, customers are still supported if they perform the update.

- Red Hat does not block users from updating to a certain version. Red Hat may declare conditional update risks, which may or may not apply to a particular cluster.

  - Declared risks provide cluster administrators more context about a supported update. Cluster administrators can still accept the risk and update to that particular target version.

**What if I see that an update to a particular release is no longer recommended?**

- If Red Hat removes update recommendations from any supported release due to a regression, a superseding update recommendation will be provided to a future version that corrects the regression. There may be a delay while the defect is corrected, tested, and promoted to your selected channel.

**How long until the next z-stream release is made available on the fast and stable channels?**

- While the specific cadence can vary based on a number of factors, new z-stream releases for the latest minor version are typically made available about every week. Older minor versions, which have become more stable over time, may take much longer for new z-stream releases to be made available.

  > [!IMPORTANT]
  > These are only estimates based on past data about z-stream releases. Red Hat reserves the right to change the release frequency as needed. Any number of issues could cause irregularities and delays in this release cadence.

- Once a z-stream release is published, it also appears in the `fast` channel for that minor version. After a delay, the z-stream release may then appear in that minor version’s `stable` channel.

<div>

<div class="title">

Additional resources

</div>

- [Understanding update channels and releases](understanding-update-channels-release.md#understanding-update-channels-releases)

</div>

# About the OpenShift Update Service

The OpenShift Update Service (OSUS) provides update recommendations to OpenShift Container Platform, including Red Hat Enterprise Linux CoreOS (RHCOS). It provides a graph, or diagram, that contains the *vertices* of component Operators and the *edges* that connect them.

The edges in the graph show which versions you can safely update to. The vertices are update payloads that specify the intended state of the managed cluster components.

The Cluster Version Operator (CVO) in your cluster checks with the OpenShift Update Service to see the valid updates and update paths based on current component versions and information in the graph. When you request an update, the CVO uses the corresponding release image to update your cluster. The release artifacts are hosted in Quay as container images.

To allow the OpenShift Update Service to provide only compatible updates, a release verification pipeline drives automation. Each release artifact is verified for compatibility with supported cloud platforms and system architectures, as well as other component packages. After the pipeline confirms the suitability of a release, the OpenShift Update Service notifies you that it is available.

The OpenShift Update Service (OSUS) supports a single-stream release model, where only one release version is active and supported at any given time. When a new release is deployed, it fully replaces the previous release.

The updated release provides support for upgrades from all OpenShift Container Platform versions starting after 4.8 up to the new release version.

> [!IMPORTANT]
> The OpenShift Update Service displays all recommended updates for your current cluster. If an update path is not recommended by the OpenShift Update Service, it might be because of a known issue related to the update path, such as incompatibility or availability.

Two controllers run during continuous update mode. The first controller continuously updates the payload manifests, applies the manifests to the cluster, and outputs the controlled rollout status of the Operators to indicate whether they are available, upgrading, or failed. The second controller polls the OpenShift Update Service to determine if updates are available.

> [!IMPORTANT]
> Only updating to a newer version is supported. Reverting or rolling back your cluster to a previous version is not supported. If your update fails, contact Red Hat support.

During the update process, the Machine Config Operator (MCO) applies the new configuration to your cluster machines. The MCO cordons the number of nodes specified by the `maxUnavailable` field on the machine configuration pool and marks them unavailable. By default, this value is set to `1`. The MCO updates the affected nodes alphabetically by zone, based on the `topology.kubernetes.io/zone` label. If a zone has more than one node, the oldest nodes are updated first. For nodes that do not use zones, such as in bare metal deployments, the nodes are updated by age, with the oldest nodes updated first. The MCO updates the number of nodes as specified by the `maxUnavailable` field on the machine configuration pool at a time. The MCO then applies the new configuration and reboots the machine.

> [!WARNING]
> The default setting for `maxUnavailable` is `1` for all the machine config pools in OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to `3` for the control plane pool.

If you use Red Hat Enterprise Linux (RHEL) machines as workers, the MCO does not update the kubelet because you must update the OpenShift API on the machines first.

With the specification for the new version applied to the old kubelet, the RHEL machine cannot return to the `Ready` state. You cannot complete the update until the machines are available. However, the maximum number of unavailable nodes is set to ensure that normal cluster operations can continue with that number of machines out of service.

The OpenShift Update Service is composed of an Operator and one or more application instances.

# Understanding cluster Operator condition types

The status of cluster Operators includes their condition type, which informs you of the current state of your Operator’s health.

The following definitions cover a list of some common ClusterOperator condition types. Operators that have additional condition types and use Operator-specific language have been omitted.

The Cluster Version Operator (CVO) is responsible for collecting the status conditions from cluster Operators so that cluster administrators can better understand the state of the OpenShift Container Platform cluster.

- Available: The condition type `Available` indicates that an Operator is functional and available in the cluster. If the status is `False`, at least one part of the operand is non-functional and the condition requires an administrator to intervene.

- Progressing: The condition type `Progressing` indicates that an Operator is actively rolling out new code, propagating configuration changes, or otherwise moving from one steady state to another.

  Operators do not report the condition type `Progressing` as `True` when they are reconciling a previous known state. If the observed cluster state has changed and the Operator is reacting to it, then the status reports back as `True`, since it is moving from one steady state to another.

- Degraded: The condition type `Degraded` indicates that an Operator has a current state that does not match its required state over a period of time. The period of time can vary by component, but a `Degraded` status represents persistent observation of an Operator’s condition. As a result, an Operator does not fluctuate in and out of the `Degraded` state.

  There might be a different condition type if the transition from one state to another does not persist over a long enough period to report `Degraded`. An Operator does not report `Degraded` during the course of a normal update. An Operator may report `Degraded` in response to a persistent infrastructure failure that requires eventual administrator intervention.

  > [!NOTE]
  > This condition type is only an indication that something may need investigation and adjustment. As long as the Operator is available, the `Degraded` condition does not cause user workload failure or application downtime.

- Upgradeable: The condition type `Upgradeable` indicates whether the Operator is safe to update based on the current cluster state. The message field contains a human-readable description of what the administrator needs to do for the cluster to successfully update. The CVO allows updates when this condition is `True`, `Unknown` or missing.

  When the `Upgradeable` status is `False`, only minor updates are impacted, and the CVO prevents the cluster from performing impacted updates unless forced.

# Understanding cluster version condition types

The Cluster Version Operator (CVO) monitors cluster Operators and other components, and is responsible for collecting the status of both the cluster version and its Operators. This status includes the condition type, which informs you of the health and current state of the OpenShift Container Platform cluster.

In addition to `Available`, `Progressing`, and `Upgradeable`, there are condition types that affect cluster versions and Operators.

- Failing: The cluster version condition type `Failing` indicates that a cluster cannot reach its desired state, is unhealthy, and requires an administrator to intervene.

- Invalid: The cluster version condition type `Invalid` indicates that the cluster version has an error that prevents the server from taking action. The CVO only reconciles the current state as long as this condition is set.

- RetrievedUpdates: The cluster version condition type `RetrievedUpdates` indicates whether or not available updates have been retrieved from the upstream update server. The condition is `Unknown` before retrieval, `False` if the updates either recently failed or could not be retrieved, or `True` if the `availableUpdates` field is both recent and accurate.

- ReleaseAccepted: The cluster version condition type `ReleaseAccepted` with a `True` status indicates that the requested release payload was successfully loaded without failure during image verification and precondition checking.

- ImplicitlyEnabledCapabilities: The cluster version condition type `ImplicitlyEnabledCapabilities` with a `True` status indicates that there are enabled capabilities that the user is not currently requesting through `spec.capabilities`. The CVO does not support disabling capabilities if any associated resources were previously managed by the CVO.

# Common terms

Some terms are commonly used in the context of OpenShift Container Platform updates, which might be useful to learn.

Control plane
The *control plane*, which is composed of control plane machines, manages the OpenShift Container Platform cluster. The control plane machines manage workloads on the compute machines, which are also known as worker machines.

Cluster Version Operator
The *Cluster Version Operator* (CVO) starts the update process for the cluster. It checks with OSUS based on the current cluster version and retrieves the graph which contains available or possible update paths.

Machine Config Operator
The *Machine Config Operator* (MCO) is a cluster-level Operator that manages the operating system and machine configurations. Through the MCO, platform administrators can configure and update systemd, CRI-O and Kubelet, the kernel, NetworkManager, and other system features on the worker nodes.

OpenShift Update Service
The *OpenShift Update Service* (OSUS) provides over-the-air updates to OpenShift Container Platform, including to Red Hat Enterprise Linux CoreOS (RHCOS). It provides a graph, or diagram, that contains the vertices of component Operators and the edges that connect them.

Channels
*Channels* declare an update strategy tied to minor versions of OpenShift Container Platform. The OSUS uses this configured strategy to recommend update edges consistent with that strategy.

Recommended update edge
A *recommended update edge* is a recommended update between OpenShift Container Platform releases. Whether a given update is recommended can depend on the cluster’s configured channel, current version, known bugs, and other information. OSUS communicates the recommended edges to the CVO, which runs in every cluster.

<div>

<div class="title">

Additional resources

</div>

- [Machine Config Overview](../../machine_configuration/index.md#machine-config-overview)

- [Using the OpenShift Update Service in a disconnected environment](../../disconnected/updating/disconnected-update-osus.md#update-service-overview_updating-disconnected-cluster-osus)

- [Update channels](understanding-update-channels-release.md#understanding-update-channels_understanding-update-channels-releases)

</div>

# Additional resources

- [How cluster updates work](how-updates-work.md#how-updates-work)
