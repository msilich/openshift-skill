<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you update your OpenShift Container Platform cluster, complete the required administrative tasks and review best practices to minimize disruption and avoid update failures.

# Kubernetes API removals

There are no Kubernetes API removals in this release.

# Providing an administrator acknowledgment for Microsoft Azure or VMware vSphere clusters

If you are updating a Microsoft Azure or VMware vSphere cluster from OpenShift Container Platform 4.21 to 4.22, and you have not configured the `managedBootImages` parameter, the update is blocked with a "*This cluster is Azure or vSphere but lacks a boot image configuration.*" message.

The update is blocked intentionally on Azure or vSphere clusters in order to alert you that the default updated boot image behavior is changing between version 4.21 and 4.22 to enable updated boot images by default on those platforms.

To allow the update, you must perform one of the following tasks:

- If you want to allow the feature to be enabled, you must provide an administrator acknowledgment as described in the following procedure before you can update your cluster.

- If you do not want the updated boot image feature enabled, you must explicitly disable the feature for compute nodes and then update your cluster. For more information, see "Disabling boot image management".

<div>

<div class="title">

Prerequisite

</div>

- You must have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Acknowledge that you are aware of the change in the default behavior by running the following command:

  ``` terminal
  $ oc -n openshift-config patch cm admin-acks --patch '{"data":{"ack-4.21-boot-image-opt-out-in-4.22":"true"}}' --type=merge
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Disabling boot image management](../../nodes/nodes/nodes-update-boot-images.md#mco-update-boot-images-disable_nodes-update-boot-images)

</div>

# Self-service Technical Supportability Review

You can use the self-service Technical Supportability Review (TSR) on the Red Hat Customer Portal to validate your cluster configuration against Red Hat common practices.

> [!NOTE]
> The `must-gather` tool collects diagnostic information about your cluster, including resource definitions, service logs, and configuration data. For more information, see "Gathering data about your cluster" in the OpenShift Container Platform documentation.

The self-service TSR uses AI to evaluate your cluster’s `must-gather` data and provides a prioritized executive summary of recommendations. This serves as a starting point to help you identify and resolve potential issues before they impact your environment.

The TSR performs hundreds of checks across the OpenShift Container Platform platform, including OpenShift Virtualization. Coverage is continually expanding.

## When to use the self-service TSR tool

Integrating the self-service TSR into your regular operational workflow can be helpful in the following scenarios:

Routine benchmarking
Use the TSR quarterly to benchmark cluster health and plan for routine maintenance activities.

Pre-flight checks
Validate your cluster configuration before major structural changes, including upgrades, migrations, and expansions.

Critical event preparation
Confirm cluster stability ahead of high-traffic business events, such as seasonal peaks, or operational milestones, such as year-end shutdowns, business continuity drills, and compliance audits.

## How to access the TSR

To run a self-service review, upload your cluster’s `must-gather` data to the **Analyze** tab in the **Support** section of the Red Hat Customer Portal. For a direct link, see "Technical Supportability Review with AI tool" in the Additional resources section. The **Analyze** feature generates a prioritized executive summary that identifies your cluster’s top risks and recommends corrective actions. Review the recommendations and implement the suggested corrective actions to address the identified risks.

The self-service TSR provides a solid baseline for cluster health. If you need additional guidance or a more comprehensive review, contact your Red Hat account team to arrange an assisted review through a Technical Account Manager (TAM) or Red Hat consultant. An assisted review includes human analysis, deeper coverage, and access to checks that are updated more frequently than the self-service version.

<div>

<div class="title">

Additional resources

</div>

- [Technical Supportability Review with AI tool](https://access.redhat.com/support/cases/#/analyze)

- [Red Hat Technical Supportability Review with AI: Proactive AI-Driven Cluster Assessments for OpenShift Container Platform](https://access.redhat.com/solutions/7141255)

</div>

# The risk of conditional updates

Conditional updates are update targets flagged by the OpenShift Update Service (OSUS) as available but not recommended due to known risks that apply to your cluster.

The Cluster Version Operator (CVO) periodically queries the OSUS for the most recent data about update recommendations, and some potential update targets might have risks associated with them.

The CVO evaluates the conditional risks, and if the risks are not applicable to the cluster, then the target version is available as a recommended update path for the cluster. If the risk is determined to be applicable, or if for some reason CVO cannot evaluate the risk, then the update target is available to the cluster as a conditional update.

When you encounter a conditional update while you are trying to update to a target version, you must assess the risk of updating your cluster to that version. Generally, if you do not have a specific need to update to that target version, it is best to wait for a recommended update path from Red Hat.

However, if you have a strong reason to update to that version, for example, if you need to fix an important CVE, then the benefit of fixing the CVE might outweigh the risk of the update being problematic for your cluster. You can complete the following tasks to determine whether you agree with the Red Hat assessment of the update risk:

- Complete extensive testing in a non-production environment to the extent that you are comfortable completing the update in your production environment.

- Follow the links provided in the conditional update description, investigate the bug, and determine if it is likely to cause issues for your cluster. If you need help understanding the risk, contact Red Hat Support.

<div>

<div class="title">

Additional resources

</div>

- [Evaluation of update availability](../understanding_updates/how-updates-work.md#update-evaluate-availability_how-updates-work)

</div>

# etcd backups before cluster updates

Create etcd backups before you update clusters to preserve your cluster state and to enable disaster recovery.

etcd backups record the state of your cluster and all of its resource objects. You can use backups to try to restore the state of a cluster when the cluster has become unrecoverable.

In the context of updates, you can attempt an etcd restoration of the cluster if an update introduced catastrophic conditions that cannot be fixed without reverting to the previous cluster version.

etcd restorations might be destructive and destabilizing to a running cluster, use them only as a last resort.

> [!WARNING]
> Due to their high consequences, etcd restorations are not intended to be used as a rollback solution. Rolling your cluster back to a previous version is not supported. If your update is failing to complete, contact Red Hat support.

There are several factors that affect the viability of an etcd restoration. For more information, see "Backing up etcd data" and "Restoring to an earlier cluster state".

<div>

<div class="title">

Additional resources

</div>

- [Backing up etcd](../../backup_and_restore/control_plane_backup_and_restore/backing-up-etcd.md#backup-etcd)

- [Restoring to an earlier cluster state](../../backup_and_restore/control_plane_backup_and_restore/disaster_recovery/scenario-2-restoring-cluster-state.md#dr-restoring-cluster-state)

</div>

# Using the oc adm upgrade recommend command to identify update risks

To identify potential update risks before initiating a cluster update, you can use the `oc adm upgrade recommend` command.

When you run the `oc adm upgrade recommend` command, the output displays the following information:

- Any issues that cause the Cluster Version Operator to have a status of `Failing=True`

- Any firing alerts that might be a cause for concern about a cluster update

- Information about your current update channel and your cluster’s update service

- Recommended target versions and any relevant known issues associated with each version

You can use the information provided by the output to make informed decisions about the state of your cluster. Examples include whether any critical cluster issues should be addressed before attempting an update, or which specific target version would have less risk for your cluster.

> [!NOTE]
> The `oc adm upgrade recommend` command is read-only and does not affect the state of the cluster. To request an update, use the `oc adm upgrade` command.

<div>

<div class="title">

Prerequisites

</div>

- You installed the latest version of OpenShift CLI (`oc`).

- You are logged in with a token-based identity, such as `kubeadmin`, by using the `oc login` command.

  > [!NOTE]
  > The `oc adm upgrade recommend` command requires a bearer token to query the cluster’s Thanos monitoring service for firing alerts. Certificate-based authentication, such as the `system:admin` identity provided in the default `kubeconfig` file from the installation program, does not satisfy this requirement. If you use certificate-based authentication, the command output displays the following message and skips all alert-based precondition checks:
  >
  > ``` terminal
  > Failed to check for at least some preconditions: no token is currently in use for this session
  > ```

</div>

<div>

<div class="title">

Procedure

</div>

- Identify potential update risks and view recommended update versions by running the following command:

  ``` terminal
  $ oc adm upgrade recommend
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  The following conditions found no cause for concern in updating this cluster to later releases: recommended/CriticalAlerts (AsExpected), recommended/NodeAlerts (AsExpected), recommended/PodDisruptionBudgetAlerts (AsExpected), recommended/PodImagePullAlerts (AsExpected), recommended/UpdatePrecheckAlerts (AsExpected)

  Upstream update service is unset, so the cluster will use an appropriate default.
  Channel: stable-4.21 (available channels: candidate-4.20, candidate-4.21, candidate-4.22, eus-4.20, fast-4.20, fast-4.21, stable-4.20, stable-4.21)

  Updates to 4.21:
    VERSION     ISSUES
    4.21.14     no known issues relevant to this cluster
    4.21.13     no known issues relevant to this cluster
  And 2 older 4.21 updates you can see with '--show-outdated-releases' or '--version VERSION'.

  Updates to 4.20:
    VERSION     ISSUES
    4.20.20     no known issues relevant to this cluster
  ```

  </div>

</div>

## Adding custom alerts to oc adm upgrade recommend command output

You can configure specific alerts to be checked by the `oc adm upgrade recommend` command, so that if they are firing they appear in the output of the command. To do this, add the `openShiftUpdatePrecheck` label to an alert and set it to true.

<div>

<div class="title">

Procedure

</div>

1.  Edit a `PrometheusRule` custom resource (CR) by running the following command:

    ``` terminal
    $ oc edit prometheusrule <rule_name> -n <namespace>
    ```

    where:

    `<rule_name>`
    Specifies the name of the `PrometheusRule` CR.

    `<namespace>`
    Specifies the namespace that contains the CR.

2.  Add the following snippet to the `labels` section of the alert you want to be checked by the `oc adm upgrade recommend` command:

    ``` yaml
    # ...
         labels:
           openShiftUpdatePrecheck: "true"
    # ...
    ```

    <div class="formalpara">

    <div class="title">

    Example `PrometheusRule` CR with precheck label

    </div>

    ``` yaml
    apiVersion: monitoring.coreos.com/v1
    kind: PrometheusRule
    metadata:
      name: storage-warning-alerts
      namespace: openshift-monitoring
    spec:
      groups:
      - name: disk-usage-warnings
        rules:
        - alert: VolumeNearingCapacity
          expr: (kubelet_volume_stats_used_bytes / kubelet_volume_stats_capacity_bytes) > 0.85
          for: 15m
          labels:
            severity: warning
            openShiftUpdatePrecheck: "true"
          annotations:
            summary: "Storage volume is over 85% full"
            description: "The volume {{ $labels.persistentvolumeclaim }} in namespace {{ $labels.namespace }} is currently {{ $value | humanizePercentage }} full. This may cause issues during pod restarts or cluster updates."
    ```

    </div>

</div>

## Accepting risks with the oc adm upgrade recommend command

You can use a command flag to explicitly accept update risks that are shown in the output of the `oc adm upgrade recommend` command.

<div>

<div class="title">

Procedure

</div>

1.  Check for update risks by running the following command:

    ``` terminal
    $ oc adm upgrade recommend
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    The following conditions found no cause for concern in updating this cluster to later releases: recommended/CriticalAlerts (AsExpected), recommended/NodeAlerts (AsExpected), recommended/PodDisruptionBudgetAlerts (AsExpected), recommended/PodImagePullAlerts (AsExpected)

    The following conditions found cause for concern in updating this cluster to later releases: recommended/UpdatePrecheckAlerts/TestAlert/0

    recommended/UpdatePrecheckAlerts/TestAlert/0=False:

      Reason: Alert:firing
      Message: warning alert TestAlert firing, suggesting issues worth investigating before updating the cluster. Test alert for updates. The alert description is: Test alert for updates <alert does not have a runbook_url annotation>

    Upstream update service is unset, so the cluster will use an appropriate default.
    Channel: stable-4.21 (available channels: candidate-4.20, candidate-4.21, candidate-4.22, eus-4.20, fast-4.20, fast-4.21, stable-4.20, stable-4.21)

    Updates to 4.21:
      VERSION     ISSUES
      4.21.14     no known issues relevant to this cluster
      4.21.13     no known issues relevant to this cluster
    And 2 older 4.21 updates you can see with '--show-outdated-releases' or '--version VERSION'.

    Updates to 4.20:
      VERSION     ISSUES
      4.20.20     no known issues relevant to this cluster
    ```

    </div>

    In this example, `TestAlert` is the name of the alert that is firing on the cluster and is considered a risk to a cluster update. Alerts that are identified as update risks might be changed over time.

2.  Accept update risks by running the following command:

    ``` terminal
    $ oc adm upgrade recommend --accept <risk_name>
    ```

    Replace `<risk_name>` with the name of the risk you want to accept. You can accept multiple risks at once by separating each risk by a comma, for example `risk1,risk2,risk3`.

    <div class="formalpara">

    <div class="title">

    Example command

    </div>

    ``` terminal
    $ oc adm upgrade recommend --accept TestAlert
    ```

    </div>

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    The following conditions found no cause for concern in updating this cluster to later releases: recommended/CriticalAlerts (AsExpected), recommended/NodeAlerts (AsExpected), recommended/PodDisruptionBudgetAlerts (AsExpected), recommended/PodImagePullAlerts (AsExpected)

    The following conditions found cause for concern in updating this cluster to later releases, but were explicitly accepted via --accept: recommended/UpdatePrecheckAlerts/TestAlert/0

    Upstream update service is unset, so the cluster will use an appropriate default.
    Channel: stable-4.21 (available channels: candidate-4.20, candidate-4.21, candidate-4.22, eus-4.20, fast-4.20, fast-4.21, stable-4.20, stable-4.21)

    Updates to 4.21:
      VERSION     ISSUES
      4.21.14     no known issues relevant to this cluster
      4.21.13     no known issues relevant to this cluster
    And 2 older 4.21 updates you can see with '--show-outdated-releases' or '--version VERSION'.

    Updates to 4.20:
      VERSION     ISSUES
      4.20.20     no known issues relevant to this cluster
    ```

    </div>

