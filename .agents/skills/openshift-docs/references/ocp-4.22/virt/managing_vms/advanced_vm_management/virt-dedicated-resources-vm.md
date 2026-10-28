<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To improve performance, you can dedicate node resources, such as CPU, to a virtual machine.

# Exclusive CPU use for predictable VM latency

Dedicated resources give a virtual machine (VM) workload exclusive use of its CPUs, which improves VM performance and the accuracy of latency predictions.

When you enable dedicated resources, the VM’s workload is pinned to specific CPUs on the node, and no other process is scheduled on those CPUs. The node must have CPU Manager configured.

# Enable dedicated resources for a virtual machine

Enable dedicated resources for a virtual machine in the OpenShift Container Platform web console so that its workload gets exclusive use of its CPUs.

You can configure dedicated resources for virtual machines that were created from a Red Hat template.

<div>

<div class="title">

Prerequisites

</div>

- The CPU Manager must be configured on the node. Verify that the node has the `cpumanager = true` label before scheduling virtual machine workloads.

- The virtual machine must be powered off.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform console, click **Virtualization** → **VirtualMachines** from the side menu.

2.  Select a virtual machine to open the **VirtualMachine details** page.

3.  On the **Configuration → Scheduling** tab, click the edit icon beside **Dedicated Resources**.

4.  Select **Schedule this workload with dedicated resources (guaranteed policy)**.

5.  Click **Save**.

</div>
