<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# Prerequisites

- You reviewed details about the [OpenShift Container Platform installation and update](../../architecture/architecture-installation.md#architecture-installation) processes.

- You read the documentation on [selecting a cluster installation method and preparing it for users](../overview/installing-preparing.md#installing-preparing).

# Requirements for installing OpenShift Container Platform on Google Cloud

Before installing OpenShift Container Platform on Google Cloud, you must create a service account and configure a Google Cloud project. See [Configuring a Google Cloud project](installing-gcp-account.md#installing-gcp-account) for details about creating a project, enabling API services, configuring DNS, Google Cloud account limits, and supported Google Cloud regions.

If the cloud Identity and Access Management (IAM) APIs are not accessible in your environment, or if you do not want to store an administrator-level credential secret in the `kube-system` namespace, see [Configuring a Google Cloud cluster to use short-term credentials](installing-gcp-customizations.md#installing-gcp-with-short-term-creds_installing-gcp-customizations), [Manually creating long-term credentials for Google Cloud](installing-gcp-customizations.md#manually-create-iam_installing-gcp-customizations), or both for other options.

# Choosing a method to install OpenShift Container Platform on Google Cloud

You can install OpenShift Container Platform on installer-provisioned or user-provisioned infrastructure. The default installation type uses installer-provisioned infrastructure, where the installation program provisions the underlying infrastructure for the cluster. You can also install OpenShift Container Platform on infrastructure that you provision. If you do not use infrastructure that the installation program provisions, you must manage and maintain the cluster resources yourself.

See [Installation process](../../architecture/architecture-installation.md#installation-process_architecture-installation) for more information about installer-provisioned and user-provisioned installation processes.

## Installing a cluster on installer-provisioned infrastructure

You can install a cluster on Google Cloud infrastructure that is provisioned by the OpenShift Container Platform installation program, by using one of the following methods:

- **[Installing a cluster quickly on Google Cloud](installing-gcp-default.md#installing-gcp-default)**: You can install OpenShift Container Platform on Google Cloud infrastructure that is provisioned by the OpenShift Container Platform installation program. You can install a cluster quickly by using the default configuration options.

- **[Installing a customized cluster on Google Cloud](installing-gcp-customizations.md#installing-gcp-customizations)**: You can install a customized cluster on Google Cloud infrastructure that the installation program provisions. You can customize your OpenShift Container Platform network configuration during installation, so that your cluster can coexist with your existing IP address allocations and adhere to your network requirements. The installation program allows for some customization to be applied at the installation stage. Many other customization options are available [post-installation](../../post_installation_configuration/cluster-tasks.md#post-install-cluster-tasks).

- **[Installing a cluster on Google Cloud in a restricted network](installing-restricted-networks-gcp-installer-provisioned.md#installing-restricted-networks-gcp-installer-provisioned)**: You can install OpenShift Container Platform on Google Cloud on installer-provisioned infrastructure by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components. While you can install OpenShift Container Platform by using the mirrored content, your cluster still requires internet access to use the Google Cloud APIs.

- **[Installing a cluster into an existing Virtual Private Cloud](installing-gcp-vpc.md#installing-gcp-vpc)**: You can install OpenShift Container Platform on an existing Google Cloud Virtual Private Cloud (VPC). You can use this installation method if you have constraints set by the guidelines of your company, such as limits on creating new accounts or infrastructure.

- **[Installing a private cluster on an existing VPC](installing-gcp-private.md#installing-gcp-private)**: You can install a private cluster on an existing Google Cloud VPC. You can use this method to deploy OpenShift Container Platform on an internal network that is not visible to the internet.

## Installing a cluster on user-provisioned infrastructure

You can install a cluster on Google Cloud infrastructure that you provision, by using one of the following methods:

- **[Installing a cluster on Google Cloud with user-provisioned infrastructure](installing-gcp-user-infra.md#installing-gcp-user-infra)**: You can install OpenShift Container Platform on Google Cloud infrastructure that you provide. You can use the provided Deployment Manager templates to assist with the installation.

- **[Installing a cluster with shared VPC on user-provisioned infrastructure in Google Cloud](installing-gcp-user-infra-vpc.md#installing-gcp-user-infra-vpc)**: You can use the provided Deployment Manager templates to create Google Cloud resources in a shared VPC infrastructure.

- **[Installing a cluster on Google Cloud in a restricted network with user-provisioned infrastructure](installing-restricted-networks-gcp.md#installing-restricted-networks-gcp)**: You can install OpenShift Container Platform on Google Cloud in a restricted network with user-provisioned infrastructure. By creating an internal mirror of the installation release content, you can install a cluster that does not require an active internet connection to obtain the software components. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content.

# Next steps

- [Configuring a Google Cloud project](installing-gcp-account.md#installing-gcp-account)
