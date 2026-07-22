<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can encrypt your virtual machines after installing OpenShift Container Platform 4.17 on vSphere by draining and shutting down your nodes one at a time. While each virtual machine is shutdown, you can enable encryption in the vCenter web interface.

# Encrypting virtual machines

You can encrypt your virtual machines with the following process. You can drain your virtual machines, power them down and encrypt them using the vCenter interface. Finally, you can create a storage class to use the encrypted storage.

<div>

<div class="title">

Prerequisites

</div>

- You have configured a Standard key provider in vSphere. For more information, see [Adding a KMS to vCenter Server](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vsan.doc/GUID-AC06B3C3-901F-402E-B25F-1EE7809D1264.html).

  > [!IMPORTANT]
  > The Native key provider in vCenter is not supported. For more information, see [vSphere Native Key Provider Overview](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-54B9FBA2-FDB1-400B-A6AE-81BF3AC9DF97.html).

- You have enabled host encryption mode on all of the ESXi hosts that are hosting the cluster. For more information, see [Enabling host encryption mode](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-A9E1F016-51B3-472F-B8DE-803F6BDB70BC.html).

- You have a vSphere account which has all cryptographic privileges enabled. For more information, see [Cryptographic Operations Privileges](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-660CCB35-847F-46B3-81CA-10DDDB9D7AA9.html).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Drain and cordon one of your nodes. For detailed instructions on node management, see "Working with Nodes".

2.  Shutdown the virtual machine associated with that node in the vCenter interface.

3.  Right-click the virtual machine in the vCenter interface and select **VM Policies** → **Edit VM Storage Policies**.

4.  Select an encrypted storage policy and select **OK**.

5.  Start the encrypted virtual machine in the vCenter interface.

6.  Repeat steps 1-5 for all nodes that you want to encrypt.

7.  Configure a storage class that uses the encrypted storage policy. For more information about configuring an encrypted storage class, see "VMware vSphere CSI Driver Operator".

</div>

# Additional resources

- [Evacuating pods on nodes](../../nodes/nodes/nodes-nodes-working.md#nodes-nodes-working-evacuating_nodes-nodes-working)

- [vSphere persistent disks encryption](../../storage/container_storage_interface/persistent-storage-csi-vsphere.md#vsphere-pv-encryption)

- [Requirements for encrypting virtual machines](upi/upi-vsphere-installation-reqs.md#installation-vsphere-encrypted-vms_upi-vsphere-installation-reqs)
