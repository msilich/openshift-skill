<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As an OpenShift Container Platform administrator, you can create or configure a physical network in the OpenShift Container Platform web console without using the node network configuration policy (NNCP) page.

> [!NOTE]
> The **Physical networks** page is available when the NMState console plugin is installed. When you use the **Physical networks** page in the web console, the NNCP is generated automatically. If you need more flexibility or require complex settings, use the NNCP page.

# Creating a physical network by using the OpenShift Container Platform web console

You can create physical networks for OpenShift Virtualization using the OpenShift Container Platform web console to create a network with direct layer 2 connectivity to your data center.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, go to **Networking** → **Physical networks**.

2.  Click **Create network**. The **Network configuration wizard** is displayed.

3.  On the **Network identity** page, enter a name for your network.

4.  On the **Nodes configuration** page, select either **Apply to all nodes on the cluster** or **Apply to specific subsets of nodes using the nodes selector**.

    > [!NOTE]
    > If you select specific nodes to apply the network to, you can view the matching nodes list to ensure the selection is correct. A validation error is displayed if the selected nodes overlap with another configuration associated with the same network.

5.  On the **Uplink connection** page, select the network interface that you want to connect to the physical network:

    Default node network
    Uses the default node network to access the outside physical network.

    A single interface
    Select a specific physical network interface from the list.

    > [!WARNING]
    > If the selected secondary interface has an IP address on some of the nodes, using it removes the IP address and might disrupt network services.

    Bonding interface
    Configures bonded network interfaces to achieve resilience and higher throughput.

    1.  Enter a **Bonding name**.

    2.  Select the **Network interfaces** to bond.

    3.  Select the **Aggregation mode** from the drop-down menu.

6.  On the **Settings** page, enter a **Bridge name** and set the **Maximum Transmission Unit (MTU)**.

7.  Review the configuration details.

8.  Click **Create**.

</div>

<div>

<div class="title">

Verification

</div>

1.  In the OpenShift Container Platform web console, go to **Networking** → **Physical networks**.

2.  Locate your new network in the list.

3.  Expand the network row to view the associated configurations. Verify that the **Enactment state** is **Available** and that the **Nodes** count matches your expectation.

</div>

# Expanding a OpenShift Container Platform physical network to include new nodes

You can add one or more OpenShift Container Platform worker nodes to an existing physical network if you want to expand access to that network. Expanding a physical network creates a new configuration under the same logical physical network.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, go to **Networking** → **Physical networks**.

2.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to the network that you want to edit.

3.  Click **Configure nodes**. The **Network configuration wizard** is displayed.

    > [!NOTE]
    > The **Physical network name** is predefined. You cannot edit it during this process.

4.  Click **Next**.

5.  On the **Nodes configuration** page, select either **Apply to all nodes on the cluster** or **Apply to specific subsets of nodes using the nodes selector**.

    > [!NOTE]
    > If you select specific nodes, you can view the matching nodes list to ensure the selection is correct. A validation error is displayed if the selected nodes overlap with another configuration associated with the same network.

6.  On the **Uplink connection** page, select the network interface to connect to the physical network:

    Default node network
    Uses the default node network to access the outside physical network.

    A single interface
    Select a specific physical network interface from the list.

    > [!WARNING]
    > If the selected secondary interface has an IP address on some of the nodes, using removes the IP address and might disrupt network services.

    Bonding interface
    Configures bonded network interfaces to achieve resilience and higher throughput.

    1.  Enter a **Bonding name**.

    2.  Select the **Network interfaces** to bond.

        > [!NOTE]
        > The system displays only the interfaces that all nodes have in common.

    3.  Select the **Aggregation mode** from the drop down options.

7.  On the **Settings** page, enter a **Bridge name** and set the **Maximum Transmission Unit (MTU)**.

8.  Review the configuration details.

9.  Click **Create**.

</div>

# Creating a virtual machine network from a physical network

If your use case does not permit the use of network address translation (NAT), you can give VMs direct layer 2 access by creating a VM network that uses a physical network.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, go to **Networking** → **Physical networks**.

2.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) next to the network that you want to edit.

3.  Click **Create a virtual machines network using this physical network**. The **Create virtual machine network** wizard is displayed with the network name populated.

4.  Select a **Physical network**.

5.  Optional: Select **VLAN tagging** and enter a **VLAN ID**.

6.  On the **Project mapping** page, define which projects can access this network.

7.  Click **Create**.

</div>
