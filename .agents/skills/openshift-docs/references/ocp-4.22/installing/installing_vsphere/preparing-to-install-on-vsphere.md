<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can install an OpenShift Container Platform cluster on vSphere by using a variety of installation methods. Each method is suitable for different use cases, such as disconnected environments or minimal configuration.

# Assisted Installer

You can install OpenShift Container Platform with the Assisted Installer. This method requires no setup for the installation program and is ideal for connected environments such as vSphere. Installing with the Assisted Installer also provides integration with vSphere, enabling autoscaling.

<div>

<div class="title">

Additional resources

</div>

- [Assisted Installer](https://access.redhat.com/documentation/en-us/assisted_installer_for_openshift_container_platform)

- [Installing an on-premise cluster using the Assisted Installer](../installing_on_prem_assisted/installing-on-prem-assisted.md#installing-on-prem-assisted)

</div>

# Agent-based Installer

You can install an OpenShift Container Platform cluster on vSphere using the Agent-based Installer. The Agent-based Installer can be used to boot an on-premise server in a disconnected environment by using a bootable image. With the Agent-based Installer, users also have the flexibility to provision infrastructure, customize network configurations, and customize installations within a disconnected environment.

<div>

<div class="title">

Additional resources

</div>

- [Preparing to install with the Agent-based Installer](../installing_with_agent_based_installer/preparing-to-install-with-agent-based-installer.md#preparing-to-install-with-agent-based-installer)

</div>

# Installer-provisioned infrastructure installation

You can install OpenShift Container Platform on vSphere by using installer-provisioned infrastructure. Installer-provisioned infrastructure allows the installation program to preconfigure and automate the provisioning of resources required by OpenShift Container Platform. Installer-provisioned infrastructure is useful for installing in environments with disconnected networks, where the installation program provisions the underlying infrastructure for the cluster.

- **Installing a cluster on vSphere**: You can install OpenShift Container Platform on vSphere by using installer-provisioned infrastructure installation with no customization.

- **Installing a cluster on vSphere with customizations**: You can install OpenShift Container Platform on vSphere by using installer-provisioned infrastructure installation with the default customization options.

- **Installing a cluster on vSphere in a restricted network**: You can install a cluster on VMware vSphere infrastructure in a restricted network by creating an internal mirror of the installation release content.

  You can use this method to deploy OpenShift Container Platform on an internal network that is not visible to the internet.

<div>

<div class="title">

Additional resources

</div>

- [Installing a cluster on vSphere](ipi/installing-vsphere-installer-provisioned.md#installing-vsphere-installer-provisioned)

- [Installing a cluster on vSphere with customizations](ipi/installing-vsphere-installer-provisioned-customizations.md#installing-vsphere-installer-provisioned-customizations)

- [Installing a cluster on vSphere in a disconnected environment](ipi/installing-restricted-networks-installer-provisioned-vsphere.md#installing-restricted-networks-installer-provisioned-vsphere)

</div>

# User-provisioned infrastructure installation

You can install OpenShift Container Platform on vSphere by using user-provisioned infrastructure. User-provisioned infrastructure requires the user to provision all resources required by OpenShift Container Platform. If you do not use infrastructure that the installation program provisions, you must manage and maintain the cluster resources yourself.

- **Installing a cluster on vSphere with user-provisioned infrastructure**: You can install OpenShift Container Platform on VMware vSphere infrastructure that you provision or you can install OpenShift Container Platform on VMware vSphere infrastructure that you provision with customized network configuration options.

- **Installing a cluster on vSphere in a restricted network with user-provisioned infrastructure**: OpenShift Container Platform can be installed on VMware vSphere infrastructure that you provision in a restricted network.

> [!IMPORTANT]
> The steps for performing a user-provisioned infrastructure installation are provided as an example only. Installing a cluster with infrastructure you provide requires knowledge of the vSphere platform and the installation process of OpenShift Container Platform. Use the user-provisioned infrastructure installation instructions as a guide; you are free to create the required resources through other methods.

<div>

<div class="title">

Additional resources

</div>

- [Installing a cluster on vSphere with user-provisioned infrastructure](upi/installing-vsphere.md#installing-vsphere)

- [Installing a cluster on vSphere in a disconnected environment with user-provisioned infrastructure](upi/installing-restricted-networks-vsphere.md#installing-restricted-networks-vsphere)

- [Installation process](../../architecture/architecture-installation.md#installation-process_architecture-installation)

</div>
