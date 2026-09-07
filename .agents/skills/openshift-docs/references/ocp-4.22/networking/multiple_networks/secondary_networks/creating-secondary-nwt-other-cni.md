<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The specific configuration fields for secondary networks are described in the following sections.

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

# Configuration for a Bond CNI secondary network

The Bond Container Network Interface (Bond CNI) enables the aggregation of multiple network interfaces into a single logical bonded interface within a container, which enhanches network redundancy and fault tolerance. Only SR-IOV Virtual Functions (VFs) are supported for bonding with this plugin.

The following table describes the configuration parameters for the Bond CNI plugin:

| Field | Type | Description |
|----|----|----|
| `name` | `string` | The mandatory, unique identifier assigned to this CNI network attachment definition. It is used by the container runtime to select the correct network configuration and serves as the key for persistent resource state management, such as IP address allocations. |
| `cniVersion` | `string` | The CNI specification version. A minimum version of `0.3.1` is required. |
| `type` | `string` | Specifies the name of the CNI plugin to configure: `bond`. |
| `miimon` | `string` | Specifies the address resolution protocol (ARP) link monitoring frequency in milliseconds. This parameter defines how often the bond interface sends ARP requests to check the availability of its aggregated interfaces. |
| `mtu` | `integer` | Optional: Specifies the maximum transmission unit (MTU) of the bond. The default is `1500`. |
| `failOverMac` | `integer` | Optional: Specifies the `failOverMac` setting for the bond. Default is `0`. |
| `mode` | `string` | Specifies the bonding policy. |
| `xmitHashPolicy` | `string` | Specifies the transmit hash policy for load balancing across the aggregated interfaces. This parameter defaults to `layer2` and supports the following values: `layer2`, `layer2+3` and `layer3+4`. |
| `linksInContainer` | `boolean` | Optional: Specifies whether the network interfaces intended for bonding are expected to be created and available directly within the network namespace of the container when the bond starts. If `false` which is the default, the CNI plugin looks for these interfaces on the host system first before attempting to form the bond. |
| `links` | `object` | Specifies the interfaces to be bonded. |
| `ipam` | `object` | The configuration object for the IPAM CNI plugin. The plugin manages IP address assignment for the attachment definition. |

Bond CNI plugin JSON configuration object

> [!IMPORTANT]
> xmitHashPolicy is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

## Bond CNI plugin configuration example

The following example configures a secondary network named `bond-net1`:

``` json
{
 "type": "bond",
 "cniVersion": "0.3.1",
 "name": "bond-net1",
 "mode": "active-backup",
 "failOverMac": 1,
 "linksInContainer": true,
 "miimon": "100",
 "mtu": 1500,
 "links": [
       {"name": "net1"},
       {"name": "net2"}
   ],
  "ipam": {
        "type": "host-local",
        "subnet": "10.56.217.0/24",
        "routes": [{
        "dst": "0.0.0.0/0"
        }],
        "gateway": "10.56.217.1"
    }
}
```

The following example configures a secondary network named `bond-tlb-net` with the `xmitHashPolicy` feature enabled:

``` json
{
 "type": "bond",
 "cniVersion": "0.3.1",
 "name": "bond-tlb-net",
 "mode": "tlb",
 "xmitHashPolicy": "layer2+3",
 "failOverMac": 0,
 "linksInContainer": true,
 "miimon": "100",
 "mtu": 1500,
 "links": [
       {"name": "net1"},
       {"name": "net2"}
   ],
  "ipam": {
        "type": "host-local",
        "subnet": "10.57.218.0/24",
        "routes": [{
        "dst": "0.0.0.0/0"
        }],
        "gateway": "10.57.218.1"
    }
}
```

- `xmitHashPolicy`: This parameter dictates how outgoing network traffic is distributed across the `net1` and `net2` active member interfaces within the bond. The hashing algorithm combines layer 2 information, specifically source and destination MAC addresses, with layer 3 information, which includes source and destination IP addresses.

<div>

<div class="title">

