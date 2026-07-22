<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Cross-cluster live migration requires that the clusters be connected in the same network. Specifically, `virt-handler` pods must be able to communicate.

> [!IMPORTANT]
> Cross-cluster live migration is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

# Configuration for a bridge secondary network

The Bridge CNI plugin JSON configuration object describes the configuration parameters for the Bridge CNI plugin.

The following table details the configuration parameters:

| Field | Type | Description |
|----|----|----|
| `cniVersion` | `string` | The CNI specification version. A minimum version of `0.3.1` is required. |
| `name` | `string` | The mandatory, unique identifier assigned to this CNI network attachment definition. It is used by the container runtime to select the correct network configuration and serves as the key for persistent resource state management, such as IP address allocations. |
| `type` | `string` | The name of the CNI plugin to configure: `bridge`. |
| `ipam` | `object` | The configuration object for the IPAM CNI plugin. The plugin manages IP address assignment for the attachment definition. |
| `bridge` | `string` | Optional: Specify the name of the virtual bridge to use. If the bridge interface does not exist on the host, the bridge interface gets created. The default value is `cni0`. |
| `ipMasq` | `boolean` | Optional: Set to `true` to enable IP masquerading for traffic that leaves the virtual network. The source IP address for all traffic is rewritten to the bridge’s IP address. If the bridge does not have an IP address, this setting has no effect. The default value is `false`. |
| `disableContainerInterface` | `boolean` | Optional: Controls the container interface (`veth` peer inside the `netns` container). When set to `true`, the container interface link-state is set to `down`, you cannot use the IPAM CNI plugin. The default value is `false`. |
| `isGateway` | `boolean` | Optional: Set to `true` to assign an IP address to the bridge. The default value is `false`. |
| `isDefaultGateway` | `boolean` | Optional: Set to `true` to configure the bridge as the default gateway for the virtual network. The assigned IP address of the bridge is used as the default route. If `isDefaultGateway` is set to `true`, `isGateway` is also set to `true` automatically. The default value is `false`. |
| `forceAddress` | `boolean` | Optional: Set to `true` to allow assignment of a previously assigned IP address to the virtual bridge. When set to `false`, if an IPv4 address or an IPv6 address from overlapping subsets is assigned to the virtual bridge, an error occurs. The default value is `false`. |
| `hairpinMode` | `boolean` | Optional: Set to `true` to allow the virtual bridge to send an Ethernet frame back through the virtual port it was received on. This mode is also known as *reflective relay*. The default value is `false`. |
| `promiscMode` | `boolean` | Optional: Set to `true` to enable promiscuous mode on the bridge. The default value is `false`. |
| `vlan` | `integer` | Optional: Specify a virtual LAN (VLAN) tag as an integer value. By default, no VLAN tag is assigned. |
| `preserveDefaultVlan` | `boolean` | Optional: Indicates whether the default VLAN must be preserved on the `veth` end connected to the bridge. Defaults to `false`. |
| `portIsolation` | `boolean` | Optional: If `true`, prevents containers on the same bridge from communicating with each other. A container can still reach non-isolated ports. For example, a bridge interface that allows access to the host or an optional uplink that allows access outside the host. The default value is `false`. |
| `vlanTrunk` | `list` | Optional: Assign a VLAN trunk tag. The default value is `none`. |
| `mtu` | `integer` | Optional: Set the maximum transmission unit (MTU) to the specified value. The default value is automatically set by the kernel. |
| `enabledad` | `boolean` | Optional: Enables duplicate address detection for the container side `veth`. The default value is `false`. |
| `macspoofchk` | `boolean` | Optional: Enables mac spoof check, limiting the traffic originating from the container to the mac address of the interface. The default value is `false`. |

> [!NOTE]
> The VLAN parameter configures the VLAN tag on the host end of the `veth` and also enables the `vlan_filtering` feature on the bridge interface.

> [!NOTE]
> To configure an uplink for an L2 network, you must allow the VLAN on the uplink interface by using the following command:
>
> ``` terminal
> $  bridge vlan add vid VLAN_ID dev DEV
> ```

## Bridge CNI plugin configuration example

The following example configures a secondary network named `bridge-net`:

``` json
{
  "cniVersion": "0.3.1",
  "name": "bridge-net",
  "type": "bridge",
  "isGateway": true,
  "vlan": 2,
  "ipam": {
    "type": "dhcp"
    }
}
```

# Configuring a dedicated secondary network for live migration

After you have configured a Linux bridge network, you can configure a dedicated network for live migration. A dedicated network minimizes the effects of network saturation on tenant workloads during live migration.

To configure a dedicated secondary network for live migration, you must first create a bridge network attachment definition (NAD) by using the CLI. You can then add the name of the `NetworkAttachmentDefinition` object to the `HyperConverged` custom resource (CR).

<div>

<div class="title">

Prerequisites

</div>

- You installed the OpenShift CLI (`oc`).

- You logged in to the cluster as a user with the `cluster-admin` role.

- Each node has at least two Network Interface Cards (NICs).

- The NICs for live migration are connected to the same VLAN.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `NetworkAttachmentDefinition` manifest according to the following example:

    ``` yaml
    apiVersion: "k8s.cni.cncf.io/v1"
    kind: NetworkAttachmentDefinition
    metadata:
      name: my-secondary-network
      namespace: openshift-cnv
    spec:
      config: '{
        "cniVersion": "0.3.1",
        "name": "migration-bridge",
        "type": "macvlan",
        "master": "eth1",
        "mode": "bridge",
        "ipam": {
          "type": "whereabouts",
          "range": "10.200.5.0/24"
        }
      }'
    ```

    - `metadata.name` defines the name of the `NetworkAttachmentDefinition` object.

    - `config.master` defines the name of the NIC to be used for live migration.

    - `config.type` defines the name of the CNI plugin that provides the network for the NAD.

    - `config.range` defines an IP address range for the secondary network. This range must not overlap the IP addresses of the main network.

2.  Open the `HyperConverged` CR in your default editor by running the following command:

    ``` terminal
    $ oc edit hyperconverged kubevirt-hyperconverged -n openshift-cnv
    ```

3.  Add the name of the `NetworkAttachmentDefinition` object to the `spec.liveMigrationConfig` stanza of the `HyperConverged` CR.

    Example `HyperConverged` manifest:

    ``` yaml
    apiVersion: hco.kubevirt.io/v1beta1
    kind: HyperConverged
    metadata:
      name: kubevirt-hyperconverged
      namespace: openshift-cnv
    spec:
      liveMigrationConfig:
        completionTimeoutPerGiB: 800
        network: <network>
        parallelMigrationsPerCluster: 5
        parallelOutboundMigrationsPerNode: 2
        progressTimeout: 150
    # ...
    ```

    - `spec.liveMigrationConfig.network` defines the name of the Multus `NetworkAttachmentDefinition` object to be used for live migrations.

4.  Save your changes and exit the editor. The `virt-handler` pods restart and connect to the secondary network.

</div>

<div>

<div class="title">

Verification

</div>

- When the node that the virtual machine runs on is placed into maintenance mode, the VM automatically migrates to another node in the cluster. You can verify that the migration occurred over the secondary network and not the default pod network by checking the target IP address in the virtual machine instance (VMI) metadata.

  ``` terminal
  $ oc get vmi <vmi_name> -o jsonpath='{.status.migrationState.targetNodeAddress}'
  ```

</div>
