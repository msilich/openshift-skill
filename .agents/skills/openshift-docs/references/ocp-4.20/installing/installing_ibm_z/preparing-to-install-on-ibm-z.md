<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can install an OpenShift Container Platform cluster on IBM Z® and IBM® LinuxONE using a variety of different installation methods. Each method has qualities that can make them more suitable for different use cases, such as installing a cluster in a disconnected environment or installing a cluster with minimal configuration and provisioning.

> [!NOTE]
> While this document refers only to IBM Z®, all information in it also applies to IBM® LinuxONE.

# Choosing a method to install OpenShift Container Platform on IBM Z or IBM LinuxONE

The OpenShift Container Platform installation program offers the following methods for deploying a cluster on IBM Z®:

- **Interactive**: You can deploy a cluster with the web-based [Assisted Installer](https://access.redhat.com/documentation/en-us/assisted_installer_for_openshift_container_platform). This method requires no setup for the installer, and is ideal for connected environments like IBM Z®.

- **Local Agent-based**: You can deploy a cluster locally with the [Agent-based Installer](../installing_with_agent_based_installer/preparing-to-install-with-agent-based-installer.md#preparing-to-install-with-agent-based-installer). It provides many of the benefits of the Assisted Installer, but you must download and configure the [Agent-based Installer](https://console.redhat.com/openshift/install/ibmz/agent-based) first. Configuration is done with a command-line interface (CLI). This approach is ideal for disconnected networks.

- **Full control**: You can deploy a cluster on infrastructure that you prepare and maintain, which provides maximum customizability. You can deploy clusters in connected or disconnected environments.

|  | Assisted Installer | Agent-based Installer | User-provisioned installation | Installer-provisioned installation |
|----|----|----|----|----|
| IBM Z® with z/VM | ✓ | ✓ | [✓](upi/installing-ibm-z.md#installing-ibm-z) |  |
| Restricted network IBM Z® with z/VM |  | ✓ | [✓](upi/installing-restricted-networks-ibm-z.md#installing-restricted-networks-ibm-z) |  |
| IBM Z® with RHEL KVM | ✓ | ✓ | [✓](upi/installing-ibm-z-kvm.md#installing-ibm-z-kvm) |  |
| Restricted network IBM Z® with RHEL KVM |  | ✓ | [✓](upi/installing-restricted-networks-ibm-z-kvm.md#installing-restricted-networks-ibm-z-kvm) |  |
| IBM Z® in an LPAR | ✓ | ✓ | [✓](upi/installing-ibm-z-lpar.md#installing-ibm-z-lpar) |  |
| Restricted network IBM Z® in an LPAR |  | ✓ | ✓ |  |

IBM Z® installation options

For more information about the installation process, see the [Installation process](../../architecture/architecture-installation.md#installation-process_architecture-installation).

# User-provisioned infrastructure installation of OpenShift Container Platform on IBM Z

User-provisioned infrastructure requires the user to provision all resources required by OpenShift Container Platform.

> [!IMPORTANT]
> The steps for performing a user-provisioned infrastructure installation are provided as an example only. Installing a cluster with infrastructure you provide requires knowledge of the IBM Z® platform and the installation process of OpenShift Container Platform. Use the user-provisioned infrastructure installation instructions as a guide; you are free to create the required resources through other methods.

- **[Installing a cluster with z/VM on IBM Z® and IBM® LinuxONE](upi/installing-ibm-z.md#installing-ibm-z)**: You can install OpenShift Container Platform with z/VM on IBM Z® or IBM® LinuxONE infrastructure that you provision.

- **[Installing a cluster with z/VM on IBM Z and IBM LinuxONE in a disconnected environment](upi/installing-restricted-networks-ibm-z.md#installing-restricted-networks-ibm-z)**: You can install OpenShift Container Platform with z/VM on IBM Z® or IBM® LinuxONE infrastructure that you provision in a restricted or disconnected network by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content.

- **[Installing a cluster with RHEL KVM on IBM Z® and IBM® LinuxONE](upi/installing-ibm-z-kvm.md#installing-ibm-z-kvm)**: You can install OpenShift Container Platform with KVM on IBM Z® or IBM® LinuxONE infrastructure that you provision.

- **[Installing a cluster with RHEL KVM on IBM Z® and IBM® LinuxONE in a disconnected environment](upi/installing-restricted-networks-ibm-z-kvm.md#installing-restricted-networks-ibm-z-kvm)**: You can install OpenShift Container Platform with RHEL KVM on IBM Z® or IBM® LinuxONE infrastructure that you provision in a restricted or disconnected network by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content.

- **[Installing a cluster in an LPAR on IBM Z® and IBM® LinuxONE](upi/installing-ibm-z-lpar.md#installing-ibm-z-lpar)**: You can install OpenShift Container Platform in a logical partition (LPAR) on IBM Z® or IBM® LinuxONE infrastructure that you provision.

- **[Installing a cluster in an LPAR on IBM Z® and IBM® LinuxONE in a disconnected environment](upi/installing-restricted-networks-ibm-z-lpar.md#installing-restricted-networks-ibm-z-lpar)**: You can install OpenShift Container Platform in an LPAR on IBM Z® or IBM® LinuxONE infrastructure that you provision in a restricted or disconnected network by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content.