Additional resources

</div>

- [Configuring a bond interface from two SR-IOV interfaces](../../hardware_networks/using-pod-level-bonding.md#nw-sriov-cfg-bond-interface-with-virtual-functions_using-pod-level-bonding)

</div>

# Configuration for a host device secondary network

The host device CNI plugin JSON configuration object describes the configuration parameters for the host-device CNI plugin.

> [!NOTE]
> Specify your network device by setting only one of the following parameters: `device`,`hwaddr`, `kernelpath`, or `pciBusID`.

The following table details the configuration parameters:

| Field | Type | Description |
|----|----|----|
| `cniVersion` | `string` | The CNI specification version. A minimum version of `0.3.1` is required. |
| `name` | `string` | The mandatory, unique identifier assigned to this CNI network attachment definition. It is used by the container runtime to select the correct network configuration and serves as the key for persistent resource state management, such as IP address allocations. |
| `type` | `string` | The name of the CNI plugin to configure: `host-device`. |
| `device` | `string` | Optional: The name of the device, such as `eth0`. |
| `hwaddr` | `string` | Optional: The device hardware MAC address. |
| `kernelpath` | `string` | Optional: The Linux kernel device path, such as `/sys/devices/pci0000:00/0000:00:1f.6`. |
| `pciBusID` | `string` | Optional: The PCI address of the network device, such as `0000:00:1f.6`. |

## host-device configuration example

The following example configures a secondary network named `hostdev-net`:

``` json
{
  "cniVersion": "0.3.1",
  "name": "hostdev-net",
  "type": "host-device",
  "device": "eth1"
}
```

# Configuration for a dummy device additional network

The dummy CNI plugin functions like a loopback device. The plugin is a virtual interface, and you can use the plugin to route the packets to a designated IP address. Unlike a loopback device, the IP address is arbitrary and is not restricted to the `127.0.0.0/8` address range.

The dummy device CNI plugin JSON configuration object describes the configuration parameters for the dummy CNI plugin. The following table details these parameters:

| Field | Type | Description |
|----|----|----|
| `cniVersion` | `string` | The CNI specification version. A minimum version of `0.3.1` is required. |
| `name` | `string` | The mandatory, unique identifier assigned to this CNI network attachment definition. It is used by the container runtime to select the correct network configuration and serves as the key for persistent resource state management, such as IP address allocations. |
| `type` | `string` | The name of the CNI plugin that you want to configure. The required value is `dummy`. |
| `ipam` | `object` | The configuration object for the IPAM CNI plugin. The plugin manages the IP address assignment for the attachment definition. |

## dummy configuration example

The following example configures an additional network named `hostdev-net`:

``` json
{
  "cniVersion": "0.3.1",
  "name": "dummy-net",
  "type": "dummy",
  "ipam": {
      "type": "host-local",
      "subnet": "10.1.1.0/24"
  }
}
```

# Configuration for a VLAN secondary network

The VLAN CNI plugin JSON configuration object describes the configuration parameters for the VLAN, `vlan`, CNI plugin. The following table details these parameters:

| Field | Type | Description |
|----|----|----|
| `cniVersion` | `string` | The CNI specification version. A minimum version of `0.3.1` is required. |
| `name` | `string` | The mandatory, unique identifier assigned to this CNI network attachment definition. It is used by the container runtime to select the correct network configuration and serves as the key for persistent resource state management, such as IP address allocations. |
| `type` | `string` | The name of the CNI plugin to configure: `vlan`. |
| `master` | `string` | The Ethernet interface to associate with the network attachment. If a `master` is not specified, the interface for the default network route is used. |
| `vlanId` | `integer` | Set the ID of the `vlan`. |
| `ipam` | `object` | The configuration object for the IPAM CNI plugin. The plugin manages IP address assignment for the attachment definition. |
| `mtu` | `integer` | Optional: Set the maximum transmission unit (MTU) to the specified value. The default value is automatically set by the kernel. |
| `dns` | `integer` | Optional: DNS information to return. For example, a priority-ordered list of DNS nameservers. |
| `linkInContainer` | `boolean` | Optional: Specifies whether the `master` interface is in the container network namespace or the main network namespace. Set the value to `true` to request the use of a container namespace `master` interface. |

> [!IMPORTANT]
> A `NetworkAttachmentDefinition` custom resource definition (CRD) with a `vlan` configuration can be used only on a single pod in a node because the CNI plugin cannot create multiple `vlan` subinterfaces with the same `vlanId` on the same `master` interface.

## VLAN configuration example

The following example demonstrates a `vlan` configuration with a secondary network that is named `vlan-net`:

``` json
{
  "name": "vlan-net",
  "cniVersion": "0.3.1",
  "type": "vlan",
  "master": "eth0",
  "mtu": 1500,
  "vlanId": 5,
  "linkInContainer": false,
  "ipam": {
      "type": "host-local",
      "subnet": "10.1.1.0/24"
  },
  "dns": {
      "nameservers": [ "10.1.1.1", "8.8.8.8" ]
  }
}
```

- `ipam.type.host-local`: Allocates IPv4 and IPv6 IP addresses from a specified set of address ranges. IPAM plugin stores the IP addresses locally on the host filesystem so that the addresses remain unique to the host.

# Configuration for an IPVLAN secondary network

The IPVLAN CNI plugin JSON configuration object describes the configuration parameters for the IPVLAN, `ipvlan`, CNI plugin. The following table details these parameters:

| Field | Type | Description |
|----|----|----|
| `cniVersion` | `string` | The CNI specification version. A minimum version of `0.3.1` is required. |
| `name` | `string` | The mandatory, unique identifier assigned to this CNI network attachment definition. It is used by the container runtime to select the correct network configuration and serves as the key for persistent resource state management, such as IP address allocations. |
| `type` | `string` | The name of the CNI plugin to configure: `ipvlan`. |
| `ipam` | `object` | The configuration object for the IPAM CNI plugin. The plugin manages IP address assignment for the attachment definition. This is required unless the plugin is chained. |
| `mode` | `string` | Optional: The operating mode for the virtual network. The value must be `l2`, `l3`, or `l3s`. The default value is `l2`. |
| `master` | `string` | Optional: The Ethernet interface to associate with the network attachment. If a `master` is not specified, the interface for the default network route is used. |
| `mtu` | `integer` | Optional: Set the maximum transmission unit (MTU) to the specified value. The default value is automatically set by the kernel. |
| `linkInContainer` | `boolean` | Optional: Specifies whether the `master` interface is in the container network namespace or the main network namespace. Set the value to `true` to request the use of a container namespace `master` interface. |

<div class="important">

<div class="title">

</div>

- The `ipvlan` object does not allow virtual interfaces to communicate with the `master` interface. Therefore the container is not able to reach the host by using the `ipvlan` interface. Be sure that the container joins a network that provides connectivity to the host, such as a network supporting the Precision Time Protocol (`PTP`).

- A single `master` interface cannot simultaneously be configured to use both `macvlan` and `ipvlan`.

- For IP allocation schemes that cannot be interface agnostic, the `ipvlan` plugin can be chained with an earlier plugin that handles this logic. If the `master` is omitted, then the previous result must contain a single interface name for the `ipvlan` plugin to enslave. If `ipam` is omitted, then the previous result is used to configure the `ipvlan` interface.

</div>

## IPVLAN CNI plugin configuration example

The following example configures a secondary network named `ipvlan-net`:

``` json
{
  "cniVersion": "0.3.1",
  "name": "ipvlan-net",
  "type": "ipvlan",
  "master": "eth1",
  "linkInContainer": false,
  "mode": "l3",
  "ipam": {
    "type": "static",
    "addresses": [
       {
         "address": "192.168.10.10/24"
       }
    ]
  }
}
```

# Configuration for a MACVLAN secondary network

The MACVLAN CNI plugin JSON configuration object describes the configuration parameters for the MAC Virtual LAN (MACVLAN) Container Network Interface (CNI) plugin. The following table describes these parameters:

| Field | Type | Description |
|----|----|----|
| `cniVersion` | `string` | The CNI specification version. A minimum version of `0.3.1` is required. |
| `name` | `string` | The mandatory, unique identifier assigned to this CNI network attachment definition. It is used by the container runtime to select the correct network configuration and serves as the key for persistent resource state management, such as IP address allocations. |
| `type` | `string` | The name of the CNI plugin to configure: `macvlan`. |
| `ipam` | `object` | The configuration object for the IPAM CNI plugin. The plugin manages IP address assignment for the attachment definition. |
| `mode` | `string` | Optional: Configures traffic visibility on the virtual network. Must be either `bridge`, `passthru`, `private`, or `vepa`. If a value is not provided, the default value is `bridge`. |
| `master` | `string` | Optional: The host network interface to associate with the newly created macvlan interface. If a value is not specified, then the default route interface is used. |
| `mtu` | `integer` | Optional: The maximum transmission unit (MTU) to the specified value. The default value is automatically set by the kernel. |
| `linkInContainer` | `boolean` | Optional: Specifies whether the `master` interface is in the container network namespace or the main network namespace. Set the value to `true` to request the use of a container namespace `master` interface. |

> [!NOTE]
> If you specify the `master` key for the plugin configuration, use a different physical network interface than the one that is associated with your primary network plugin to avoid possible conflicts.

## MACVLAN CNI plugin configuration example

The following example configures a secondary network named `macvlan-net`:

``` json
{
  "cniVersion": "0.3.1",
  "name": "macvlan-net",
  "type": "macvlan",
  "master": "eth1",
  "linkInContainer": false,
  "mode": "bridge",
  "ipam": {
    "type": "dhcp"
    }
}
```

# Configuration for a TAP secondary network

The TAP CNI plugin JSON configuration object describes the configuration parameters for the TAP CNI plugin.

The following table describes these configuration parameters:

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Field</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>cniVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The CNI specification version. A minimum version of <code>0.3.1</code> is required.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The mandatory, unique identifier assigned to this CNI network attachment definition. It is used by the container runtime to select the correct network configuration and serves as the key for persistent resource state management, such as IP address allocations.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>The name of the CNI plugin to configure: <code>tap</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mac</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: Request the specified MAC address for the interface.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mtu</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Optional: Set the maximum transmission unit (MTU) to the specified value. The default value is automatically set by the kernel.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selinuxcontext</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: The SELinux context to associate with the tap device.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>The value <code>system_u:system_r:container_t:s0</code> is required for OpenShift Container Platform.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>multiQueue</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>Optional: Set to <code>true</code> to enable multi-queue.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>owner</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Optional: The user owning the tap device.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>group</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Optional: The group owning the tap device.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>bridge</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Optional: Set the tap device as a port of an already existing bridge.</p></td>
</tr>
</tbody>
</table>

## Tap configuration example

The following example configures a secondary network named `mynet`:

``` json
{
 "name": "mynet",
 "cniVersion": "0.3.1",
 "type": "tap",
 "mac": "00:11:22:33:44:55",
 "mtu": 1500,
 "selinuxcontext": "system_u:system_r:container_t:s0",
 "multiQueue": true,
 "owner": 0,
 "group": 0
 "bridge": "br1"
}
```

# Setting SELinux boolean for the TAP CNI plugin

To create the tap device with the `container_t` SELinux context, enable the `container_use_devices` boolean on the host by using the Machine Config Operator (MCO).

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a new YAML file with the following details:

    <div class="formalpara">

    <div class="title">

    Example `setsebool-container-use-devices.yaml`

    </div>

    ``` yaml
    apiVersion: machineconfiguration.openshift.io/v1
    kind: MachineConfig
    metadata:
      labels:
        machineconfiguration.openshift.io/role: worker
      name: 99-worker-setsebool
    spec:
      config:
        ignition:
          version: 3.2.0
        systemd:
          units:
          - enabled: true
            name: setsebool.service
            contents: |
              [Unit]
              Description=Set SELinux boolean for the TAP CNI plugin
              Before=kubelet.service

              [Service]
              Type=oneshot
              ExecStart=/usr/sbin/setsebool container_use_devices=on
              RemainAfterExit=true

              [Install]
              WantedBy=multi-user.target graphical.target
    ```

    </div>

2.  Create the new `MachineConfig` object by running the following command:

    ``` terminal
    $ oc apply -f setsebool-container-use-devices.yaml
    ```

    > [!NOTE]
    > Applying any changes to the `MachineConfig` object causes all affected nodes to gracefully reboot after the change is applied. The MCO might take some time to apply the update.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the change is applied by running the following command:

  ``` terminal
  $ oc get machineconfigpools
  ```

  ``` terminal
  NAME        CONFIG                                                UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
  master      rendered-master-e5e0c8e8be9194e7c5a882e047379cfa      True      False      False      3              3                   3                     0                      7d2h
  worker      rendered-worker-d6c9ca107fba6cd76cdcbfcedcafa0f2      True      False      False      3              3                   3                     0                      7d
  ```

  > [!NOTE]
  > All nodes should be in the `Updated` and `Ready` state.

</div>

# Configuring routes using the route-override plugin on a secondary network

The Route override CNI plugin JSON configuration object describes the configuration parameters for the `route-override` CNI plugin. The following table details these parameters:

| Field | Type | Description |
|----|----|----|
| `type` | `string` | The name of the CNI plugin to configure: `route-override`. |
| `flushroutes` | `boolean` | Optional: Set to `true` to flush any existing routes. |
| `flushgateway` | `boolean` | Optional: Set to `true` to flush the default route namely the gateway route. |
| `delroutes` | `object` | Optional: Specify the list of routes to delete from the container namespace. |
| `addroutes` | `object` | Optional: Specify the list of routes to add to the container namespace. Each route is a dictionary with `dst` and optional `gw` fields. If `gw` is omitted, the plugin uses the default gateway value. |
| `skipcheck` | `boolean` | Optional: Set this to `true` to skip the check command. By default, CNI plugins verify the network setup during the container lifecycle. When modifying routes dynamically with `route-override`, skipping this check ensures the final configuration reflects the updated routes. |

## Route-override plugin configuration example

The `route-override` CNI is a type of CNI that is designed to be used when chained with a parent CNI. The CNI type does not operate independently, but relies on the parent CNI to first create the network interface and assign IP addresses before the CNI type can modify the routing rules.

The following example configures a secondary network named `mymacvlan`. The parent CNI creates a network interface attached to `eth1` and assigns an IP address in the `192.168.1.0/24` range by using `host-local` IPAM. The `route-override` CNI is then chained to the parent CNI and modifies the routing rules by flushing existing routes, deleting the route to `192.168.0.0/24`, and adding a new route for `192.168.0.0/24` with a custom gateway.

``` json
{
    "cniVersion": "0.3.0",
    "name": "mymacvlan",
    "plugins": [
        {
            "type": "macvlan",
            "master": "eth1",
            "mode": "bridge",
            "ipam": {
                "type": "host-local",
                "subnet": "192.168.1.0/24"
            }
        },
        {
            "type": "route-override",
            "flushroutes": true,
            "delroutes": [
                {
                    "dst": "192.168.0.0/24"
                }
            ],
            "addroutes": [
                {
                    "dst": "192.168.0.0/24",
                    "gw": "10.1.254.254"
                }
            ]
        }
    ]
}
```

where:

`"type": "macvlan"`
The parent CNI creates a network interface attached to `eth1`.

`"type": "route-override"`
The chained `route-override` CNI modifies the routing rules.

<div>

<div class="title">

Additional resources

</div>

- [Setting SELinux booleans](../../../nodes/nodes/nodes-nodes-managing.md#nodes-nodes-working-setting-booleans_nodes-nodes-managing)

</div>
