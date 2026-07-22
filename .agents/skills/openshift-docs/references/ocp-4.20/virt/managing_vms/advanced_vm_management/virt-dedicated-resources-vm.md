<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To improve performance, you can dedicate node resources, such as CPU, to a virtual machine.

# About dedicated resources

When you enable dedicated resources for your virtual machine, your virtual machine’s workload is scheduled on CPUs that will not be used by other processes.

By using dedicated resources, you can improve the performance of the virtual machine and the accuracy of latency predictions.

# Enabling dedicated resources for a virtual machine

You can enable dedicated resources for a virtual machine in the **Details** tab. Virtual machines that were created from a Red Hat template can be configured with dedicated resources.

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
