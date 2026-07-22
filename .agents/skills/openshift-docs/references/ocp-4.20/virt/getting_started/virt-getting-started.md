<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Explore OpenShift Virtualization by taking guided tours, installing the Operator, and configuring a basic environment. Learn how to migrate from your current platform, then learn more about how to deploy and manage virtual machines (VMs) by following the additional resources links.

> [!NOTE]
> Cluster configuration procedures require `cluster-admin` privileges.

# Getting started tour

The **Getting started** tour introduces several key aspects of using OpenShift Virtualization. There are two ways to start the tour.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform web console.

</div>

<div>

<div class="title">

Procedure

</div>

- If you see the **Welcome to OpenShift Virtualization** dialog, click **Start Tour**.

- Otherwise, go to **Virtualization** → **Overview** → **Settings** → **User** → **Getting started resources** → **Guided tour**.

</div>

# Quick start tours

You can explore several OpenShift Virtualization capabilities by taking quick start tours in the web console.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift Container Platform web console.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Click the **Help** icon **?** in the menu bar on the header of the OpenShift Container Platform web console.

2.  Select **Quick Starts**. You can filter the list of tours by entering the keyword `virtual` in the **Filter** field.

</div>

# Additional resources

- [Plan your bare-metal cluster for OpenShift Virtualization](../../installing/installing_bare_metal/preparing-to-install-on-bare-metal.md#virt-planning-bare-metal-cluster-for-ocp-virt_preparing-to-install-on-bare-metal)

- [Prepare your cluster for OpenShift Virtualization](../install/preparing-cluster-for-virt.md#preparing-cluster-for-virt)

- [Learn about storage volumes for VM disks](../install/preparing-cluster-for-virt.md#virt-about-storage-volumes-for-vm-disks_virt-requirements)

- [Use a CSI-enabled storage provider](../../storage/container_storage_interface/persistent-storage-csi.md#persistent-storage-csi)

- [Configure local storage for virtual machines](../storage/virt-configuring-local-storage-with-hpp.md#virt-configuring-local-storage-with-hpp)

- [Install the OpenShift Virtualization Operator](../install/installing-virt.md#virt-installing-virt-operator_installing-virt)

- [Install the Kubernetes NMState Operator](../../networking/networking_operators/k8s-nmstate-about-the-k8s-nmstate-operator.md#installing-the-kubernetes-nmstate-operator-cli)

- [Specify nodes for virtual machines](../managing_vms/advanced_vm_management/virt-specifying-nodes-for-vms.md#virt-specifying-nodes-for-vms)

- [Install and use the `virtctl` command-line interface (CLI) tool](virt-using-the-cli-tools.md#virt-using-the-cli-tools)

- [Create a VM from a Red Hat image](../creating_vms_advanced/virt-creating-vms-from-rh-images-overview.md#virt-creating-vms-from-rh-images-overview)

- [Create a VM from an instance type](../creating_vm/virt-creating-vms-from-instance-types.md#virt-creating-vms-from-instance-types)

- [Import a custom image from a web page](../creating_vms_advanced/virt-creating-vms-from-web-images.md#virt-creating-vms-from-web-images)

- [Upload an image from your local machine](../creating_vms_advanced/virt-creating-vms-uploading-images.md#virt-creating-vms-uploading-images)

- [Clone a persistent volume claim (PVC)](../creating_vms_advanced/virt-creating-vms-by-cloning-pvcs.md#virt-creating-vms-by-cloning-pvcs)

- [Connect a VM to a Linux bridge network](../vm_networking/virt-connecting-vm-to-linux-bridge.md#virt-connecting-vm-to-linux-bridge)

- [Connect a VM to an Open Virtual Network (OVN)-Kubernetes secondary network](../vm_networking/virt-connecting-vm-to-ovn-secondary-network.md#virt-connecting-vm-to-ovn-secondary-network)

- [Connect a VM to a Single Root I/O Virtualization (SR-IOV) network](../vm_networking/virt-connecting-vm-to-sriov.md#virt-connecting-vm-to-sriov)

- [Connect to a virtual machine console](../managing_vms/virt-accessing-vm-consoles.md#virt-accessing-vm-consoles)

- [SSH access for virtual machines](../managing_vms/ssh/virt-accessing-vm-ssh.md#virt-accessing-vm-ssh)

- [Connect to the desktop viewer by using the web console](../managing_vms/virt-accessing-vm-consoles.md#virt-connecting-desktop-viewer-web_virt-accessing-vm-consoles)

- [Manage a VM by using the web console](../managing_vms/virt-controlling-vm-states.md#virt-controlling-vm-states)

- [Export a VM](../managing_vms/virt-exporting-vms.md#virt-accessing-exported-vm-manifests_virt-exporting-vms)

- [Review post-installation configuration options](../post_installation_configuration/virt-post-install-config.md#virt-post-install-config)

- [Configure storage options and automatic boot source updates](../storage/virt-storage-config-overview.md#virt-storage-config-overview)

- [Learn about monitoring and health checks](../monitoring/virt-monitoring-overview.md#virt-monitoring-overview)

- [Learn about live migration](../live_migration/virt-about-live-migration.md#virt-about-live-migration)

- [Back up and restore VMs by using the OpenShift API for Data Protection (OADP)](../../backup_and_restore/application_backup_and_restore/installing/installing-oadp-kubevirt.md#installing-oadp-kubevirt)

- [Tune and scale your cluster](https://access.redhat.com/articles/6994974)
