<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can perform a network reconfiguration on a single-node OpenShift cluster by editing the `IPConfig` custom resource (CR) and transitioning through the configuration stages.

# Perform a single-node OpenShift network reconfiguration

You can change the network configuration of a single-node OpenShift cluster by editing the `IPConfig` custom resource (CR) and transitioning through the configuration stages.

<div>

<div class="title">

Prerequisites

</div>

- You have a single-node OpenShift cluster.

- You have installed the Lifecycle Agent.

- You have the new network configuration details, including IP addresses, gateways, and DNS servers.

- You have cluster administrator privileges.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that the `IPConfig` CR exists and check its current state by running the following command:

    ``` terminal
    $ oc get ipc ipconfig -o yaml
    ```

    If the CR does not exist, verify that you installed the Lifecycle Agent.

2.  Verify that the `spec.stage` field is set to `Idle`, the `Idle` status condition is set to `true`, and review the current network configuration in the `status` fields.

    > [!NOTE]
    > You can only modify spec fields when the CR is in the `Idle` stage.

3.  Edit the `IPConfig` CR to specify the new network configuration by running the following command:

    ``` terminal
    $ oc edit ipc ipconfig
    ```

4.  Update the spec fields with your new network configuration. The following example shows a dual-stack configuration with VLAN and DNS settings:

    ``` yaml
    apiVersion: lca.openshift.io/v1
    kind: IPConfig
    metadata:
      name: ipconfig
    spec:
      stage: Idle
      ipv4:
        address: 192.0.2.10
        machineNetwork: 192.0.2.0/24
        gateway: 192.0.2.1
      ipv6:
        address: 2001:db8::10
        machineNetwork: 2001:db8::/64
        gateway: 2001:db8::1
      dnsServers:
      - 192.0.2.53
      - 2001:4860:4860::8888
      vlanID: 100
      dnsFilterOutFamily: none
      autoRollbackOnFailure:
        initMonitorTimeoutSeconds: 1800
    ```

    where:

    `spec.stage`
    Set this field to `Config` when you are ready to apply the new network settings.

    `spec.ipv4.address`
    Specifies the target IPv4 address. Must be within the machine network CIDR.

    `spec.ipv4.machineNetwork`
    Specifies the target machine network CIDR.

    `spec.ipv4.gateway`
    Specifies the target default gateway.

    `spec.dnsServers`
    Specifies an ordered list of DNS servers. The first server in the list is used as the primary DNS server. Use a maximum of two servers.

    `spec.vlanID`
    Specifies an optional VLAN ID. Only specify if the cluster already has VLAN configuration.

    `spec.dnsFilterOutFamily`
    Specifies optional DNS filtering for dual-stack clusters. Set to `ipv4` or `ipv6` to filter out A or AAAA records respectively.

    `spec.autoRollbackOnFailure.initMonitorTimeoutSeconds`
    Specifies the timeout in seconds for automatic rollback if the configuration does not complete. The default value is 1800 seconds, or 30 minutes.

5.  After saving the configuration, change the stage to `Config` to start the network reconfiguration by running the following command:

    ``` terminal
    $ oc patch ipc ipconfig --type merge -p '{"spec":{"stage":"Config"}}'
    ```

    > [!NOTE]
    > After triggering the network reconfiguration, update your external DNS servers to resolve the cluster’s new API and ingress endpoints.

6.  Monitor the progress of the configuration by running the following command:

    ``` terminal
    $ oc get ipc ipconfig -o yaml
    ```

    Watch for the following progression:

    - The controller sets the `ConfigInProgress` condition

    - The pre-pivot phase runs and triggers a reboot

    - After reboot, the post-pivot phase applies the network changes

    - The controller waits for cluster stabilization

    - The `ConfigCompleted` condition is set when successful

7.  After the configuration completes successfully, verify that the `status.validNextStages` field includes `Idle` and `Rollback`.

8.  Verify the new network configuration by running the following command:

    ``` terminal
    $ oc get nodes -o wide
    ```

9.  Verify cluster health by running the following command:

    ``` terminal
    $ oc get clusteroperators
    ```

10. When you are satisfied with the new configuration, finalize the change by setting the stage to `Idle`. Run the following command:

    ``` terminal
    $ oc patch ipc ipconfig --type merge -p '{"spec":{"stage":"Idle"}}'
    ```

    > [!IMPORTANT]
    > After you finalize the configuration by transitioning to `Idle`, you cannot roll back to the previous network configuration. The old stateroot is removed during `Idle` state cleanup.

</div>

# Roll back a network reconfiguration

If you see issues after a network reconfiguration, you can roll back to an earlier network configuration. The rollback reboots the node into an earlier stateroot with the original network settings.

