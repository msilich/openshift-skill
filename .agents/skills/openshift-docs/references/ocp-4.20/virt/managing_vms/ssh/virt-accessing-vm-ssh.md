<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use SSH to securely access your virtual machines (VMs) from the command line. You can set up your SSH configuration using the `virtctl ssh` command, `virtctl port-forward` command, a service, or a secondary network.

# Options for connecting to VMs

Your goal determines the best way to connect to a virtual machine (VM), whether troubleshooting, automating configuration with Ansible, or providing access to clients outside the cluster.

> [!NOTE]
> Services provide excellent performance and are recommended for applications that are accessed from outside the cluster.

If the internal cluster network cannot handle the traffic load, you can configure a secondary network.

`virtctl ssh` and `virtctl port-forwarding` commands
- Simple to configure.

- Recommended for troubleshooting VMs.

- `virtctl port-forwarding` recommended for automated configuration of VMs with Ansible.

- Dynamic public SSH keys can be used to provision VMs with Ansible.

- Not recommended for high-traffic applications such as Rsync or Remote Desktop Protocol because of the burden on the API server.

- The API server must be able to handle the traffic load.

- The clients must be able to access the API server.

- The clients must have access credentials for the cluster.

Cluster IP service
- The internal cluster network must be able to handle the traffic load.

- The clients must be able to access an internal cluster IP address.

Node port service
- The internal cluster network must be able to handle the traffic load.

- The clients must be able to access at least one node.

Load balancer service
- A load balancer must be configured.

- Each node must be able to handle the traffic load of one or more load balancer services.

Secondary network
- Excellent performance because traffic does not go through the internal cluster network.

- Allows a flexible approach to network topology.

- Guest operating system must be configured with appropriate security because the VM is exposed directly to the secondary network. If a VM is compromised, an intruder could gain access to the secondary network.

# Additional resources

- [OpenShift Virtualization Tuning & Scaling Guide](https://access.redhat.com/articles/6994974)

- [Connecting a virtual machine to a Linux bridge network](../../vm_networking/virt-connecting-vm-to-linux-bridge.md#virt-connecting-vm-to-linux-bridge)

- [Connecting a virtual machine to an SR-IOV network](../../vm_networking/virt-connecting-vm-to-sriov.md#virt-connecting-vm-to-sriov)

- [Create a Linux bridge NAD by using the web console](../../vm_networking/virt-connecting-vm-to-linux-bridge.md#virt-creating-linux-bridge-nad-web_virt-connecting-vm-to-linux-bridge)

- [Configure an SR-IOV additional network](../../vm_networking/virt-connecting-vm-to-sriov.md#nw-sriov-additional-network_virt-connecting-vm-to-sriov)

- [Accessing a virtual machine by using its external FQDN](../../vm_networking/virt-accessing-vm-secondary-network-fqdn.md#virt-accessing-vm-secondary-network-fqdn)
