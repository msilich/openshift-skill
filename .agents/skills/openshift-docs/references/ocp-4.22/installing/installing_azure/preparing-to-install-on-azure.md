<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

When you plan an OpenShift Container Platform deployment on Microsoft Azure, you can select installer-provisioned or user-provisioned infrastructure. Compare installation methods to find the path that matches your network, security, and operational requirements.

The default installation type uses installer-provisioned infrastructure, where the installation program provisions the underlying infrastructure for the cluster.

You can also install OpenShift Container Platform on infrastructure that you provision. If you do not use infrastructure that the installation program provisions, you must manage and support the cluster resources yourself.

# Installing a cluster on installer-provisioned infrastructure

You can install a cluster on Microsoft Azure infrastructure that is provisioned by the OpenShift Container Platform installation program, by using one of the following methods:

- You can install OpenShift Container Platform on Azure infrastructure that the installation program provisions and use default configuration options for a quick deployment. For more information, see "Installing a cluster quickly on Azure".

- You can install a customized cluster on Azure infrastructure that the installation program provisions. The installation program supports some customization during installation, and many other options are available postinstallation. For more information, see "Installing a customized cluster on Azure".

- You can customize your OpenShift Container Platform configuration during installation so that your cluster coexists with existing IP address allocations and meets customized network requirements. For more information, see "Installing a cluster on Azure with customizations".

- You can install a cluster on Azure in a restricted network by creating an internal mirror of the installation release content on an existing Azure Virtual Network (`VNet`). For more information, see "Installing a cluster on Azure in a restricted network".

- You can install OpenShift Container Platform on an existing Azure `VNet` when company guidelines limit new accounts or infrastructure. For more information, see "Installing a cluster on Azure into an existing \`VNet\`".

- You can install a private cluster into an existing Azure `VNet` on Azure and deploy OpenShift Container Platform on an internal network that is not visible to the internet. For more information, see "Installing a private cluster on Azure".

- You can deploy OpenShift Container Platform into Microsoft Azure Government (MAG) regions for US government agencies, contractors, educational institutions, and other US customers that must run sensitive workloads on Azure. For more information, see "Installing a cluster on Azure into a government region".

<div>

<div class="title">

Additional resources

</div>

- [Installing a cluster quickly on Azure](ipi/installing-azure-default.md#installing-azure-default)

- [Installing a cluster on Azure with customizations](ipi/installing-azure-customizations.md#installing-azure-customizations)

- [Installing a cluster on Azure in a restricted network](ipi/installing-restricted-networks-azure-installer-provisioned.md#installing-restricted-networks-azure-installer-provisioned)

- [Installing a cluster on Azure into an existing `VNet`](ipi/installing-azure-vnet.md#installing-azure-vnet)

- [Installing a private cluster on Azure](ipi/installing-azure-private.md#installing-azure-private)

- [Installing a cluster on Azure into a government region](ipi/installing-azure-government-region.md#installing-azure-government-region)

</div>

# Installing a cluster on user-provisioned infrastructure

You can install a cluster on Azure infrastructure that you provision, by using one of the following methods:

- You can install a cluster on Azure in a restricted network with user-provisioned infrastructure when you do not require an active internet connection to obtain software components. For more information, see "Installing a cluster on Azure in a restricted network with user-provisioned infrastructure".

- You can install OpenShift Container Platform on Azure by using infrastructure that you manage and Azure Resource Manager (ARM) templates to assist with the installation. For more information, see "Installing a cluster on Azure using ARM templates".

<div>

<div class="title">

Additional resources

</div>

- [Installing a cluster on Azure in a restricted network with user-provisioned infrastructure](upi/installing-restricted-networks-azure-user-provisioned.md#installing-restricted-networks-azure-user-provisioned)

- [Installing a cluster on Azure using ARM templates](upi/installing-azure-user-infra.md#installing-azure-user-infra)

</div>

# Additional resources

- [Configuring an Azure account](installing-azure-account.md#installing-azure-account)

- [Installation process](../../architecture/architecture-installation.md#installation-process_architecture-installation)