<div>

<div class="title">

Prerequisites

</div>

- You have completed a network reconfiguration that has not been finalized.

- The `status.validNextStages` field in the `IPConfig` customer resource (CR) includes `Rollback`.

- You have cluster administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that rollback stage is available by checking the `IPConfig` CR. Run the following command:

    ``` terminal
    $ oc get ipc ipconfig -o jsonpath='{.status.validNextStages}'
    ```

    Verify that the output includes `Rollback`.

2.  Check the rollback availability expiration timestamp by running the following command:

    ``` terminal
    $ oc get ipc ipconfig -o jsonpath='{.status.rollbackAvailabilityExpiration}'
    ```

    > [!NOTE]
    > Plan your rollback before this timestamp. After this timestamp, rolling back requires manual recovery because of expired control plane or kubelet certificates in the rollback stateroot.

3.  Trigger the rollback by setting the stage to `Rollback` by running the following command:

    ``` terminal
    $ oc patch ipc ipconfig --type merge -p '{"spec":{"stage":"Rollback"}}'
    ```

    The Lifecycle Agent reboots the node into the earlier stateroot.

4.  After the node reboots, monitor the rollback progress by running the following command:

    ``` terminal
    $ oc get ipc ipconfig -o yaml
    ```

    Wait for the `RollbackCompleted` condition to be set.

5.  Verify the node is using the original network configuration by running the following command:

    ``` terminal
    $ oc get nodes -o wide
    ```

6.  Finalize the rollback by setting the stage to `Idle` by running the following command:

    ``` terminal
    $ oc patch ipc ipconfig --type merge -p '{"spec":{"stage":"Idle"}}'
    ```

</div>

# Automatic rollback mechanisms for network reconfiguration

Network reconfiguration includes many automatic rollback safety mechanisms that help protect your cluster from failed configuration changes.

Automatic rollback on post-pivot failure
If network configuration or certificate regeneration fails after the reboot, the system automatically triggers a rollback to the earlier stateroot.

Init-monitor timeout rollback
If the network reconfiguration does not complete within the configured timeout, the system automatically triggers a rollback. The default timeout is 1800 seconds, 30 minutes. You can configure this timeout by using the `spec.autoRollbackOnFailure.initMonitorTimeoutSeconds` field in the `IPConfig` CR. Setting the value to `0` uses the default timeout.

# IPConfig reference specifications

The `IPConfig` custom resource (CR) is a cluster-scoped CR that controls the IP configuration workflow for single-node OpenShift clusters using the Lifecycle Agent.

> [!NOTE]
> The CR name must be `ipconfig`.

| Field | Type | Description |
|----|----|----|
| `spec.stage` | String | Controls the current stage of the IP configuration workflow. Valid values are `Idle`, `Config`, and `Rollback`. You can only change the stage to a value listed in `status.validNextStages`. |
| `spec.ipv4.address` | String | The IPv4 node address without CIDR notation, for example `192.0.2.10`. Required if the `ipv4` object is present. Omit the entire `ipv4` object for IPv6-only clusters. |
| `spec.ipv4.machineNetwork` | String | The machine network CIDR, for example `192.0.2.0/24`. The address must be within this CIDR. |
| `spec.ipv4.gateway` | String | The IPv4 default gateway address, used to create the default route for IPv4 traffic. Must be within the machine network CIDR. |
| `spec.ipv6.address` | String | The IPv6 node address without CIDR notation, for example `2001:db8::10`. Required if the `ipv6` object is present. Omit the entire `ipv6` object for IPv4-only clusters. |
| `spec.ipv6.machineNetwork` | String | The IPv6 machine network CIDR, for example `2001:db8::/64`. The address must be within this CIDR. |
| `spec.ipv6.gateway` | String | The IPv6 default gateway, used to create the default route for IPv6 traffic. You can use link-local gateways. |
| `spec.dnsServers` | Array of strings | Ordered list of DNS server IP addresses. The first server in the list is used as the primary DNS server. Must match cluster IP families. Maximum of 2 servers. |
| `spec.vlanID` | Integer | The VLAN ID to configure. Valid values are 1-4094. You can only set this field if the cluster already has VLAN configuration. |
| `spec.dnsFilterOutFamily` | String | DNS response filtering for dual-stack clusters only. Set to `ipv4` to filter out A records, `ipv6` to filter out AAAA records, or `none` to disable filtering. You can only configure this field to `ipv4` or `ipv6` when the cluster uses a dual-stack configuration. |
| `spec.autoRollbackOnFailure.initMonitorTimeoutSeconds` | Integer | Timeout in seconds for the init-monitor watchdog. Set to `0` or leave unset to use the default of 1800 seconds. |

IPConfig spec fields