</div>

# Best practices for cluster updates

Follow best practices to ensure successful cluster updates. These best practices include selecting recommended versions, resolving critical alerts, maintaining spare node capacity, and properly configuring pod disruption budgets.

OpenShift Container Platform minimizes workload disruptions during an update. Updates do not begin unless the cluster is in an upgradeable state at the time of the update request.

This design enforces some key conditions before initiating an update, but there are several actions you can take to increase your chances of a successful cluster update.

## Choose versions recommended by the OpenShift Update Service

The OpenShift Update Service (OSUS) provides update recommendations based on cluster characteristics such as the cluster’s subscribed channel. The Cluster Version Operator saves these recommendations as either recommended or conditional updates.

While it is possible to attempt an update to a version that is not recommended by OSUS, following a recommended update path protects users from encountering known issues or unintended consequences on the cluster.

Choose only update targets that are recommended by OSUS to ensure a successful update.

## Address all critical alerts on the cluster

Critical alerts must always be addressed as soon as possible, but it is especially important to address these alerts and resolve any problems before initiating a cluster update.

Failing to address critical alerts before beginning an update can cause problematic conditions for the cluster.

In the **Administrator** perspective of the web console, navigate to **Observe** → **Alerting** to find critical alerts.

## Ensure that the cluster is in an Upgradeable state

