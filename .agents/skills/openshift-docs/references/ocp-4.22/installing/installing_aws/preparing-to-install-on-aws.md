<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can install OpenShift Container Platform on Amazon Web Services using installer-provisioned, user-provisioned infrastructure, or on a single node, depending on the needs of your use case.

The default installation type uses installer-provisioned infrastructure, where the installation program provisions the underlying infrastructure for the cluster.

You can also install OpenShift Container Platform on infrastructure that you provision. If you do not use infrastructure that the installation program provisions, you must manage and maintain the cluster resources yourself.

You can also install OpenShift Container Platform on a single node, which is a specialized installation method that is ideal for edge computing environments.

# Installing a cluster on installer-provisioned infrastructure

You can install a cluster on AWS infrastructure that is provisioned by the OpenShift Container Platform installation program, by using one of the following methods:

You can install OpenShift Container Platform on AWS infrastructure that is provisioned by the OpenShift Container Platform installation program. You can install a cluster quickly by using the default configuration options.

You can install a customized cluster on AWS infrastructure that the installation program provisions. You can also customize your OpenShift Container Platform network configuration during installation, so that your cluster can coexist with your existing IP address allocations and adhere to your network requirements. The installation program allows for some customization to be applied at the installation stage. Many other customization options are available post-installation.

You can install OpenShift Container Platform on AWS on installer-provisioned infrastructure by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components.

You can install OpenShift Container Platform on an existing AWS Virtual Private Cloud (VPC). You can use this installation method if you have constraints set by the guidelines of your company, such as limits when creating new accounts or infrastructure.

You can install a private cluster on an existing AWS VPC. You can use this method to deploy OpenShift Container Platform on an internal network that is not visible to the internet.

OpenShift Container Platform can be deployed into AWS regions that are specifically designed for US government agencies at the federal, state, and local level, as well as contractors, educational institutions, and other US customers that must run sensitive workloads in the cloud.

# Installing a cluster on user-provisioned infrastructure

You can install a cluster on AWS in one of two ways: on infrastructure that you provide or infrastructure that you provide by using an internal mirror of the installation release content.

To install OpenShift Container Platform on AWS infrastructure that you provide, you can use the provided CloudFormation templates to create stacks of AWS resources that represent each of the components required for an OpenShift Container Platform installation.

To install a cluster that does not require an active internet connection to obtain the software components, install OpenShift Container Platform on AWS infrastructure that you provide by using an internal mirror of the installation release content. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content. While you can install OpenShift Container Platform by using the mirrored content, your cluster still requires internet access to use the AWS APIs.

# Installing a cluster on a single node

Installing OpenShift Container Platform on a single node alleviates some of the requirements for high availability and large scale clusters. However, you must address requirements for installing on a single node, and the additional requirements for installing single-node OpenShift on a cloud provider.

After addressing the requirements for single node installation, use the installing a customized cluster on AWS procedure to install the cluster. The installing single-node OpenShift manually section contains an exemplary `install-config.yaml` file when installing an OpenShift Container Platform cluster on a single node.

# Additional resources

- [Installing a cluster quickly on AWS](ipi/installing-aws-default.md#installing-aws-default)

- [Installing a customized cluster on AWS](ipi/installing-aws-customizations.md#installing-aws-customizations)

- [Post-installation](../../post_installation_configuration/cluster-tasks.md#post-install-cluster-tasks)

- [Installing a cluster on AWS in a restricted network](ipi/installing-restricted-networks-aws-installer-provisioned.md#installing-restricted-networks-aws-installer-provisioned)

- [Installing a cluster on an existing Virtual Private Cloud](ipi/installing-aws-vpc.md#installing-aws-vpc)

- [Installing a private cluster on an existing VPC](ipi/installing-aws-private.md#installing-aws-private)

- [Installing a cluster on AWS into a government or secret region](ipi/installing-aws-specialized-region.md#installing-aws-specialized-region)

- [Installing a cluster on AWS infrastructure that you provide](upi/installing-aws-user-infra.md#installing-aws-user-infra)

- [Installing a cluster on AWS in a restricted network with user-provisioned infrastructure](upi/installing-restricted-networks-aws.md#installing-restricted-networks-aws)

- [Installation process](../../architecture/architecture-installation.md#installation-process_architecture-installation)