When one or more Operators have not reported their `Upgradeable` condition as `True` for more than an hour, the `ClusterNotUpgradeable` warning alert is triggered in the cluster. In most cases this alert does not block patch updates, but you cannot perform a minor version update until you resolve this alert and all Operators report `Upgradeable` as `True`.

For more information about the `Upgradeable` condition, see "Understanding cluster Operator condition types" in the additional resources section.

## SDN support removal

OpenShift SDN network plugin was deprecated in versions 4.15 and 4.16. With this release, the SDN network plugin is no longer supported and the content has been removed from the documentation.

If your OpenShift Container Platform cluster is still using the OpenShift SDN CNI, see [Migrating from the OpenShift SDN network plugin](https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html/networking/ovn-kubernetes-network-plugin#migrate-from-openshift-sdn).

> [!IMPORTANT]
> It is not possible to update a cluster to OpenShift Container Platform 4.17 if it is using the OpenShift SDN network plugin. You must migrate to the OVN-Kubernetes plugin before upgrading to OpenShift Container Platform 4.17.

## Ensure that enough spare nodes are available

A cluster should not be running with little to no spare node capacity, especially when initiating a cluster update. Nodes that are not running and available may limit a cluster’s ability to perform an update with minimal disruption to cluster workloads.

Depending on the configured value of the cluster’s `maxUnavailable` spec, the cluster might not be able to apply machine configuration changes to nodes if there is an unavailable node. Additionally, if compute nodes do not have enough spare capacity, workloads might not be able to temporarily shift to another node while the first node is taken offline for an update.

Make sure that you have enough available nodes in each worker pool, as well as enough spare capacity on your compute nodes, to increase the chance of successful node updates.

> [!WARNING]
> The default setting for `maxUnavailable` is `1` for all the machine config pools in OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to `3` for the control plane pool.

## Ensure that the cluster’s PodDisruptionBudget is properly configured

You can use the `PodDisruptionBudget` object to define the minimum number or percentage of pod replicas that must be available at any given time. This configuration protects workloads from disruptions during maintenance tasks such as cluster updates.

However, it is possible to configure the `PodDisruptionBudget` for a given topology in a way that prevents nodes from being drained and updated during a cluster update.

When planning a cluster update, check the configuration of the `PodDisruptionBudget` object for the following factors:

- For highly available workloads, make sure there are replicas that can be temporarily taken offline without being prohibited by the `PodDisruptionBudget`.

- For workloads that are not highly available, make sure they are either not protected by a `PodDisruptionBudget` or have some alternative mechanism for draining these workloads eventually, such as periodic restart or guaranteed eventual termination.

<div>

<div class="title">

Additional resources

</div>

- [Understanding cluster Operator condition types](../understanding_updates/intro-to-updates.md#understanding_clusteroperator_conditiontypes_understanding-openshift-updates)

</div>

# Minimizing worker node deployment time

You can minimize deployment time during cluster worker node installation by applying configuration changes across nodes simultaneously.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the configuration file for your required installation method (`install-config.yaml` or similar).

- You have the OpenShift CLI (`oc`) installed.

- You have the OpenShift installation program (`openshift-install`) installed.

- You have access to the cluster as a user with the `cluster-admin` role.

- You create more than one worker Machine Configuration Pool (MCP) in the cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a MCP YAML file for each custom worker MCP that you intend to use, as in the following example:

    ``` yaml
    apiVersion: machineconfiguration.openshift.io/v1
    kind: MachineConfigPool
    metadata:
      name: worker-0
      labels:
        machineconfiguration.openshift.io/role: worker-0
    spec:
      machineConfigSelector:
        matchExpressions:
          - key: machineconfiguration.openshift.io/role
            operator: In
            values: [ worker, worker-0 ]
      paused: false
      maxUnavailable: 100%
      nodeSelector:
        matchLabels:
          node-role.kubernetes.io/worker-0: ""
    ```

    Ensure the following configurations are present:

    - **maxUnavailable**: Set this value to `100%`. This setting ensures that all nodes within this specific MCP update concurrently during the initial deployment. By default, `maxUnavailable` is set to 1, causing all nodes within this specific MCP to update sequentially during the initial deployment.

    - **nodeSelector**: Define a unique label, such as `node-role.kubernetes.io/worker-0`, to bind specific nodes to this pool.

    - **paused**: Set this value to `true` if you plan to apply additional Day 2 configurations, such as `PerformanceProfile`, after installation. All Day 2 configurations can be applied while the MCP is paused. They will be queued and applied when you unpause the node. Set this value to `false` if no further configurations are required.

      > [!NOTE]
      > For bare-metal servers, the reboot time can take up to a couple of minutes.

2.  Place the YAML files in the directory generated by the installation program. Ensure that your worker nodes get assigned the correct labels, such as `node-role.kubernetes.io/worker-0`, during the provisioning phase or immediately upon joining.

    > [!NOTE]
    > Proper labeling ensures that the nodes get assigned to the correct custom MCP rather than the default worker pool.

3.  Optional: If you set the `paused` parameter to `true` to apply additional configurations, complete the following steps:

    1.  Apply your Day 2 configuration.

    2.  Unpause the MCPs to start the configuration phase and reboot if needed. Clusters must be deployed to access the API and run `oc` commands:

        ``` terminal
        $ oc patch mcp/worker-0 --patch '{"spec":{"paused":false}}' --type=merge
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        machineconfigpool.machineconfiguration.openshift.io/worker-0 patched
        ```

        </div>

        > [!NOTE]
        > If you did not set the `paused` parameter to `true`, the configuration will apply sequentially and reboot if needed.

4.  Verify that the MCPs updated successfully:

    ``` terminal
    $ oc get machineconfigpools
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME       CONFIG                                           UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
    master     rendered-master-b0bb90c4921860f2a5d8a2f8137c1867 True      False      False      3              3                   3                     0                      97m
    worker-0   rendered-worker-config-new                       False     True       False      10             0                   0                     0                      5m
    ```

    </div>

5.  When all MCPs are set to `UPDATED=true`, update the MCPs with the appropriate `maxUnavailable` based on workload requirements. This ensures cluster stability and high availability when users deploy workloads onto the cluster. For example, set `maxUnavailable` to 1 by running the following command:

    ``` terminal
    $ oc patch mcp/worker-0 --patch '{"spec":{"maxUnavailable":1}}' --type=merge
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    machineconfigpool.machineconfiguration.openshift.io/worker-0 patched
    ```

    </div>

</div>
